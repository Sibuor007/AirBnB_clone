#!/usr/bin/python3
"""
This module defines the `City` class, representing a specific city within the system.

The `City` class inherits the base functionalities from the `BaseModel` class, adding attributes
and methods relevant to managing city information.
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    Represents a city entity with essential attributes for location identification.

    Attributes:
        state_id (str): The unique identifier of the associated state. This links the city to its corresponding state.
        name (str): The official name of the city.
    """

    state_id = ""
    name = ""

