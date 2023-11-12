#!/usr/python3
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        """Create an instance of BaseModel for testing"""

        self.base_model = BaseModel()

    def test_attributes(self):
        """ Test if id is a string"""

        self.assertIsInstance(self.base_model.id, str)

        """ Test if created_at and updated_at are datetime objects"""
        self.assertIsInstance(self.base_model.created_at, datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_save_method(self):
        """Save the current updated_at value"""
        original_updated_at = self.base_model.updated_at

        """Call the save method"""
        self.base_model.save()

        """Check if updated_at has been updated after calling save"""
        self.assertNotEqual(original_updated_at, self.base_model.updated_at)

    def test_to_dict_method(self):
        """Call to_dict method"""
        model_dict = self.base_model.to_dict()

        """Check if keys are present in the dictionary"""
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)
        self.assertIn('__class__', model_dict)

        """Check if values are of the correct type"""
        self.assertIsInstance(model_dict['id'], str)
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)
        self.assertIsInstance(model_dict['__class__'], str)

        """Check if the values match the instance attributes"""
        self.assertEqual(model_dict['id'], self.base_model.id)
        self.assertEqual(
            model_dict['created_at'],
            self.base_model.created_at.isoformat()
            )
        self.assertEqual(
            model_dict['updated_at'],
            self.base_model.updated_at.isoformat()
            )
        self.assertEqual(model_dict['__class__'], 'BaseModel')

    def test_str_method(self):
        """Call str method"""
        model_str = str(self.base_model)

        """Check if the string contains the class name and id"""
        self.assertIn('BaseModel', model_str)
        self.assertIn(self.base_model.id, model_str)


if __name__ == '__main__':
    unittest.main()
