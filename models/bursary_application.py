#!/usr/bin/python3
"""Module bursary_application

This Module contains a definition for the BursaryApplication Class.
"""

from models.base_model import BaseModel

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
        # Call super to handle base class initialization
        super().__init__(*args, **kwargs)
        
        # Apply kwargs to instance
        for key, value in kwargs.items():
            setattr(self, key, value)
        
        # Validate fields after instantiation
        self.validate_fields()

    def validate_fields(self):
        """Validate fields during instantiation."""
        self.validate_course_period()
        self.validate_birth_certificate()

    def validate_course_period(self):
        """Ensure that course_period is less than 4 years."""
        if self.course_period >= 4:
            raise ValueError("Course period must be less than 4 years.")

    def validate_birth_certificate(self):
        """Ensure birth certificate number is provided during new submissions."""
        if not self.birth_certificate_number:
            raise ValueError("Birth certificate number is required.")

    def set_student(self, student):
        """Set the student for this application."""
        from models.student import Student  # Import inside method to avoid circular import
        if isinstance(student, Student):
            self.student = student

    def set_institution(self, institution):
        """Set the institution for this application."""
        from models.institution import Institution  # Import inside method to avoid circular import
        if isinstance(institution, Institution):
            self.institution = institution

    def __str__(self) -> str:
        """Print/str representation of the BursaryApplication instance."""
        return f"[BursaryApplication] ({self.id}) {self.__dict__}"
