from ..typing import OpenAI_Response, Pointer

# to handle pointers
from ..pointers.pointer_handler import from_address

# this function returns a generic OpenAI-type response
def get_openai_generic(model: Pointer, role: Pointer, content: str, finish_reason: Pointer) -> OpenAI_Response | dict[str | int]:

    return {
        "object": "chat.completion",
        "model": f"{from_address(model).id}",
        "choices": [{
            "index": 0,
            "message": {
                "role": f"{from_address(role)}",
                "content": f"{content}",
            },
            "finish_reason": f"{from_address(finish_reason)}",
        }],
    }

# Path: assets/format/openai_static.py