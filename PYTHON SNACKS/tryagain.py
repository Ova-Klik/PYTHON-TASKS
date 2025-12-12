menu = """
            NOKIA 3310

            === MAIN PHONE MENU ===
            1. Phone book
            2. Messages
            3. Chat
            4. Call register
            5. Tones
            6. Settings
            7. Call divert
            8. Info service
            9. Voice mailbox number
            10. Service command editor
            11. Clock
            12. Profiles
            13. SIM Services

   
    """

print(menu)
main_menu_choice = int(input("Select option: "))

match main_menu_choice:
    case 1:
        print("Search has been selected\n")
    case 2:
        print("Service nos selected\n")
    case 3:
        print("Add name selected\n")
    case 4:
        print("Erase selected\n")
    case 5:
        print("Edit selected\n")
    case 6:
        print("Assign tone selected\n")
    case 7:
        print("Sending b'card...\n")
    case _:
        print("Sendinasjkdhkashdkjasdkjd...\n")
                    
