#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone
"""
import json
import copy


class FileStorage:
    """This class manages storage of hbnb models in JSON format
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage
        """
        if cls:
            my_dict = copy.deepcopy(FileStorage.__objects)
            for key, val in FileStorage.__objects.items():
                if val.__class__ is not cls:
                    del my_dict[key]
            return my_dict
        return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary
        """
        key = obj.__class__.__name__ + '.' + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """Saves storage dictionary to file
        """
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """this method delete obj
        from __objects
        """
        if obj:
            for key, val in self.__objects.items():
                if val is obj:
                    del FileStorage.__objects[key]
                    break

    def close(self):
        """this deserializing the JSON
        file to objects
        """
        self.reload()
