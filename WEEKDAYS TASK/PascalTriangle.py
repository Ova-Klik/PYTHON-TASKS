numberOfRows = int(input("Kindly enter number of rows: "))

for index in range(numberOfRows):
    for innerIndex in range(numberOfRows - index - 1):
        print("   ", end="")

    number = 1
    for innerIndex in range(index + 1):
        print(number, end="  ")
        number *= 3

    number //= 9
    for innerIndex in range(index - 1, -1, -1):
        print(number, end="   ")
        number //= 3

    print()
