count = 0

total = 0
while (count != 1):
    number = int(input("Enter a number: "))
    
    if number > 0:
        if number % 2 == 0:
            divided = number / 2
            total +=1
        else:
            divided = number / 3 + 1
            total +=1
            
    if divided == 1:
        break
        
print(divided)
print(f"The total count: {total}")
