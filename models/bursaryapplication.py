#!/usr/bin/python3
"""Module bursary_application

This module contains a definition for the BursaryApplication Class.
"""

from models.base_model import BaseModel  # Ensure this import is correct

class BursaryApplication(BaseModel):
    """BursaryApplication Class"""

    # Attributes related to parents
    parent_name_mother = ""
    parent_name_father = ""
    parent_alive_mother = True
    parent_alive_father = True
    death_certificate = ""  # File path for death certificate if any parent is deceased
    parent_occupation_mother = ""
    parent_occupation_father = ""
    parent_income_mother = 0.0
    parent_income_father = 0.0

    # Student's profile
    student_first_name = ""
    student_last_name = ""
    birth_certificate_number = ""  # Mandatory field
    institution_id = ""  # Linked to Institution
    index_number = ""
    course_period = 0  # Number of years

    # Geographical location
    county = ""
    constituency = ""
    location = ""
    sub_location = ""
    village = ""

    def __init__(self, *args, **kwargs):
        """__init__ method & instantiation of class BursaryApplication."""
        super().__init__(*args, **kwargs)
        print(f"Initializing BursaryApplication with args: {args} kwargs: {kwargs}")

        if '__class__' in kwargs:
            del kwargs['__class__']

        for key, value in kwargs.items():
            setattr(self, key, value)
        
        self.validate_fields()
        self.save()  # Ensure the instance is saved after initialization
        print(f"BursaryApplication instance saved: {self.id}")

    def validate_fields(self):
        """Validate fields during instantiation."""
        self.validate_course_period()
        self.validate_birth_certificate()

    def validate_course_period(self):
        """Ensure that course_period is less or equal to 4 years."""
        if not isinstance(self.course_period, int):
            raise TypeError("Course period must be an integer.")
        if self.course_period <= 0:
            raise ValueError("Course period must be greater than 0.")
        if self.course_period > 4:
            raise ValueError("Course period must be less or equal to 4 years.")

    def validate_birth_certificate(self):
        """Ensure birth certificate number is provided during new submissions."""
        if not self.birth_certificate_number:
            raise ValueError("Birth certificate number is required.")

    def __str__(self) -> str:
        """Print/str representation of the BursaryApplication instance."""
        return f"[BursaryApplication] ({self.id}) {self.__dict__}"

    def to_dict(self):
        """Override to_dict method to include custom attributes."""
        base_dict = super().to_dict()
        custom_fields = {
            'parent_name_mother': self.parent_name_mother,
            'parent_name_father': self.parent_name_father,
            'parent_alive_mother': self.parent_alive_mother,
            'parent_alive_father': self.parent_alive_father,
            'parent_income_mother': self.parent_income_mother,
            'parent_income_father': self.parent_income_father,
            'student_first_name': self.student_first_name,
            'student_last_name': self.student_last_name,
            'birth_certificate_number': self.birth_certificate_number,
            'institution_id': self.institution_id,
            'index_number': self.index_number,
            'course_period': self.course_period,
            'county': self.county,
            'constituency': self.constituency,
            'location': self.location,
            'sub_location': self.sub_location,
            'village': self.village,
        }
        base_dict.update(custom_fields)
        return base_dict
