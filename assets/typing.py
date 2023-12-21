import typing as t

Headers = t.Dict[str, str]
Address = t.NewType("Address", int)
Pointer = t.Union[Address, Address]
Any = t.Any
Url = t.NewType("Url", str)
Key = t.NewType("Key", str)
Messages = t.List[str]
Model = t.Any
OpenAI_Response = t.Dict[str, str | int]
OpenAI_Streamed = t.Dict[str, str | int]

__all__ = ["Headers", "Address", "Pointer", "Any", "Url", "Key", "Messages", "Model", "OpenAI_Response", "OpenAI_Streamed"]