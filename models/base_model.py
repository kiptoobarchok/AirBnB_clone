#!/usr/bin/python3
import json
import uuid
from datetime import datetime

class BaseModel():
    def __init__(self, id, created_at, update_at):
        self.id = str(uuid.uuid4())
        self.created_at  = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self)