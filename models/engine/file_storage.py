#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """
            Returns a dictionary of models currently in storage
            or the list of objects of one type of class
        """
        if cls:
            class_dict = dict()
            for key, value in FileStorage.__objects.items():
                key_type = key[:key.find('.')]
                try:
                    cls_type = (str(cls)).split('.')[2].rstrip(">'")
                except IndexError:
                    pass
                if key_type == cls_type:
                    class_dict[key] = value
            return class_dict
        else:
            return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
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
        """Deletes obj from __objects if it’s inside"""
        if obj:
            obj_dict = {}
            # make a dummy copy to avoid runtime error
            all_objs = self.all().copy()
            for key in self.all().keys():
                if obj.__class__.__name__ == key[:key.find('.')] and \
                        obj.id == key[key.find('.') + 1:]:
                    del all_objs[key]
            FileStorage.__objects = all_objs
            return FileStorage.__objects

    def close(self):
        """
            To close the FileStorage and deserialize the objects
        """
        self.reload()
