#!/usr/bin/python3
"""
This module defines the `Amenity` class, representing various amenities associated with properties.

The `Amenity` class inherits from the `BaseModel` class, providing core attributes and methods
for object management and persistence within the application.
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Represents an amenity offered by a property, such as a pool, gym, or parking.

    Attributes:
        name (str): The descriptive name of the amenity (e.g., "Swimming Pool", "Fitness Center").
    """

    name = ""

