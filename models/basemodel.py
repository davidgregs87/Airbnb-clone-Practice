from datetime import datetime
from uuid import uuid4
import models



class BaseModel:
    """This is our basemodel for all other models"""
    def __init__(self, *args, **kwargs):
            """Initialize public instance attribute"""
            if not kwargs:
                """If kwargs is empty"""
                self.id = str(uuid4())
                self.created_at = datetime.now()
                self.updated_at = self.created_at
                models.storage.new(self)
            else:
                """If kwargs is not empty, delete the key __class__ from the dictionary
                and change the date to be a datetime object not a string object as before"""
                if "__class__" in kwargs.keys():
                    del kwargs["__class__"]
                for k, v in kwargs.items():
                    kwargs["created_at"] = datetime.now()
                    kwargs["updated_at"] = datetime.now()
                    setattr(self, k, v)
                    

    def __str__(self) -> str:
        """A string representation"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    
    def save(self):
        """updates the public instance attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()
    
    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__ of the instance"""
        self.created_at = datetime.now().strftime("%Y, %m, %d %H, %M, %S. %f")
        self.updated_at = self.created_at
        return self.__dict__
    
