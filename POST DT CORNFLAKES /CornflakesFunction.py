


def mutiple_of_10(number):
    sum=0;

    for number in range(0, 20001,10):
        
            sum+=number
        
    print (sum)    

def mutiple_of_3(number):

    for number in range(1,16):
    
    if number%3==0:  
        print(number)
            
def even_number(number):
            
    for number in range(1,101):
    
        if number%2==0:  
            print (number, end=" ")
        
            
   
def student_score():
          
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


def mutiplication_table(number):

    number=int(input("Kindly enter a number to get the multiplication table: "))

    for a in range(10):

        result= number*a
        print(f"{number} x {a}= {result}")
        
        
    
def star(number):

    number=int(input("Kindly enter a number to get star: "))

    for a in range(number):
        
        result= '*'* a
        print(f"{result}")
        
def number_triangle(number):

    number=int(input("Kindly enter a number to get a triangle factorial: "))


    for a in range(number,0, -1):
        
        for b in range(a,0,-1):
        
            print(b,end=" ")
        
        print()
        


    
