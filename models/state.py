#!/usr/bin/python3
"""
This module defines the `State` class, representing a state within the system's geographical hierarchy.

The `State` class inherits core functionalities from the `BaseModel` class, providing the ability to manage and persist state information.
"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    Represents a geographical state entity with its unique name.

    Attributes:
        name (str): The official name of the state. This identifier should be unique within the system.
    """

    name = ""

