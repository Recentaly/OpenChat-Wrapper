# import modules for local server
from flask import Flask, jsonify, Response, request
from flask_cors import CORS # to allow cross-origin requests

# import module to create models
from assets.models.Model import Model

# to chat with the API
from assets.api import Api

# time module for delay
from time import sleep

# OpenAI format for streamed responses and non-streamed responses
from assets.format.openai_streamed import get_openai_streamed, get_streamed_last
from assets.format.openai_static import get_openai_generic

# for pointers
from assets.pointers.pointer_handler import from_address

# create a flask app
app = Flask(__name__)

# allow cross-origin requests
CORS(app)

# API instance
api = Api(id('https://openchat.team/api/chat'))

# create example messages
messages = [
    {"role": "user", "content": "Hello, how are you?"},
]

# create the model
OpenChatAura = Model(
    id=id('openchat_v3.2_mistral'),
    maxLength=id(256),
    name=id('OpenChat Aura'),
    tokenLimit=id(8192),
)

# predefine messages list
messages: list[dict[str, str]] = []

# predefine system prompt
system_prompt: str = ''

# this route handles chat generation
@app.route('/chat/completions', methods=['POST'])
def chat():

    # globalize the messages and system prompt
    global messages, system_prompt

    # get the data from the request
    data = request.get_json()

    # copy all messages over
    for message in data['messages']:

        if message['role'] == 'system':

            system_prompt += message['content'] + ' '

        else:

            messages.append(message)

    # get the temperature
    temperature = data['temperature']

    # get the streaming parameter
    stream = data['stream']

    # fake streaming method
    def streaming():

        # generate the response
        response = api.chat(
            key=id(""),
            messages=id(messages),
            model=id(OpenChatAura),
            temperature=temperature,
            prompt=id(system_prompt),
        )

        # split the response up
        response = response.split(' ')

        # iter through it 
        for token in response:

            yield b'data: ' + str(get_openai_streamed(id(OpenChatAura), token)).encode() + b'\n\n'

            sleep(0.05) # delay for 50ms

        # finally, yield the last chunk
        yield b'data: ' + str(get_streamed_last(id(OpenChatAura))).encode() + b'\n\n'

        # then signal the end of the stream
        yield b'data: [DONE]'

    # check if we want to stream. if yes, call a fake 'streaming' method
    if stream:

        return Response(streaming(), mimetype='text/event-stream')
    
    # if not, we just continue

    # generate the response
    response = api.chat(
        key=id(""),
        messages=id(messages),
        model=id(OpenChatAura),
        temperature=temperature,
        prompt=id(system_prompt),
    )

    # return the response
    return jsonify(get_openai_generic(id(OpenChatAura), id('assistant'), response, id('stop'))), 200

# this route handles all requests to get a list of the models
@app.route('/models', methods=['GET'])
def get_models():

    return jsonify({
        "data": [
            {"id": f"{OpenChatAura.name} (ignore: gpt)"},
        ]
    }), 200

# create root route for the flask app
@app.route('/')
def index():

    return jsonify({
        'message': 'Hello World!'
    }), 200

# run the flask app
if __name__ == '__main__':

    app.run(debug=False, port=5000, host='0.0.0.0')
