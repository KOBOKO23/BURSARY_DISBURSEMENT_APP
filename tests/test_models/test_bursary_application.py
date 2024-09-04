#!/usr/bin/python3
import unittest
from models.bursary_application import BursaryApplication
from models.student import Student
from models.institution import Institution

class TestBursaryApplication(unittest.TestCase):
    """Test cases for BursaryApplication class."""

    def setUp(self):
        """Set up test environment."""
        self.institution = Institution(name="Test Institution", location="Test Location", contact_info="Test Contact")
        self.student = Student(first_name="John", last_name="Doe", email="john.doe@example.com", phone_number="123456789", date_of_birth="2000-01-01", parent_income=5000, is_orphan=False, is_partial_orphan=False)
        self.bursary_application = BursaryApplication(
            parent_name_mother="Jane Doe",
            parent_name_father="John Doe",
            parent_alive_mother=True,
            parent_alive_father=True,
            death_certificate="",
            parent_occupation_mother="Teacher",
            parent_occupation_father="Engineer",
            parent_income_mother=25000,
            parent_income_father=30000,
            student_first_name="John",
            student_last_name="Doe",
            birth_certificate_number="123456789",
            institution_id=self.institution.id,
            index_number="123456",
            course_period=3,
            county="Test County",
            constituency="Test Constituency",
            location="Test Location",
            sub_location="Test Sub-location",
            village="Test Village"
        )

    def test_bursary_application_initialization(self):
        """Test initialization of BursaryApplication instance."""
        self.assertEqual(self.bursary_application.parent_name_mother, "Jane Doe")
        self.assertEqual(self.bursary_application.parent_name_father, "John Doe")
        self.assertTrue(self.bursary_application.parent_alive_mother)
        self.assertTrue(self.bursary_application.parent_alive_father)
        self.assertEqual(self.bursary_application.death_certificate, "")
        self.assertEqual(self.bursary_application.parent_occupation_mother, "Teacher")
        self.assertEqual(self.bursary_application.parent_occupation_father, "Engineer")
        self.assertEqual(self.bursary_application.parent_income_mother, 25000)
        self.assertEqual(self.bursary_application.parent_income_father, 30000)
        self.assertEqual(self.bursary_application.student_first_name, "John")
        self.assertEqual(self.bursary_application.student_last_name, "Doe")
        self.assertEqual(self.bursary_application.birth_certificate_number, "123456789")
        self.assertEqual(self.bursary_application.institution_id, self.institution.id)
        self.assertEqual(self.bursary_application.index_number, "123456")
        self.assertEqual(self.bursary_application.course_period, 3)
        self.assertEqual(self.bursary_application.county, "Test County")
        self.assertEqual(self.bursary_application.constituency, "Test Constituency")
        self.assertEqual(self.bursary_application.location, "Test Location")
        self.assertEqual(self.bursary_application.sub_location, "Test Sub-location")
        self.assertEqual(self.bursary_application.village, "Test Village")

if __name__ == '__main__':
    unittest.main()
