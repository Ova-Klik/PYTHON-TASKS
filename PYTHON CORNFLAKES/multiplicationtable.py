
number = int(input("Enter a number to display its multiplication table: "))


for count in range(1, 11):
    result = number * count
    print(f"{number} x {count} = {result}")

