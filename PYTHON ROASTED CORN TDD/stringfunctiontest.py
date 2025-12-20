from unittest import TestCase
from stringfunctionclass import length_of_string

class TestClass(TestCase):

    def test_that_length_of_string_matches(self):
        result = length_of_string("semicolon", 9)
        self.assertTrue(result)
        
    def test_that_length_of_string_does_not_match(self):
        result = length_of_string("semicolon", 7)
        self.assertFalse(result)
        
    def test_that_length_of_string_ignores_white_spaces(self):
        result = length_of_string("semi colon", 9)
        self.assertTrue(result)
        
    def test_that_length_of_string_does_not_ignore_white_spaces(self):
        result = length_of_string("semi colon", 10)
        self.assertFalse(result)

    
     
