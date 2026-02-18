

def mutiple_of_10(number):
    sum=0;

    for number in range(0, 20000):
        
        if number%10==0: 
            sum+=number
        
    return(sum)   

def mutiple_of_3(number):

    for number in range(1, 15):
        
        if number%3==0:  
            print(number)
            
def even_number(number):
            
    for number in range(1, 100):
        
        if number%2==0:  
            print(number)
            
            
    studentfail=0;
    studentpass=0; 
   
def student_score(number):

    for number in range(0,15):
       
        score=int(input("Kindly enter score: "))
        if score<45:
            studentfail+=1;
        
        else:
        
            studentpass+=1;
            
    return(f"{studentpass} passed")
    return(f"{studentfail} failed")


def mutiplication_table(number):

    number=int(input("Kindly enter a number to get the multiplication table: "))


    for a in range(1,11):

        result= number*a
        print(f"{number} x {a}= {result}")
        
    
def star(number):

    number=int(input("Kindly enter a number to get star: "))


    for a in range(1,number+1):
        
        result= '*'* a
        print(f"{result}")
    
