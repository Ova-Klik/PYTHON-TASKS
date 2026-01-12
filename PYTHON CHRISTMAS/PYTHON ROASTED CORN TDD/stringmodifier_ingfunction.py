
def string_modifier_add_ing(entry, get_string_test):
    get_string=""
    length=len(entry)
    
    if length<3:
        get_string+=entry
       
    elif length>=3:
        if entry.endswith("ing"):
            get_string+=entry+"ly"
        else:
            get_string+=entry+"ing"
    
    return get_string==get_string_test

    
