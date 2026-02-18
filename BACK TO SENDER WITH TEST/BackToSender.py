import re

delivery_format=re.compile(r"^(100|[1-9]?[0-9])$")

def get_payment (successful_Delivery):
   
    BASE_PAY=5000
    payment =0;
    
 
    if successful_Delivery < 50:
       amount_per_parcel= 160
    
       payment = successful_Delivery * amount_per_parcel + BASE_PAY
       return payment
    
    elif successful_Delivery>=50 and successful_Delivery<=59:
        amount_per_parcel= 200
        
        payment = successful_Delivery * amount_per_parcel + BASE_PAY
        return payment
    elif (successful_Delivery>=60 and successful_Delivery<=69):
        amount_per_parcel= 250
    
        payment = successful_Delivery * amount_per_parcel + BASE_PAY;
        return payment
    elif (successful_Delivery >=70):
        amount_per_parcel= 500
    
        payment = successful_Delivery * amount_per_parcel + BASE_PAY;
        return payment





payment_Board="""
                                    WELCOME TO DELIVERY PAYMENT BOARD 
                            ___________________________________________________
                            |                 |                   |           |
                            | Collection Rate | Amount Per Parcel | Base Pay  |
                            ---------------------------------------------------      
                            | Less than 50%   |       160         |     5000  |    
                            ---------------------------------------------------      
                            | 50 - 59%        |       200         |     5000  |   
                            ---------------------------------------------------      
                            | 60 - 69%        |       250         |     5000  |   
                            ---------------------------------------------------      
                            | >=70%           |       500         |     5000  | 
                            |_________________________________________________|  
                            
                            
                            
                            
             """
             
print(payment_Board)
run="start"


while run=="start":
    number = input("Kindly enter number of successful deliveries (0-100): ")
        
    if not delivery_format.fullmatch(number):
        print("Invalid input!")
        continue
        
    else:
        number_of_delivery= int(number)
           
    wages= get_payment(number_of_delivery)
    
    print(f"Your wage for Today is:${wages:,}")
   
    while run=="start":
        print()
        more  = input("Will you like to calculate next Wage (yes/no): ").casefold();
    
        if (more=="yes"):
            break
        elif (more=="no"):
            run="stop"
            break        
        else:
            print("\n\tInvalid input!")
            continue
     





