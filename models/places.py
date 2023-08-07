from models.basemodel import BaseModel


class Place(BaseModel):
    """Stores information about a places and any other relevant information"""
    owner_name = ""
    price_by_night = 0
    address = ""
    longitude = 0.0
    lattitude = 0.0
    description = ""
    