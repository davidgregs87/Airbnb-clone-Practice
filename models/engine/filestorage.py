from models.basemodel import BaseModel
from models.user import User
from models.reviews import Review
from models.citys import City
from models.amenities import Amenity
from models.states import State
from models.places import Place
import json
import os



class FileStorage:
    """that serializes instances to a JSON file and deserializes JSON file to instances"""
    __file_path = 'new.json'
    __objects = {}

    def all(self, cls=None):
        """Returns the list of objects of one type of class.
        Example below with State - its an optional filtering"""
        if cls is None:
            return FileStorage.__objects
        filter_dict = {}
        for k, v in FileStorage.__objects.items():
            key = k.split('.')
            if key[0] == cls.__name__:
                filter_dict[k] = v
        return filter_dict
    
    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        value = obj
        clasname = obj.__class__.__name__
        obj = clasname + '.' + obj.id
        self.__objects[obj] = value
    
    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, "w") as f:
            dic = {}
            for key, value in self.__objects.items():
                dic[key] = value.to_dict()
            json.dump(dic, f)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file (__file_path) exists ;"""
        classes = {"BaseModel": BaseModel, "User": User, "Review": Review, "City": City, "Amenity": Amenity,
                   "State": State, "Place": Place}
        if os.path.exists(self.__file_path):
            with open(self.__file_path) as f:
                objs = json.load(f)
                for key, value in objs.items():
                    obj_class = key.split('.')[0]
                    self.__objects[key] = classes[obj_class](**value)

    def delete(self, obj=None):
        """delete obj from __objects if its inside -
        if obj is equal to None, the method should not do anything"""
        if obj is not None:
            key = obj.__class__.__name__ + '.' + obj.id
            del FileStorage.__objects[key]



