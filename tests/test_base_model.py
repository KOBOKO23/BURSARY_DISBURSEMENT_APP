#!/usr/bin/python3

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models.base_model import BaseModel

# Create an instance of BaseModel
my_model = BaseModel()
my_model.name = "Bursary Application"
my_model.amount = 5000
print(my_model)

# Save the model to update the updated_at attribute
my_model.save()
print(my_model)

# Convert the model to a dictionary and print it
my_model_json = my_model.to_dict()
print(my_model_json)

# Print out each key and its corresponding type and value
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
