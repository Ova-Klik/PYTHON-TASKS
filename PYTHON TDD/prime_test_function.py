#import unittest
from unittest import TestCase
from prime_function_class import number_is_prime

class TestClass(TestCase):
    
    def test_that_number_is_prime(self):
                
        is_prime=number_is_prime(11)    
        
        self.assertTrue(is_prime)
        
   
    def test_that_number_is_not_prime(self):
               
        is_prime=number_is_prime(20)
            
        self.assertFalse(is_prime)
        
    def test_that_negative_number_is_prime(self):
        is_prime=number_is_prime(-11)
        
        self.assertTrue(is_prime)

    def test_that_word_is_not_prime(self):
    
        
        is_prime=number_is_prime("trying")
        
        self.assertFalse(is_prime)

