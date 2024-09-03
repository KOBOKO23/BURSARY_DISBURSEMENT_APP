#!/usr/bin/python3
"""Module student

This Module contains a definition for the Student Class
"""

from models.base_model import BaseModel

class Student(BaseModel):
    """Student Class"""

    first_name = ""
    last_name = ""
    email = ""
    phone_number = ""
    date_of_birth = ""
    parent_income = 0.0
    is_orphan = False
    is_partial_orphan = False
    institution_id = ""
    bursary_amount = 0.0

    def __init__(self, *args, **kwargs):
        """__init__ method & instantiation of class Student

        Args:
            *args.
            **kwargs (dict): Key/value pairs
        """
        super().__init__(*args, **kwargs)
        self.calculate_bursary_amount()

    def calculate_bursary_amount(self):
        """Calculate the bursary amount based on parent's income and orphan status."""
        if self.is_orphan:
            self.bursary_amount = 65000
        elif self.is_partial_orphan:
            if self.parent_income <= 6000:
                self.bursary_amount = 50000 + 10000
            elif self.parent_income <= 12000:
                self.bursary_amount = 45000 + 10000
            elif self.parent_income <= 18000:
                self.bursary_amount = 40000 + 10000
            elif self.parent_income <= 24000:
                self.bursary_amount = 30000 + 10000
            else:
                self.bursary_amount = 0.0  # No bursary if income is above 24,000
        else:
            if self.parent_income <= 6000:
                self.bursary_amount = 50000
            elif self.parent_income <= 12000:
                self.bursary_amount = 45000
            elif self.parent_income <= 18000:
                self.bursary_amount = 40000
            elif self.parent_income <= 24000:
                self.bursary_amount = 30000
            else:
                self.bursary_amount = 0.0  # No bursary if income is above 24,000

    def __str__(self) -> str:
        """Print/str representation of the Student instance."""
        return f"[Student] ({self.id}) {self.__dict__}"
