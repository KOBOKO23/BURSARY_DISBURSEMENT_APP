from models import storage
from models.applicant import Applicant  # Import the customized Applicant model

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# Reload existing objects
all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new Applicant --")
my_applicant = Applicant()
my_applicant.first_name = "Betty"
my_applicant.last_name = "Bar"
my_applicant.email = "betty.bar@mail.com"
my_applicant.password = "securepassword"
my_applicant.institution = "University of Example"
my_applicant.course = "Computer Science"
my_applicant.amount_requested = 1000.0
my_applicant.save()
print(my_applicant)

print("-- Create a new Applicant 2 --")
my_applicant2 = Applicant()
my_applicant2.first_name = "John"
my_applicant2.last_name = "Doe"
my_applicant2.email = "john.doe@mail.com"
my_applicant2.password = "anotherpassword"
my_applicant2.institution = "Example Institute"
my_applicant2.course = "Data Science"
my_applicant2.amount_requested = 1500.0
my_applicant2.save()
print(my_applicant2)
