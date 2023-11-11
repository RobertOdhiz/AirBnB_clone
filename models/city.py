#!/usr/bin/python3
"""
Module with City Class that inherits from BaseModel
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Representation of City class

    public class attributes:
        state_id - empty string(will be State.id)
        name - empty string
    """

    state_id = ""
    name = ""
