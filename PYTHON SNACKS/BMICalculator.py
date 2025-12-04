weight=int(input('Enter weight in KG:'))
height=int(input('Enter height in KG:'))

bmi=weight/(height*height);

if bmi>18.5:

    print('Underweight')

elif (bmi==18.5 and bmi<=24.9):

    print('Normal')

elif (bmi==25  and bmi<=29.9):
    
    print('Overweight')

else:
    print('Obese')
