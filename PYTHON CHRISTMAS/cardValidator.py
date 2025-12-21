number = input("\nHello Kindly enter card number to verify:\n")


if number.startswith("4"):
    print("\n**Card Type: Visa Card")
elif number.startswith("5"):
    print("**Card Type: Master Card")
elif number.startswith("37"):
    print("**Card Type: American Express Card")
elif number.startswith("6"):
    print("**Card Type: Discover Card")
else:
    print("**Card Type: Invalid")

if len(number) < 13 or len(number) > 16:
    print("**Card Number: Invalid length")
    

for ch in number:
    if not ch.isdigit():
        print("**Card Number: Invalid (non-digit found)")
        break

print(f"**Card Number Length: {len(number)}")
print(f"**Card Number: {number}")


total = 0

for index in range(len(number) - 1, -1, -1):
    new_number = int(number[index])

    if index % 2 == 0:
        new_number *= 2
        if new_number > 9:
            new_number -= 9

    total += new_number

if total % 10 == 0:
    print("**Card Validity: Valid")
else:
    print("**Card Validity: Invalid")

