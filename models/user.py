#!/usr/bin/python3
"""
Module with user class that inherits from BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """ Representation of User model """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
