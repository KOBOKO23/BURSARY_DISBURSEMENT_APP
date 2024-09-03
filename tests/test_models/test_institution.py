#!/usr/bin/python3
"""Module test_institution

This Module contains unit tests for the Institution Class
"""

import unittest
from models.institution import Institution
from models.student import Student

class TestInstitution(unittest.TestCase):
    """Test cases for the Institution class"""

    def setUp(self):
        """Set up a new instance of Institution for testing."""
        self.institution = Institution(name="Siala Technical Institute", location="Kisumu", contact_info="1234567890")
        self.student = Student(first_name="Betty", last_name="Bar", email="betty@example.com", phone_number="0725031720")

    def test_institution_creation(self):
        """Test the creation of an Institution."""
        self.assertEqual(self.institution.name, "Siala Technical Institute")
        self.assertEqual(self.institution.location, "Kisumu")
        self.assertEqual(self.institution.contact_info, "1234567890")

    def test_add_student(self):
        """Test adding a student to the institution."""
        self.institution.add_student(self.student)
        self.assertIn(self.student, self.institution.students)
        self.assertEqual(self.student.institution_id, self.institution.id)

    def test_institution_to_dict(self):
        """Test the to_dict method of the Institution class."""
        inst_dict = self.institution.to_dict()
        self.assertEqual(inst_dict["name"], "Siala Technical Institute")
        self.assertEqual(inst_dict["location"], "Kisumu")
        self.assertEqual(inst_dict["contact_info"], "1234567890")
        self.assertEqual(inst_dict["__class__"], "Institution")

    def test_institution_str(self):
        """Test the __str__ method of the Institution class."""
        inst_str = str(self.institution)
        self.assertIn("[Institution]", inst_str)
        self.assertIn(self.institution.id, inst_str)

if __name__ == '__main__':
    unittest.main()
