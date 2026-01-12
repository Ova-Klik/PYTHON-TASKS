from cardValidatorMethod import card_validator_checker


class card_validator_main:

    number=input("\nHello Kindly enter card number to verify:\n ")

    card_validator_checker.validate_card(number)
