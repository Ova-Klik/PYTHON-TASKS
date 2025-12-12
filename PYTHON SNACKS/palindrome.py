

entry=input("Enter a word or digits to check for palindrome: ").lower()

reverse=""

for point in entry:
   
    reverse=point+reverse
    
if reverse==entry:
    
    print(f"{reverse} is a palindrome, ", sep=" ")
    
else:
    print(f"{entry} is not a palindrome, ", sep=" ")
""" 
entry=madam
    
reverse=""

for point in entry:
   
    reverse=point+reverse
    
if reverse==entry:
    print ("True")
   
else: 
    print("False")
"""
