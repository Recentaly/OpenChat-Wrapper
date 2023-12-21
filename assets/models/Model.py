# This file is used to get a list of models that are available for use in the API.

from ..typing import Pointer

# for pointer handling
from ..pointers.pointer_handler import from_address

class Model(object):

    def __init__(self, id: Pointer, maxLength: Pointer, name: Pointer, tokenLimit: Pointer) -> None:

        """Initialize the Model class."""
        self.id = from_address(id)
        self.maxLength = from_address(maxLength)
        self.name = from_address(name)
        self.tokenLimit = from_address(tokenLimit)