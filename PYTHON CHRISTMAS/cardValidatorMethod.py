class card_validator_checker:

    def card_type_check(number):
        if number.startswith("4"):
            return "Visa Card"
        elif number.startswith("5"):
            return "Master Card"
        elif number.startswith("37"):
            return "American Express Card"
        elif number.startswith("6"):
            return "Discover Card"
        else:
            return "Invalid Card"

 
    def digit_length_check(number):
        if len(number) < 13 or len(number) > 16:
            return False

        for ch in number:
            if not ch.isdigit():
                return False

        return True



    def card_validity_check(number):
        total = 0

        for index in range(len(number) - 1, 0, -1):
            new_number = int(number[index])

            if index % 2 == 0:
                new_number *= 2
                if new_number > 9:
                    new_number -= 9

            total += new_number

        return total % 10 == 0

 
    def validate_card(number):
        card_type = card_validator_checker.card_type_check(number)
        card_digits = card_validator_checker.digit_length_check(number)
        card_validity = card_validator_checker.card_validity_check(number)

        if not card_digits:
            print("\n**Invalid Card Number!**\n")
        elif not card_validity:
            print(f"\n**Credit Card Type: {card_type}")
            print(f"**Credit Card Number: {number}")
            print(f"**Credit Card Digit Length: {len(number)}")
            print("**Credit Card Validity: Invalid\n")
        else:
            print(f"\n**Credit Card Type: {card_type}")
            print(f"**Credit Card Number: {number}")
            print(f"**Credit Card Digit Length: {len(number)}")
            print("**Credit Card Validity: Valid\n")

