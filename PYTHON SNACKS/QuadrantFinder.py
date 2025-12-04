first_number=int(input('Please input First number: '))
second_number=int(input('Kindly enter Second number: '))


if (first_number>0 and second_number>0):
    print ('First Quadrant')

elif (first_number<0 and second_number>0):
    print ('Second Quadrant')

elif (first_number<0 and second_number<0):
    print ('Third Quadrant')

elif (first_number>0 and second_number<0):
    print ('Fourth Quadrant')

elif (first_number==0 and second_number==0):
    print ('This is at Origin 0')

elif (first_number==0 and second_number!=0):
    print ('This is on X-axis')

else:
    print ('Definitely on Y-axis')



