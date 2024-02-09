#!/usr/bin/python3
"""
This module provides the FileStorage class, a robust abstraction layer for data persistence.
"""

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
import json


class FileStorage:
    """
    Encapsulates storage operations for seamless object persistence within a JSON file.

    Attributes:
        __file_path (str): File path to store objects.
        __objects (dict): Dictionary housing instantiated objects.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Retrieves a comprehensive dictionary of all stored objects.

        Returns:
            dict: A deep copy of the __objects dictionary.
        """

        return FileStorage.__objects.copy()

    def new(self, obj):
        """
        Register a new object within the storage system.

        Args:
            obj: The object to be added to storage.
        """

        obj_name = obj.__class__.__name__
        FileStorage.__objects[f"{obj_name}.{obj.id}"] = obj

    def save(self):
        """
        Persists all objects to the designated JSON file.
        """

        curr_dict = FileStorage.__objects
        obj_dict = {obj: curr_dict[obj].to_dict() for obj in curr_dict.keys()}
        with open(FileStorage.__file_path, "w") as file_0:
            json.dump(obj_dict, file_0)

    def reload(self):
        """
        Restores objects from the JSON file, if it exists.
        """

        try:
            with open(FileStorage.__file_path) as file_0:
                obj_dict = json.load(file_0)
                for item in obj_dict.values():
                    class_name = item["__class__"]
                    del item["__class__"]
                    self.new(eval(class_name)(**item))
        except FileNotFoundError:
            return

