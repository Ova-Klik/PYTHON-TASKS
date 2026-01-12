entry=input("enter string: ")
entry_test=""
length=len(entry)
    
if length<2:
    entry_test+=""
    print(entry , entry_test)
elif length==2:
    entry_test+=entry*2
    print(entry , entry_test)
elif length>2:
    entry_test+=entry[0]+entry[1]+(entry[length-2])+(entry[length-1])
    print(entry , entry_test)
    
    
