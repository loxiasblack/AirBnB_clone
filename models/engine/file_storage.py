#!/usr/bin/python3
import json


class FileStorage:
    """a class that allow to serialize and
        desirilize object and save"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """"""
        return FileStorage.__objects

    def new(self, obj):
        """"""
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            FileStorage.__objects[key] = obj

    def save(self):
        """serialize from python to json file"""
        from models.base_model import BaseModel
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump({k: v.to_dict() for k, v in
                       FileStorage.__objects.items() if
                       isinstance(v, BaseModel)}, f)

    def reload(self):
        """"""
        from models.base_model import BaseModel
        try:
            with open(FileStorage.__file_path, "r") as f:
                objects = json.load(f)
            for key, value in objects.items():
                FileStorage.__objects[key] = BaseModel(**value)
        except FileNotFoundError:
            pass
        except json.decoder.JSONDecodeError:
            pass
