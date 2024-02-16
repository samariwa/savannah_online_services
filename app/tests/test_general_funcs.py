import unittest
from datetime import datetime, date
from app.general_functions import *

class TestGeneralFuncs(unittest.TestCase):
    def test_generate_random_string(self):
        self.assertEqual(len(generate_random_string(10)), 10)
        self.assertEqual(len(generate_random_string(0)), 0)
        self.assertEqual(len(generate_random_string("10")), 10)
        self.assertEqual(len(generate_random_string(-10)), 0)
        self.assertEqual(len(generate_random_string(10.5)), 10)

    def test_timestamp_to_standard_format(self):
        self.assertEqual(
            timestamp_to_standard_format("2020-10-10 10:10:10"), 
            "10/10 10:10"
            )
        self.assertRaises(
            TypeError, timestamp_to_standard_format, 
            datetime(2024, 2, 16, 11, 48, 57, 93829)
            )
        self.assertIsInstance(
            timestamp_to_standard_format("2020-10-10 10:10:10"),
            str
            )

    def test_stringify_datetime_object(self):
        self.assertEqual(
            stringify_datetime_object(datetime(2024, 2, 16, 11, 48, 57, 93829)),
            "2024-02-16 11:48:57"
            )
        self.assertEqual(
            stringify_datetime_object(date(2024, 2, 16)), 
            "2024-02-16 00:00:00"
            )
        self.assertRaises(
            AttributeError, 
            stringify_datetime_object, 
            "2024-02-16 11:48:57"
            )
        self.assertIsInstance(
            stringify_datetime_object(datetime(2024, 2, 16, 11, 48, 57, 93829)),
            str
            )

    def test_create_timestamp(self):
        self.assertIsInstance(create_timestamp(), str)

    def test_get_uuid(self):
        self.assertIsInstance(get_uuid(), str)
        self.assertEqual(len(get_uuid()), 36)

    def test_id_generator(self):
        self.assertEqual(len(id_generator()), 6)
        self.assertIsInstance(id_generator(), str)

    def test_date_object(self):
        self.assertEqual(is_date_object(7), False)
        self.assertEqual(is_date_object(date(2024, 2, 16)), True)
        self.assertEqual(
            is_date_object(datetime(2024, 2, 16, 11, 48, 57, 93829)),
            True
            )

    def test_datetime_object(self):
        self.assertEqual(
            is_datetime_object(7), 
            False
            )
        self.assertEqual(
            is_datetime_object(datetime(2024, 2, 16, 11, 48, 57, 93829)),
            True
            )
        self.assertEqual(
            is_datetime_object(date(2024, 2, 16)), 
            False
            )

    def test_datetime_to_standard_date(self):
        self.assertEqual(
            datetime_to_standard_date(datetime(2024, 2, 16, 11, 48, 57, 93829)),
            "2024-02-16"
            )
        self.assertRaises(
            AttributeError, 
            datetime_to_standard_date, 
            "2024-02-16 11:48:57"
            )
        self.assertIsInstance(
            datetime_to_standard_date(datetime(2024, 2, 16, 11, 48, 57, 93829)),
            str)