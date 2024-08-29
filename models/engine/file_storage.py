import json
import os

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Adds new object to __objects"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Saves __objects to a JSON file"""
        with open(self.__file_path, 'w') as f:
            json_objects = {k: v.to_dict() for k, v in self.__objects.items()}
            json.dump(json_objects, f, indent=4)  # Added indent for readability

    def reload(self):
        """Loads __objects from a JSON file"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                try:
                    json_objects = json.load(f)
                    for key, obj_dict in json_objects.items():
                        class_name = obj_dict.pop("__class__")
                        cls = current_classes.get(class_name, BaseModel)
                        self.__objects[key] = cls(**obj_dict)
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON: {e}")
                except Exception as e:
                    print(f"Unexpected error: {e}")
