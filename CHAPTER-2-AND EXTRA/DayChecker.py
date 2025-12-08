#monday is 1/7 the
#sunday is 6

number=int(input("Enter a single number :\n" ))

check=number%7

if check==0:
    print(f"It will be Thursday in {number} days")
elif check==1:
    print(f"It will be Friday in {number} days")
elif check==2:
    print(f"It will be Saturday  in {number} days")
elif check==3:
    print(f"It will be Sunday in {number} days")
elif check==4:
    print(f"It will be Monday in {number} days")
elif check==5:
    print(f"It will be Tuesday in {number} days")
elif check==6:
    print(f"It will be Wednesday in {number} days")
