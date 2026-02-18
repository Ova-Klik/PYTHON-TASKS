

def string_modifier(entry, get_string_test):
    get_string=""
    length=len(entry)
    
    if length<2:
        get_string=""
       
    elif length==2:
        get_string+=entry*2
        
    elif length>2:
        get_string+=entry[0]+entry[1]+(entry[length-2])+(entry[length-1])
    
    return get_string==get_string_test


    
