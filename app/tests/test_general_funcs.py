import unittest
from datetime import datetime, date
from app.general_functions import *

class TestGeneralFuncs(unittest.TestCase):
    def test_generate_random_string(self):
        """Tests the generate_random_string function
        with different input types and values
        """
        # Testing when a positive integer is passed
        self.assertEqual(len(generate_random_string(10)), 10)
        # Tesing when 0 is passed as the argument
        self.assertEqual(len(generate_random_string(0)), 0)
        # Testing if a string passed will be converted to an int
        self.assertEqual(len(generate_random_string("10")), 10)
        # Testing when a negative integer is passed
        self.assertEqual(len(generate_random_string(-10)), 0)
        # Testing when a float is passed
        self.assertEqual(len(generate_random_string(10.5)), 10)

    def test_timestamp_to_standard_format(self):
        """
        Tests the test_timestamp_to_standard_format
        with different input types and values. The function
        is supposed to return a DD/MM %H:%Mdate format from a 
        timestamp
        """
        # Testing for the correct output
        self.assertEqual(
            timestamp_to_standard_format("2020-10-10 10:10:10"), 
            "10/10 10:10"
            )
        # Testing when a datetime object instead of a string is passed
        self.assertRaises(
            TypeError, timestamp_to_standard_format, 
            datetime(2024, 2, 16, 11, 48, 57, 93829)
            )
        # Testing the type of the returned value. [Expecting a string]
        self.assertIsInstance(
            timestamp_to_standard_format("2020-10-10 10:10:10"),
            str
            )

    def test_stringify_datetime_object(self):
        """
        Tests the stringify_datetime_object function
        with different input types and values. The function
        is expected to return a datetime string from a datetime object
        """
        # Testing for the correct output
        self.assertEqual(
            stringify_datetime_object(datetime(2024, 2, 16, 11, 48, 57, 93829)),
            "2024-02-16 11:48:57"
            )
        # Testing when a date object instead of a datetime object is passed
        self.assertEqual(
            stringify_datetime_object(date(2024, 2, 16)), 
            "2024-02-16 00:00:00"
            )
        # Testing when a string instead of a datetime object is passed
        self.assertRaises(
            AttributeError, 
            stringify_datetime_object, 
            "2024-02-16 11:48:57"
            )
        # Testing the type of the returned value. [Expecting a string]
        self.assertIsInstance(
            stringify_datetime_object(datetime(2024, 2, 16, 11, 48, 57, 93829)),
            str
            )

    def test_create_timestamp(self):
        """
        Tests the create_timestamp function
        with different input types and values. The function
        is expected to return a datetime string
        """
        # Testing the type of the returned value. [Expecting a string]
        self.assertIsInstance(create_timestamp(), str)

    def test_get_uuid(self):
        """
        Tests the get_uuid function. The function
        is expected to return uuid4 string
        """
        # Testing the type of the returned value. [Expecting a string]
        self.assertIsInstance(get_uuid(), str)
        # Testing the length of the returned value. [Expecting 36]
        self.assertEqual(len(get_uuid()), 36)

    def test_id_generator(self):
        """
        Tests the id_generator function. The function
        is expected to return a random alphanumeric string of length 6
        and of type string.
        """
        # Testing the length of the returned value. [Expecting 6]
        self.assertEqual(len(id_generator()), 6)
        # Testing the type of the returned value. [Expecting a string]
        self.assertIsInstance(id_generator(), str)

    def test_is_date_object(self):
        """
        Tests the is_date_object function. The function
        is expected to check if the input is a date object
        or not. It returns a boolean value.
        """
        # Testing when an int is passed as the arg. [Expecting False] 
        self.assertEqual(is_date_object(7), False)
        # Testing when an date object is passed as the arg. [Expecting True] 
        self.assertEqual(is_date_object(date(2024, 2, 16)), True)
        # Testing when an datetime object is passed as the arg. [Expecting True]
        self.assertEqual(
            is_date_object(datetime(2024, 2, 16, 11, 48, 57, 93829)),
            True
            )

    def test_datetime_object(self):
        """
        Tests the datetime_object function. The function
        is expected to check if the input is a datetime object
        or not. It returns a boolean value.
        """
        # Testing when an int is passed as the arg. [Expecting False] 
        self.assertEqual(is_datetime_object(7), False)
        # Testing when an datetime object is passed as the arg. [Expecting True]
        self.assertEqual(
            is_datetime_object(datetime(2024, 2, 16, 11, 48, 57, 93829)),
            True
            )
        # Testing when an date object is passed as the arg. [Expecting False] 
        self.assertEqual(
            is_datetime_object(date(2024, 2, 16)), 
            False
            )

    def test_datetime_to_standard_date(self):
        """
        Tests the datetime_to_standard_date function. The function
        is expected to change a datetime object to a date string
        """
        # Testing for the correct output
        self.assertEqual(
            datetime_to_standard_date(datetime(2024, 2, 16, 11, 48, 57, 93829)),
            "2024-02-16"
            )
        # Testing when a string instead of a datetime object is passed
        self.assertRaises(
            AttributeError, 
            datetime_to_standard_date, 
            "2024-02-16 11:48:57"
            )
        # Testing the type of the returned value. [Expecting a string]
        self.assertIsInstance(
            datetime_to_standard_date(datetime(2024, 2, 16, 11, 48, 57, 93829)),
            str)