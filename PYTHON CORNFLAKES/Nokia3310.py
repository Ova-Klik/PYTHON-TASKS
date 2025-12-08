while True:
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

            0. Power off
    """

    print(menu)
    main_menu_choice = int(input("Select option: "))

    if main_menu_choice == 0:
        print("\n Nokia 3310 ...")
        break

    match main_menu_choice:
        # 1. PHONE BOOK
        case 1:
            while True:
                print("""
                    --- Phone book ---
                    1. Search
                    2. Service Nos.
                    3. Add name
                    4. Erase
                    5. Edit
                    6. Assign tone
                    7. Send b'card
                    8. Options
                    9. Speed dials
                    10. Voice tags
                    0. Back
                """)
                phone_book = int(input("Select: "))
                if phone_book == 0:
                    break

                match phone_book:
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
                    case 8:
                        while True:
                            print("""
                                --- Options ---
                                1. Type of view
                                2. Memory status
                                0. Back
                            """)
                            options_menu_choice = int(input("Select: "))
                            if options_menu_choice == 0:
                                break
                            match options_menu_choice:
                                case 1:
                                    print("Type of view selected\n")
                                case 2:
                                    print("Memory status selected\n")
                                case _:
                                    print("Invalid option\n")
                    case 9:
                        print("Speed dials selected\n")
                    case 10:
                        print("Voice tags selected\n")
                    case _:
                        print("Invalid option\n")

        # 2. MESSAGES
        case 2:
            while True:
                print("""
                    --- Messages ---
                    1. Write message
                    2. Inbox
                    3. Outbox
                    4. Picture messages
                    5. Templates
                    6. Smileys
                    7. Message settings
                    0. Back
                """)
                message_menu_choice = int(input("Select: "))
                if message_menu_choice == 0:
                    break

                match message_menu_choice:
                    case 1:
                        print("Write messages selected\n")
                    case 2:
                        print("Inbox selected\n")
                    case 3:
                        print("Outbox selected\n")
                    case 4:
                        print("Picture message\n")
                    case 5:
                        print("Templates selected\n")
                    case 6:
                        print("Smileys displayed\n")
                    case 7:
                        while True:
                            print("""
                                --- Message settings ---
                                1. Set 1
                                2. Common 3
                                0. Back
                            """)
                            message_setting_choice = int(input("Select: "))
                            if message_setting_choice == 0:
                                break
                            match message_setting_choice:
                                case 1:
                                    while True:
                                        print("""
                                            --- Set 1 ---
                                            1. Message centre number
                                            2. Message sent as
                                            3. Message validity
                                            0. Back
                                        """)
                                        set1_choice = int(input("Select: "))
                                        if set1_choice == 0:
                                            break
                                        match set1_choice:
                                            case 1:
                                                print("Message centre number selected\n")
                                            case 2:
                                                print("Message sent as selected\n")
                                            case 3:
                                                print("Message validity selected\n")
                                            case _:
                                                print("Invalid Input...\n")
                                case 2:
                                    while True:
                                        print("""
                                            --- Common 3 ---
                                            1. Delivery reports
                                            2. Reply via same centre
                                            3. Character support
                                            0. Back
                                        """)
                                        common3_choice = int(input("Select: "))
                                        if common3_choice == 0:
                                            break
                                        match common3_choice:
                                            case 1:
                                                print("Delivery reports selected\n")
                                            case 2:
                                                print("Reply via same centre selected\n")
                                            case 3:
                                                print("Character support selected\n")
                                            case _:
                                                print("Invalid Input...\n")
                    case _:
                        print("Invalid Input...\n")

        # 3. CHAT
        case 3:
            print("Chat selected\n")

        # 4. CALL REGISTER
        case 4:
            while True:
                print("""
                    --- Call register ---
                    1. Missed calls
                    2. Received calls
                    3. Dialled numbers
                    4. Erase recent call lists
                    5. Show call duration
                    6. Show call costs
                    7. Call cost settings
                    8. Prepaid credit
                    0. Back
                """)
                call_register_menu = int(input("Select: "))
                if call_register_menu == 0:
                    break

                match call_register_menu:
                    case 1:
                        print("Missed calls selected\n")
                    case 2:
                        print("Received calls selected\n")
                    case 3:
                        print("Dialled numbers selected\n")
                    case 4:
                        print("Erase recent call lists selected\n")
                    case 5:
                        while True:
                            print("""
                                --- Show call duration ---
                                1. Last call duration
                                2. All calls’ duration
                                3. Received calls’ duration
                                4. Dialled calls’ duration
                                5. Clear timers
                                0. Back
                            """)
                            call_duration_menu = int(input("Select: "))
                            if call_duration_menu == 0:
                                break
                            match call_duration_menu:
                                case 1:
                                    print("Last call duration displayed\n")
                                case 2:
                                    print("All call duration displayed\n")
                                case 3:
                                    print("Received call duration displayed\n")
                                case 4:
                                    print("Dialled call duration displayed\n")
                                case 5:
                                    print("Timers cleared\n")
                                case _:
                                    print("Invalid option\n")
                    case 6:
                        while True:
                            print("""
                                --- Show call costs ---
                                1. Last call cost
                                2. All calls’ cost
                                3. Clear counters
                                0. Back
                            """)
                            call_costs_menu = int(input("Select: "))
                            if call_costs_menu == 0:
                                break
                            match call_costs_menu:
                                case 1:
                                    print("Last call cost displayed\n")
                                case 2:
                                    print("All call cost displayed\n")
                                case 3:
                                    print("Counters cleared\n")
                                case _:
                                    print("Invalid option\n")
                    case 7:
                        while True:
                            print("""
                                --- Call cost settings ---
                                1. Call cost limit
                                2. Show cost in
                                0. Back
                            """)
                            call_costs_setting_menu = int(input("Select: "))
                            if call_costs_setting_menu == 0:
                                break
                            match call_costs_setting_menu:
                                case 1:
                                    print("Call cost limit displayed\n")
                                case 2:
                                    print("Show cost in displayed\n")
                                case _:
                                    print("Invalid option\n")
                    case 8:
                        print("Prepaid credit displayed\n")
                    case _:
                        print("Invalid option\n")

        # 5. TONES
        case 5:
            while True:
                print("""
                    --- Tones ---
                    1. Ringing tone
                    2. Ringing volume
                    3. Incoming call alert
                    4. Composer
                    5. Message alert tone
                    6. Keypad tones
                    7. Warning and game tones
                    8. Vibrating alert
                    9. Screen saver
                    0. Back
                """)
                tones_menu_choice = int(input("Select: "))
                if tones_menu_choice == 0:
                    break
                match tones_menu_choice:
                    case 1:
                        print("Ringing tone displayed\n")
                    case 2:
                        print("Ringing volume displayed\n")
                    case 3:
                        print("Incoming call alert displayed\n")
                    case 4:
                        print("Composer displayed\n")
                    case 5:
                        print("Message alert tone displayed\n")
                    case 6:
                        print("Keypad tones displayed\n")
                    case 7:
                        print("Warning and game tones displayed\n")
                    case 8:
                        print("Vibrating alert displayed\n")
                    case 9:
                        print("Screen saver displayed\n")
                    case _:
                        print("Invalid option\n")

        # 6. SETTINGS
        case 6:
            while True:
                print("""
                    --- Settings ---
                    1. Call settings
                    2. Phone settings
                    3. Security settings
                    4. Restore factory settings
                    0. Back
                """)
                setting_menu = int(input("Select: "))
                if setting_menu == 0:
                    break
                match setting_menu:
                    case 1:
                        while True:
                            print("""
                                --- Call Settings ---
                                1. Automatic redial
                                2. Speed dialling
                                3. Call waiting options
                                4. Own number sending
                                5. Phone line in use
                                6. Automatic answer
                                0. Back
                            """)
                            call_setting_menu = int(input("Select: "))
                            if call_setting_menu == 0:
                                break
                            match call_setting_menu:
                                case 1:
                                    print("Automatic redial set\n")
                                case 2:
                                    print("Speed dialling set\n")
                                case 3:
                                    print("Call waiting options displayed\n")
                                case 4:
                                    print("Own number sending selected\n")
                                case 5:
                                    print("Phone line in use\n")
                                case 6:
                                    print("Automatic answer set\n")
                                case _:
                                    print("Invalid Input\n")
                    case 2:
                        while True:
                            print("""
                                --- Phone Settings ---
                                1. Language
                                2. Cell info display
                                3. Welcome note
                                4. Network selection
                                5. Lights 2
                                6. Confirm SIM service actions
                                0. Back
                            """)
                            phone_setting_menu = int(input("Select: "))
                            if phone_setting_menu == 0:
                                break
                            match phone_setting_menu:
                                case 1:
                                    print("Language selected\n")
                                case 2:
                                    print("Cell info displayed\n")
                                case 3:
                                    print("Welcome note displayed\n")
                                case 4:
                                    print("Network selections displayed\n")
                                case 5:
                                    print("Lights 2 displayed\n")
                                case 6:
                                    print("Confirm SIM service actions displayed\n")
                                case _:
                                    print("Invalid Input\n")
                    case 3:
                        while True:
                            print("""
                                --- Security Settings ---
                                1. PIN code request
                                2. Call barring service
                                3. Fixed dialling
                                4. Closed user group
                                5. Phone security
                                6. Change access codes
                                0. Back
                            """)
                            security_setting_menu = int(input("Select: "))
                            if security_setting_menu == 0:
                                break
                            match security_setting_menu:
                                case 1:
                                    print("PIN code requested\n")
                                case 2:
                                    print("Call barring service selected\n")
                                case 3:
                                    print("Fixed dialling selected\n")
                                case 4:
                                    print("Closed user group displayed\n")
                                case 5:
                                    print("Phone security displayed\n")
                                case 6:
                                    print("Change access codes displayed\n")
                                case _:
                                    print("Invalid Input\n")
                    case 4:
                        print("Factory settings restored\n")
                    case _:
                        print("Invalid Input\n")

        # 7. CALL DIVERT
        case 7:
            print("Call divert selected\n")

        # 8. INFO SERVICE
        case 8:
            print("Info service selected\n")

        # 9. VOICE MAILBOX NUMBER
        case 9:
            print("Voice mailbox number selected\n")

        # 10. SERVICE COMMAND EDITOR
        case 10:
            print("Service command editor selected\n")

        # 11. CLOCK
        case 11:
            while True:
                print("""
                    --- Clock ---
                    1. Alarm clock
                    2. Clock settings
                    3. Date settings
                    4. Stopwatch
                    5. Countdown timer
                    6. Auto update time/date
                    0. Back
                """)
                clock_menu = int(input("Select: "))
                if clock_menu == 0:
                    break
                match clock_menu:
                    case 1:
                        print("Alarm clock selected\n")
                    case 2:
                        print("Clock settings selected\n")
                    case 3:
                        print("Date settings selected\n")
                    case 4:
                        print("Stopwatch displayed\n")
                    case 5:
                        print("Countdown timer displayed\n")
                    case 6:
                        print("Auto update time/date displayed\n")
                    case _:
                        print("Invalid Input\n")

        # 12. PROFILES
        case 12:
            print("Profiles selected\n")

        # 13. SIM SERVICES
        case 13:
            print("SIM Services selected\n")

        case _:
            print("Invalid input\n")

