#!/usr/bin/python3
import json
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
        self.update_at = datetime.now()

    def to_dict(self):
        self.created_at = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        self.update_at = self.update_at.strftime("%Y-%m-%dT%H:%M:%S.%f")

        return self.__dict__
