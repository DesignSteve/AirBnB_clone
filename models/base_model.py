#!/usr/bin/python3
"""The foundational model for this script is the base"""

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """All other classes will derive from this class"""

    def __init__(self, *args, **kwargs):
        """This method initializes instance attributes.

        Parameters:
            - *args: A list of arguments.
            - **kwargs: A dictionary of key-value arguments.
        """

        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Provides the official string representation."""
        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """public instance attribute updated_at"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """This function yields a dictionary comprising all the keys and
        values from the dict attribute."""

        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
