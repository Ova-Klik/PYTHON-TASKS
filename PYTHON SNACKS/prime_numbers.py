number=int(input("Enter number: "))

if number<0:
    number*=-1

if number<=2 and number>0: 

    print("prime number")

else:
    if number%2==0 or number%3==0 or number%5==0:

        print ("not a prime number")
      
    else: 
        print("prime number")

