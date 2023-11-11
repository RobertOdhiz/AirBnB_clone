#!/usr/bin/python3
"""
Class Place module
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    representation of Place class

    public class attributes:
        city_id - empty string(City.id)
        user_id - empty string(User.id)
        name - empty string
        description - empty string
        number_rooms - 0
        number_bathrooms - 0
        max_guest - 0
        price_per_night - 0
        latitude - 0.0
        longitude - 0.0
        amenity_ids - empty list(Amenity.id)
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_per_night = 0
    latitude = 0.0
    latitude = 0.0
    amenity_ids = []
