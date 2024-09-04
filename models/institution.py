#!/usr/bin/python3
"""Module institution

This Module contains a definition for the Institution Class
"""

from models.base_model import BaseModel

class Institution(BaseModel):
    """Institution Class"""

    name = ""
    location = ""
    contact_info = ""
    students = []  # List to store associated Student instances
    bursary_applications = []  # List to store associated BursaryApplication instances

    def __init__(self, *args, **kwargs):
        """__init__ method & instantiation of class Institution

        Args:
            *args.
            **kwargs (dict): Key/value pairs
        """
        super().__init__(*args, **kwargs)

    def add_student(self, student):
        """Add a student to the institution."""
        from models.student import Student  # Import inside method to avoid circular import
        if isinstance(student, Student):
            self.students.append(student)
            student.institution_id = self.id

    def add_bursary_application(self, bursary_application):
        """Add a bursary application to the institution."""
        from models.bursary_application import BursaryApplication  # Import inside method to avoid circular import
        if isinstance(bursary_application, BursaryApplication):
            self.bursary_applications.append(bursary_application)
            bursary_application.institution_id = self.id

    def __str__(self) -> str:
        """Print/str representation of the Institution instance."""
        return f"[Institution] ({self.id}) {self.__dict__}"
