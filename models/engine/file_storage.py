import json
import os
import importlib
from models.base_model import BaseModel
from models.student import Student

class FileStorage:
    """Serializes instances to a JSON file and deserializes back to instances"""
    
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary of __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Adds a new object to the storage dictionary"""
        if obj:
            key = f"{obj.__class__.__name__}.{obj.id}"
            FileStorage.__objects[key] = obj

    def save(self):
        """Saves objects to a JSON file"""
        with open(FileStorage.__file_path, 'w') as f:
            json.dump({k: v.to_dict() for k, v in FileStorage.__objects.items()}, f)

    def reload(self):
        """Loads objects from a JSON file"""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as f:
                objs = json.load(f)
                for k, v in objs.items():
                    cls_name = k.split('.')[0]
                    cls = self.get_class(cls_name)
                    if cls:
                        FileStorage.__objects[k] = cls(**v)

    def get_class(self, class_name):
        """Retrieves a class based on class name"""
        try:
            module = importlib.import_module(f"models.{class_name.lower()}")
            return getattr(module, class_name)
        except (ImportError, AttributeError) as e:
            print(f"** error: {e}")
            return None
