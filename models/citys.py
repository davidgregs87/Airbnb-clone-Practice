from models.basemodel import BaseModel


class City(BaseModel):
    """Stores all city instances"""
    country = ""
    city = ""