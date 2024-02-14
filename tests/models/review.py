#!/usr/bin/python3
"""
This module defines the `Review` class, representing an individual review submitted by a user for a specific place.

The `Review` class inherits core functionalities from the `BaseModel` class, allowing for object management and persistence within the system.
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Represents a feedback record about a place, submitted by a user and linked to the corresponding place and user objects.

    Attributes:
        place_id (str): The unique identifier of the associated place. This establishes a foreign key relationship with the Place class.
        user_id (str): The unique identifier of the user who submitted the review. This connects the review to a specific User object.
        text (str): The written content of the review, expressing the user's opinion and experience regarding the place.
    """

    place_id = ""
    user_id = ""
    text = ""

