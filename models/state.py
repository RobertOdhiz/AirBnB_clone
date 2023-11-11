#!/usr/bin/python3
"""
Module with State Class that inherits from BaseModel
"""
from models.base_models import BaseModel


class State(BaseModel):
    """
    Class Representation of State Class
    Public class attributes:
        name - Default as an empty string
    """
    name = ""
