#!/usr/bin/python3
"""
Module with Review class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Representation of Review class
    """
    place_id = ""
    user_id = ""
    text = ""
