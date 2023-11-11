#!/usr/bin/python3
"""
Module with the file_storage engine
"""
import json
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User


class FileStorage:
    """
    Representation of the FileStorage class
    """
    __file_path = 'file.json'
    __objects = {}
    classes = {"BaseModel": BaseModel,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Review": Review,
            "User": User
    }

    def all(self):
        """
        Public class method that returns all __objects
        """
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        if obj:
            key = '{}.{}'.format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        my_dict = {}

        for key, value in self.__objects.items():
            my_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding='UTF-8') as f:
            json.dump(my_dict, f)

    def reload(self):
        """ deserializes the json file to objects if it exists, otherwise do nothing """
        try:
            with open(self.__file_path, 'r', encoding='UTF-8') as f:
                reloaded_dict = json.load(f)
            for key, value in reloaded_dict.items():
                obj = self.classes[value['__class__']](**value)
                self.__objects[key] = obj
        except FileNotFoundError:
            pass
