from unittest import TestCase
from birthday_cake import*

class TestFile(TestCase):
    
    def merge_dictionary_should_merge_two_dictionaries(self):
    
        dictionary_one = {'a':1,'b':2,'c':3,'d':3}
        dictionary_two = {'c':5, 'e':6,'a':4,'d':2}
        
        merged_dictionary = {'a':1,'b':2,'c':3,'d':3,'c':5,'e':6,'a':4,'d':2}
        
        
        self.assertequal(merge_dictionary(dictionary_one,dictionary_two),merged_dictionary)
        
 
