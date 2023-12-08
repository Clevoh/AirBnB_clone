#!/usr/bin/python3
"""Module containing FileStorage class"""

from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import os.path
import json


class FileStorage():
    """
    class that serializes instances to a JSON file
    and deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """all method returns the __objects dictionary"""
        return FileStorage.__objects

    def new(self, obj):
        """
        new method update __objects dictionary
        each time that a new object is created
        """
        if obj:
            key = type(obj).__name__ + "." + obj.id
            FileStorage.__objects[key] = obj

    def save(self):
        """
        saves all objects inside a file in JSON represetation
        """
        m = {}
        for key, obj in FileStorage.__objects.items():
            m[key] = obj.to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as json_f:
            json.dump(m, json_f)

    def reload(self):
        """
        reload method that update __objects dictionary from JSON file
        """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as js_f:
                for key, obj in json.loads(js_f.read()).items():
                    obj = eval(obj['__class__'])(**obj)
                    FileStorage.__objects[key] = obj
