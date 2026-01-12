import re

def length_of_string(string_entry, test_length):

    string_entry=re.sub(r"\s+","",string_entry)    
    string_length = len(string_entry)
    return string_length == test_length
    
    
    

