
#Write a program to print the first 15 multiples of 3 in a straight line. 
#Write a program that print even numbers between 1-100





sum=0;


for number in range(20000):
    
    if number%10==0: 
        sum+=number
    
print (sum)   


for number in range(15):
    
    if number%3==0:  
        print(number)
        
for number in range(100):
    
    if number%2==0:  
        print (number)
        
        
studentfail=0;
studentpass=0; 
   
for number in range(0,15):
   
    score=int(input("Kindly enter score: "))
    if score<45:
        studentfail+=1;
    
    else:
    
        studentpass+=1;
        
print (f"{studentpass} passed")
print (f"{studentfail} failed")



number=int(input("Kindly enter a number to get the multiplication table: "))


for a in range(10):

    result= number*a
    print(f"{number} x {a}= {result}")
    
    
number=int(input("Kindly enter a number to get star: "))


for a in range(number):
    
    result= '*'* a
    print(f"{result}")
    
    
    
number=int(input("Kindly enter a number to get a triangle factorial: "))


for a in range(5,0, -1):
    
    for b in range(a,0,-1):
    
        print(b,end=" ")
    
    print()
    
    



    
    


