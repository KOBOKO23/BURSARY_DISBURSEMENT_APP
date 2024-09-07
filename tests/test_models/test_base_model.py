#!/usr/bin/python3
import unittest
import os
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class"""

    def setUp(self):
        """Set up the test environment"""
        self.model = BaseModel()
        self.model.name = "Test Model"
        self.model.my_number = 100

    def test_save(self):
        """Test save method"""
        self.model.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_to_dict(self):
        """Test to_dict method"""
        model_dict = self.model.to_dict()
        self.assertEqual(type(model_dict), dict)
        self.assertIn("__class__", model_dict)
        self.assertEqual(model_dict["__class__"], "BaseModel")

    def test_str(self):
        """Test __str__ method"""
        model_str = str(self.model)
        self.assertIn("[BaseModel]", model_str)
        self.assertIn(f"({self.model.id})", model_str)

    def tearDown(self):
        """Clean up after tests"""
        if os.path.exists("file.json"):
            try:
                os.remove("file.json")
            except Exception as e:
                print(f"Failed to delete file.json: {e}")

if __name__ == "__main__":
    unittest.main()
