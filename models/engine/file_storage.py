#!/usr/bin/python3
"""This is a FileStorage class module"""
import datetime
import json
import os


class FileStorage:

    """Class for retrieving and storing data"""
    __file_path = "file,json"
    __objects = {}

    def all(self):
        """return dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Set __objects obj with <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialization of __objects to JSON file"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(d, f)

    def classes(self):
        """Return dictionary of valid classes with their references"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {"BaseModel": BaseModel,
                   "User": User,
                   "Place": Place,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Review": Review}
        return classes

    def reload(self):
        """Reload stored objects"""
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            obj_dict = json.load(f)
            obj_dict = {k: self.classes()[v["__class__"]](**v)
                        for k, v in obj_dict.items()}
            # TODO: overwrite or insert
            FileStorage.__objects = obj_dict

    def attributes(self):
        """Return valid attribute and their types classname"""
        attributes = {
            "BaseModel":
                {"id": str,
                 "created_at": datetime.datetime,
                 "updated_at": datetime.datetime},
            "User":
                {"email": str,
                 "password": str,
                 "first_name": str,
                 "last_name": str},
            "Place":
                {"city_id": str,
                 "user_id": str,
                 "name": str,
                 "description": str,
                 "number_rooms": int,
                 "number_bathrooms": int,
                 "max_quest": int,
                 "price_by_night": int,
                 "latitude": float,
                 "longitude": float,
                 "amenity_ids": list},
            "State":
                {"name": str},
            "City":
                {"state_id": str,
                 "name": str},
            "Amenity":
                {"name": str},
            "Review":
                {"place_id": str,
                 "user_id": str,
                 "text": str}
        }
        return attributes
