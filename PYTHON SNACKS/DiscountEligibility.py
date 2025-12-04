
total_bill = float(input('Kindly enter the Bill Total' ))
is_member = input('Are you a member (Y/N)' )

if (is_member == 'Y' or 'y'):

    if (total_bill >= 1000):
        print ('You are eligible for a Discount of 10%off: \n', 'Your Discounted price is', total_bill*0.1)

if (total_bill < 1000):
    print ('You are eligible for a Discount of 5%off: \n','Your Discounted price is ', total_bill * 0.05 )

    else: 
            print ('Your Total Bill is:', total_bill ,'\n\tYou can Subscribe to be a member for Discounts on your purchases' )





