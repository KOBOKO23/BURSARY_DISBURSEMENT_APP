#!/usr/bin/python3
"""Module test_student

This Module contains unit tests for the Student Class
"""

import unittest
from models.student import Student
from models.institution import Institution

class TestStudent(unittest.TestCase):
    """Test cases for the Student class"""

    def setUp(self):
        """Set up a new instance of Student for testing."""
        self.student = Student(
            first_name="John",
            last_name="Doe",
            email="john@example.com",
            phone_number="0712345678",
            date_of_birth="2000-01-01",
            parent_income=8000,
            is_orphan=False,
            is_partial_orphan=False
        )
        self.institution = Institution(name="Siala Technical Institute", location="Kisumu", contact_info="1234567890")
        self.student.institution_id = self.institution.id

    def test_student_creation(self):
        """Test the creation of a Student."""
        self.assertEqual(self.student.first_name, "John")
        self.assertEqual(self.student.last_name, "Doe")
        self.assertEqual(self.student.email, "john@example.com")
        self.assertEqual(self.student.phone_number, "0712345678")
        self.assertEqual(self.student.parent_income, 8000)
        self.assertFalse(self.student.is_orphan)
        self.assertFalse(self.student.is_partial_orphan)

    def test_calculate_bursary_amount(self):
        """Test the bursary amount calculation."""
        self.student.calculate_bursary_amount()
        self.assertEqual(self.student.bursary_amount, 45000)

        # Test for an orphan
        self.student.is_orphan = True
        self.student.calculate_bursary_amount()
        self.assertEqual(self.student.bursary_amount, 65000)

        # Test for a partial orphan
        self.student.is_orphan = False
        self.student.is_partial_orphan = True
        self.student.calculate_bursary_amount()
        self.assertEqual(self.student.bursary_amount, 55000)

        # Test for an income higher than 24,000
        self.student.parent_income = 25000
        self.student.calculate_bursary_amount()
        self.assertEqual(self.student.bursary_amount, 0.0)

    def test_student_to_dict(self):
        """Test the to_dict method of the Student class."""
        student_dict = self.student.to_dict()
        self.assertEqual(student_dict["first_name"], "John")
        self.assertEqual(student_dict["last_name"], "Doe")
        self.assertEqual(student_dict["email"], "john@example.com")
        self.assertEqual(student_dict["phone_number"], "0712345678")
        self.assertEqual(student_dict["parent_income"], 8000)
        self.assertEqual(student_dict["is_orphan"], False)
        self.assertEqual(student_dict["is_partial_orphan"], False)
        self.assertEqual(student_dict["__class__"], "Student")

    def test_student_str(self):
        """Test the __str__ method of the Student class."""
        student_str = str(self.student)
        self.assertIn("[Student]", student_str)
        self.assertIn(self.student.id, student_str)

if __name__ == '__main__':
    unittest.main()
