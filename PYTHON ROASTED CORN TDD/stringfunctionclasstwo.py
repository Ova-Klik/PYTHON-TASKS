

def string_modifier(entry, entry_test)

length=len(entry)
    
if length<2:
    entry_test+=""
    return (entry , entry_test)
elif length==2:
    entry_test+=entry*2
    return entry , entry_test)
elif length>2:
    entry_test+=entry[0]+entry[1]+(entry[length-2])+(entry[length-1])
    return (entry , entry_test)
    
    
