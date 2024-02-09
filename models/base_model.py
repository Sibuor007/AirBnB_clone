#!/usr/bin/python3
""" This Modulue defines the BaseModel class """

from datetime import datetime
from uuid import uuid4
import models


class BaseModel:
    """ A Superclass that represents the Base of the AirBnB project """

    def __init__(self, *args, **kwargs):
        """This is the constructor for the BaseModel class

        Args:
            *args (any): to be used in the future
            **kwargs (dict): key value arguments
        """
        format_n = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, format_n)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def do_save(self):
        """ For updating the updated_at to current datetime """
        self.updated_at = datetime.today()
        models.storage.save()

    def do_ict(self):
        """Returns the dictionary of the BaseModel instance

        Includes the key/value pair __class__
        """
        st_dict = self.__dict__.copy()
        st_dict["created_at"] = self.created_at.isoformat()
        st_dict["updated_at"] = self.updated_at.isoformat()
        st_dict["__class__"] = self.__class__.__name__
        return st_dict

    def __str__(self):
        """ Return the official string representation of the BaseModel instance """
        obj_name = self.__class__.__name__
        return "[{}], ({}), {}".format(obj_name, self.id, self.__dict__)
