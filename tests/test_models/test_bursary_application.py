#!/usr/bin/python3
"""Unittest for BursaryApplication Class"""

import unittest
from models.bursary_application import BursaryApplication

class TestBursaryApplication(unittest.TestCase):
    """Test cases for the BursaryApplication class."""

    def setUp(self):
        """Set up a test instance of BursaryApplication before each test."""
        self.bursary_app = BursaryApplication(
            student_first_name="John",
            student_last_name="Doe",
            birth_certificate_number="123456",
            institution_id="INST001",
            index_number="001",
            course_period=3,
            county="Nairobi",
            constituency="Westlands",
            location="Kangemi",
            sub_location="Kangemi",
            village="Nyumbani"
        )

    def tearDown(self):
        """Clean up after each test."""
        del self.bursary_app

    def test_bursary_application_creation(self):
        """Test creation of BursaryApplication."""
        data = {
            "student_first_name": "John",
            "student_last_name": "Doe",
            "birth_certificate_number": "123456",
            "institution_id": "INST001",
            "index_number": "001",
            "course_period": 3,
            "county": "Nairobi",
            "constituency": "Westlands",
            "location": "Kangemi",
            "sub_location": "Kangemi",
            "village": "Nyumbani"
        }
        for key, value in data.items():
            self.assertEqual(getattr(self.bursary_app, key), value)

    def test_validate_birth_certificate(self):
        """Test validation of birth_certificate_number."""
        self.assertEqual(self.bursary_app.birth_certificate_number, "123456")

    def test_validate_birth_certificate_invalid(self):
        """Test validation of missing birth_certificate_number."""
        data = {
            "student_first_name": "John",
            "student_last_name": "Doe"
            # Missing birth_certificate_number here
        }
        with self.assertRaises(ValueError):
            BursaryApplication(**data)

    def test_validate_course_period(self):
        """Test course_period validation."""
        self.assertEqual(self.bursary_app.course_period, 3)

    def test_validate_course_period_invalid(self):
        """Test invalid course period (should raise ValueError)."""
        with self.assertRaises(ValueError):
            BursaryApplication(course_period=4)

    def test_str_representation(self):
        """Test the string representation of BursaryApplication."""
        bursary_app_str = str(self.bursary_app)
        self.assertIn("[BursaryApplication]", bursary_app_str)
        self.assertIn(self.bursary_app.id, bursary_app_str)

if __name__ == "__main__":
    unittest.main()
