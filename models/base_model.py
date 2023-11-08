#!/usr/bin/python3
"""
Module with Base_user class
"""
import uuid
from datetime import datetime


class BaseModel:
    """
    Base model class that will be inherited from while creating instances
    """
    def __init__(self):
        """Instantiates the BaseModel class"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns the string formal representation of an object
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ Saves the instance created by updated the updated_at field """
        self.pdated_at = datetime.now()

    def to_dict(self):
        """ returns a dictionary containing all keys/values of __dict__ of the instance """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
