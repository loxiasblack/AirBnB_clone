#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """BaseModel class"""

    def __init__(self, *args, **kwargs):
        from models import storage
        """instantiation"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

            storage.new(self)

    def __str__(self):
        return "[BaseModel] ({}) {}".format(self.id, self.__dict__)

    def save(self):
        """update my pulique attribute updated_at with current time updated"""
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        "Method that return a dictionary of my instances"

        return {
                "id": self.id,
                "__class__": self.__class__.__name__,
                "created_at": self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f"),
                "updated_at": self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
                }
