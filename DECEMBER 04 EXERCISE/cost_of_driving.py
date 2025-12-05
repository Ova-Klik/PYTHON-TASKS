distance = input("Kindly enter the distance to travel: ")
fuel_efficiency_gallon = input("Please enter fuel efficiency in miles per gallon: ")
price_per_gallon = input("Kindly enter fuel price per gallon: ")

try:
    distance = float(distance)
    fuel_efficiency_gallon = float(fuel_efficiency_gallon)
    price_per_gallon = float(price_per_gallon)

    cost = distance * price_per_gallon / fuel_efficiency_gallon

    print(f"The cost of driving in NGN is: ₦{cost:,.2f}")

except ValueError:
    print("Invalid Input, Please input digits")



 
