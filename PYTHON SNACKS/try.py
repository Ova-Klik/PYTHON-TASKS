
#count=1
#number=0
#while (True):
    #if number ==1 or number==2:
     #  print("finally ") 
        
    #   break
      
    
   # else: 
  #      number=int(input("Try entering number 1 or 2 please: "))
 #       count=count +1
      
import random
count =1      
for roll in range(0o101):
    while (count <1000):
        print(random.randrange(1,7), end=" ")
        count+=1
    
