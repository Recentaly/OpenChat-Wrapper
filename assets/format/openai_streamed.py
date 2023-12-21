from ..typing import OpenAI_Streamed, Pointer

# to handle pointers
from ..pointers.pointer_handler import from_address

# json dumps for json formatting
from json import dumps

# this function returns a streamed OpenAI-type response
def get_openai_streamed(model: Pointer, content: str) -> OpenAI_Streamed | dict[str | int]:

    print(from_address(model))

    return dumps({
        "object": "chat.completion.chunk",
        "model": f"{from_address(model).id}",
        "choices": [{
            "index": 0,
            "delta": {
                "content": f"{content} ",
            },
            "finish_reason": None,
        }],
    })

# this returns the last chunk in an OpenAI formatted response
def get_streamed_last(model: Pointer) -> OpenAI_Streamed | str:

    return dumps({
        "object": "chat.completion.chunk",
        "model": f"{from_address(model).id}",
        "choices": [
            {
                "index": 0,
                "delta": {},
                "finish_reason": "stop",
            }
        ]
    })