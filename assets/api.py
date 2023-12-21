# requests module is used to make requests to the API
import requests

# get_headers is a function that returns the headers for the request
from assets.headers.get_headers import get_headers

# from_address is a function that returns the object from the address
from assets.pointers.pointer_handler import from_address

# typing module is used to type hint the code
from assets.typing import Any, Pointer, Url, Headers

# this class is used to interact with the API
class Api():

    def __init__(self, url: Pointer) -> None:

        """Initialize the API class."""
        self.url: Url | str = from_address(url)

        # get the default headers
        self.headers: Headers = get_headers()

        # create a session
        self.session = requests.Session()

    def chat(self, key: Pointer, messages: Pointer, model: Pointer, prompt: Pointer, temperature: int = 0.8) -> Any:

        """This function is used to generate a chat response from the API."""

        # compile the data
        data = {
            "key": from_address(key),
            "messages": from_address(messages),
            "model": {
                "id": from_address(model).id,
                "maxLength": from_address(model).maxLength,
                "name": from_address(model).name,
                "tokenLimit": from_address(model).tokenLimit,
            },
            "prompt": from_address(prompt),
            "temperature": temperature
        }

        # make the request
        with self.session.post(self.url, json=data, headers=self.headers) as response:

            # check for any errors and raise them
            response.raise_for_status()

            # return the response
            return response.text
            
