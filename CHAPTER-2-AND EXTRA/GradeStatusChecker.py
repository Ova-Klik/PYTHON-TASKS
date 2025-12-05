grade=input("Please input your Score to Know your Status: ")

if not grade.isdigit():  
    print("Invalid Input, Please try again")
else: 
    grade=int(grade)
    if grade >=90:
        print(f" Congratulations! Your Grade of {grade} earns you an A in this course") 

    elif grade >= 60 and grade <90:
        print(f" You did Good! Your Grade of {grade} earns you an A in this course") 

    elif grade <=59:
        print(f" You can do better! Your Grade of {grade} is not so great") 
