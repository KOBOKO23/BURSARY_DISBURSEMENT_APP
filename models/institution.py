#!/usr/bin/python3
"""Module institution

This Module contains a definition for the Institution Class
"""

from models.base_model import BaseModel
from models.student import Student  # Import the Student class

class Institution(BaseModel):
    """Institution Class"""

    name = ""
    location = ""
    contact_info = ""
    students = []  # List to store associated Student instances

    def __init__(self, *args, **kwargs):
        """__init__ method & instantiation of class Institution

        Args:
            *args.
            **kwargs (dict): Key/value pairs
        """
        super().__init__(*args, **kwargs)

    def add_student(self, student):
        """Add a student to the institution."""
        if isinstance(student, Student):
            self.students.append(student)
            student.institution_id = self.id

    def __str__(self) -> str:
        """Print/str representation of the Institution instance."""
        return f"[Institution] ({self.id}) {self.__dict__}"
