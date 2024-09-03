#!/usr/bin/python3
"""Module base_model

This Module contains a definition for BaseModel Class
"""

import uuid
from datetime import datetime

import models


class BaseModel:
    """BaseModel Class"""

    def __init__(self, *args, **kwargs):
        """__init__ method & instantiation of class Basemodel

        Args:
            *args.
            **kwargs (dict): Key/value pairs
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs is not None and len(kwargs) > 0:
            for k, v in kwargs.items():
                if k == "__class__":
                    continue
                elif k in ["created_at", "updated_at"]:
                    setattr(self, k, datetime.fromisoformat(v))
                else:
                    setattr(self, k, v)
        else:
            models.storage.new(self)

    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.now()
        models.storage.save()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all
        keys/values of __dict__ of the instance.
        """
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = self.__class__.__name__
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        return dictionary

    def __str__(self):
        """Return string representation of the instance"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.to_dict()}"
