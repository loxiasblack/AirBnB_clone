#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """BaseModel class"""

    def __init__(self):
        """instantiation"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.update_at = datetime.now()

    def __str__(self):
        return "[BaseModel] ({}) {}".format(self.id, self.__dict__)

    def save(self):
        """update my pulique attribute updated_at with current time updated"""
        self.updated_at = datetime.now()

    def to_dict(self):
        "Method that return a dictionary of my instances"

        return {
                "id": self.id,
                "__class__": self.__class__.__name__,
                "created_at": self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f"),
                "updated_at": self.update_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
                }