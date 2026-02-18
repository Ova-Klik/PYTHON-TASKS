
from unittest import TestCase
from BackToSenderFunctionFile import get_payment

class TestClass(TestCase):
    
    def test_that_wage_is_accurate_for_less_than_50(self):
                
        wage_is_equal=get_payment(25, 9000)    
        
        self.assertTrue(wage_is_equal)
    
    def test_that_wage_is_not_accurate_for_less_than_50(self):
                
        wage_is_equal=get_payment(25, 50000)    
        
        self.assertFalse(wage_is_equal)
        
    def test_that_wage_is_accurate_for_50_to_59(self):
                
        wage_is_equal=get_payment(50, 15000)    
        
        self.assertTrue(wage_is_equal)
        
    def test_that_wage_is_not_accurate_for_50_to_59(self):
                
        wage_is_equal=get_payment(50, 9000)    
        
        self.assertFalse(wage_is_equal)    
        
    def test_that_wage_is_accurate_for_60_to_69(self):
                
        wage_is_equal=get_payment(60, 20000)    
        
        self.assertTrue(wage_is_equal)
        
    def test_that_wage_is_not_accurate_for_60_to_69(self):
                
        wage_is_equal=get_payment(60, 15000)    
        
        self.assertFalse(wage_is_equal)   
        
    def test_that_wage_is_accurate_for_70_to_100(self):
                
        wage_is_equal=get_payment(80, 40000)    
        
        self.assertFalse(wage_is_equal) 
        
   
   

