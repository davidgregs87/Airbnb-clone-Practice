from models.basemodel  import BaseModel


class User(BaseModel):
    """A user class that stores information
    about a user"""
    email = ""
    password = ""
    