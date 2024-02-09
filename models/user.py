#!/usr/bin/python3
"""
This module defines the `User` class, representing individual users within the system who perform various actions and interactions.

The `User` class inherits core functionalities from the `BaseModel` class, enabling object management and persistence for user data.
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    Represents an individual user account with essential identification and contact information.

    Attributes:
        email (str): The unique email address of the user, serving as their login credential and primary means of communication.
        password (str): The user's encrypted password, stored securely using appropriate hashing techniques to ensure data privacy.
        first_name (str): The user's first name, used for personalization and identification purposes.
        last_name (str): The user's last name, used for personalization and identification purposes.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

