#!/usr/bin/python3
"""
This module defines the `Place` class, representing a physical location with associated attributes and potential for linking to various entities.

The `Place` class inherits core functionalities from the `BaseModel` class, providing essential object management and persistence features.
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """
    Represents a physical location with attributes relevant to accommodation, amenities, and user relationships.

    Attributes:
        city_id (str): The unique identifier of the associated city. This establishes a foreign key relationship with the City class.
        user_id (str): The unique identifier of the owner or responsible user. This connects the place to a specific User object.
        name (str): The official name of the place.
        description (str): A detailed description of the place, highlighting its features and offerings.
        number_rooms (int): The total number of rooms available in the place.
        number_bathrooms (int): The total number of bathrooms available in the place.
        max_guest (int): The maximum number of guests allowed to stay in the place at once.
        price_by_night (int): The base price charged per night for accommodation in the place.
        latitude (float): The geographical latitude coordinate of the place's location.
        longitude (float): The geographical longitude coordinate of the place's location.
        amenity_ids (list): A list of unique identifiers (strings) referencing associated Amenity objects, enabling many-to-many relationships.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

