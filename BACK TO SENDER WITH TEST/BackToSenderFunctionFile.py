
def get_payment (successful_Delivery , test_wages):

    BASE_PAY=5000
    payment =0;

 
    if successful_Delivery < 50:
       amount_per_parcel= 160
    
       payment = successful_Delivery * amount_per_parcel + BASE_PAY
       return payment==test_wages
    
    elif successful_Delivery>=50 and successful_Delivery<=59:
        amount_per_parcel= 200
        
        payment = successful_Delivery * amount_per_parcel + BASE_PAY
        return payment==test_wages
    elif (successful_Delivery>=60 and successful_Delivery<=69):
        amount_per_parcel= 250
    
        payment = successful_Delivery * amount_per_parcel + BASE_PAY;
        return payment==test_wages
    elif (successful_Delivery >=70):
        amount_per_parcel= 500
    
        payment = successful_Delivery * amount_per_parcel + BASE_PAY;
        return payment==test_wages
   
 

