#import unittest
from unittest import TestCase
from palindrome_function_class import entry_is_palindrome

class TestClass(TestCase):
    
    def test_that_entry_is_palindrome(self):
                
        is_palindrome=entry_is_palindrome("madam")    
        
        self.assertTrue(is_palindrome)

    def test_that_entry_is_not_palindrome(self):
               
        is_palindrome=entry_is_palindrome("water")
            
        self.assertFalse(is_palindrome)
      
    def test_that_integer_entry_is_palindrome(self):
        is_palindrome=entry_is_palindrome(11)
        
        self.assertTrue(is_palindrome)
        
    def test_that_integer_entry_is_not_palindrome(self):
        is_palindrome=entry_is_palindrome(24)
        
        self.assertFalse(is_palindrome)
   
    def test_that_negative_integer_entry_is_palindrome(self):
        is_palindrome=entry_is_palindrome(-22)
        
        self.assertFalse(is_palindrome)


