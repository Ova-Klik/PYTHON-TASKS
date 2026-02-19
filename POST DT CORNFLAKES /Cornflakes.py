


sum=0;


for number in range(0, 20001,10):
  
        sum+=number
    
print (sum)   


for number in range(1,16):
    
    if number%3==0:  
        print(number)
        
for number in range(1,101):
    
    if number%2==0:  
        print (number, end=" ")
        
        
studentfail=0;
studentpass=0; 
   
for number in range(0,15):
   
    score=int(input("Kindly enter score: "))
    if score<45:
        studentfail+=1;
        print (f"FAILED")
    
    else:
    
        studentpass+=1;
        print (f"PASSED")
        
print (f"{studentpass} passed")
print (f"{studentfail} failed")



number=int(input("Kindly enter a number to get the multiplication table: "))


for a in range(10):

    result= number*a
    print(f"{number} x {a}= {result}")
    
    
number=int(input("Kindly enter a number to get star: "))


for a in range(1, number+1):
    
    result= '*'* a
    print(f"{result}")
    
    
    
number=int(input("Kindly enter a number to get a triangle factorial: "))


for digits in range(number, 0, -1):
    
    for digit in range(digits, 0, -1):
    
        print(digit, end=" ")
        
    print()
    
    
number=int(input("Kindly enter a number to get a triangle factorial: "))


for digits in range(number, 0, -1):
    
    for digit in range(digits, 0, -1):
    
        print(f"*",end=" ")
 
        
    print()




    
    


