
from unittest import TestCase
from palindrome_function_class import entry_is_palindrome

class TestClass(TestCase):
    
    def test_that_entry_is_palindrome(self):
                
        is_palindrome=entry_is_palindrome("madam")    
        
        self.assertTrue(is_palindrome)

    def test_that_entry_is_not_palindrome(self):
               
        is_palindrome=entry_is_palindrome("waters")
            
        self.assertFalse(is_palindrome)
      
    def test_that_integer_entry_is_palindrome(self):
        is_palindrome=entry_is_palindrome(12321)
        
        self.assertTrue(is_palindrome)
        
    def test_that_integer_entry_is_not_palindrome(self):
        is_palindrome=entry_is_palindrome(12)
        
        self.assertFalse(is_palindrome)
   
    def test_that_negative_integer_entry_is_palindrome(self):
        is_palindrome=entry_is_palindrome(-22)
        
        self.assertFalse(is_palindrome)


