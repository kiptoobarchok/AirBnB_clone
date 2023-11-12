#!/usr/bin/python3
import json
import uuid
from datetime import datetime

class BaseModel():
    "define base class"
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at  = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        "return a string representation"
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
    
    def save(self):
        "update"
        self.updated_at = datetime.now()

    
    
    def to_dict(self):
        """Return a dictionary representation of the BaseModel instance."""
        class_name = self.__class__.__name__
        attributes = self.__dict__.copy()
        attributes['created_at'] = self.created_at.isoformat()
        attributes['updated_at'] = self.updated_at.isoformat()
        attributes['__class__'] = class_name
        return attributes