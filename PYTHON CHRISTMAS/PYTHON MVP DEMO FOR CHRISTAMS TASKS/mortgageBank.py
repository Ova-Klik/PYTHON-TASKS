principal = float(input("Enter the Principal: "))
annual_interest = float(input("Enter the Annual Interest Rate: "))
duration = float(input("Enter the Duration: "))

def mortgage_calculator(principal, annual_interest, duration):
    duration*=12
    rate=annual_interest/100/12
    
    monthly_payment= principal*(((1+rate)**duration)*rate)/(((1+rate)**duration)-1)
    
    return monthly_payment
    
    
    
print(f"Your monthly payment is: ${mortgage_calculator(principal, annual_interest, duration): .2f}")
