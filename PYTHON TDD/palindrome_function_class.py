
def entry_is_palindrome(entry):
  
    reverse=""
    
    entry=str(entry)
    
    for point in entry:
   
        reverse=point+reverse
    
    if reverse==entry:
    
        return True
    
    else:
        return False
    
    

    
