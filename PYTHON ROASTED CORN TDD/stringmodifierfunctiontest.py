from unittest import TestCase
from stringmodifierclass import string_modifier

class TestClass(TestCase):

    def test_empty_string_when_entry_less_than_two(self):
        result = string_modifier("o", "")
        self.assertTrue(result)
    def test_empty_string_when_entry_not_less_than_two(self):
        result = string_modifier("o", "o")
        self.assertFalse(result)
    def test_double_of_entry_when_entry_equals_two(self):
        result = string_modifier("on", "onon")
        self.assertTrue(result)
    def test_not_double_of_entry_when_entry_equals_two(self):
        result = string_modifier("on", "on")
        self.assertFalse(result)
    def test_front_and_back_position_string_slice_when_entry_greater_than_two(self):
        result = string_modifier("semicolon", "seon")
        self.assertTrue(result)
    def test_not_front_and_back_position_string_sliced_when_entry_greater_than_two(self):
        result = string_modifier("semicolon", "son")
        self.assertFalse(result)
 
