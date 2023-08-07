from models.basemodel import BaseModel


class Amenity(BaseModel):
    """Stores information about amenities instance"""
    amenity_type = ""
    no_of_amenities = 0