#!/usr/bin/python3
"""
module to define class that manages file storage for hbnb
"""
import json

class FileStorage:
    """class to manage of hbnb models in JSON format"""
    __file_path = "file.json"
    __objects = {}

    def __init__(self, file_path=None):
        "initializes file storage class"
        if file_path:
            self.__file_path = file_path
        self.reload()

    def all(self):
        """returns dictionary of models in storage"""
        return FileStorage.__objects
    
    def save(self):
        "save storage dictionary to file"
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    