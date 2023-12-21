"""Pointer handler."""
from ctypes import cast, py_object
from ..typing import Any, Pointer


def from_address(address: Pointer) -> Any | py_object:

    """Get object from address."""
    return cast(address, py_object).value

# Path: assets/pointers/pointer_handler.py