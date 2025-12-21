
def string_modifier_add_ing(entry, get_string_test):
    get_string=""
    length=len(entry)
    
    if length<3:
        get_string+=entry
       
    elif length>=3 and entry.startswith("ing",length-3):
        get_string+=entry+"ly"
        else:
            get-string+=entry+"ing"
    return get_string==get_string_test

    
