from models.basemodel import BaseModel


class Review(BaseModel):
    """Stores information about a user review about an accomodation"""
    name = ""
    text = ""