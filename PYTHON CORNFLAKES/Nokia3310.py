while True:
    menu = 
    
    """

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
        print("\n Nokia 3310...")
        break

    # 1. PHONE BOOK
 
    elif main_menu_choice== 1:
        while True:
            print(
            """
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
                
            phone_book = int(input("Enter option: "))

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
                    print(
                    """
                            --- Options ---
                            1. Type of view
                            2. Memory status
                            
                            0. Back
                    """)
                    options_menu_choice = int(input("Select: "))
                    if  options_menu_choice == 0:
                        break
                     case 1:
                        print("Search has been selected\n")
                     case 2:
                        print("Service nos selected\n")
                     case 3:
                        print("Add name selected\n")
                     case _:
                        print("Invalid option\n")  
            case 9:
                print("Assign tone selected\n")
            case 10:
                print("Sending b'card...\n")
            case _:
               print("Invalid option\n")    

    # 2. MESSAGES
   
    elif  main_menu_choice == 2:
        while True:
            print(
                    """
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
                
            elif phone_book == 1:
                print("Write messages selected\n")
            elif phone_book == 2:
                print("Inbox selected\n")
            elif phone_book == 3:
                print("Outbox selected\n")
            elif phone_book == 4:
                print("Picture message\n")
            elif phone_book == 5:
                print("Templates selected\n"))
            elif phone_book == 6:
                print("Smileys displayed\n"))

            elif message_menu_choice == 7:
                while True:
                    print(
                    """
                         --- Message settings ---
                            1. Set 1
                            2. common 3
                            
                            0. Back
                    
                    """)
                    message_setting_choice = int(input("Select: "))
                    if message_setting_choice == 0:
                        break
                        
                        elif message_setting_choice == 1:
                        
                            while True:
                                print(
                                """
                                        --- set 1 ---
                                        1. Messsage centre number
                                        2. Message sent as
                                        3. Message validity
                                        
                                        0. Back
                                
                                """)
                            set1_choice = int(input("Select: "))
                            if set1_choice == 0:
                                break
                                   
                                elif set1_choice == 1:
                                    print("Message centre number selected\n")
                                elif set1_choice == 2:
                                    print("Message sent as....\n")
                                elif set1_choice == 3:
                                    print("Message validity selected\n")
                        
                        elif message_setting_choice == 2:
                        
                            while True:
                                print(
                                """
                                        --- common 3 ---
                                        1. Delivery reports
                                        2. Reply via same centre
                                        3. Character support
                                        
                                        0. Back
                                
                                """)
                            common3_choice = int(input("Select: "))
                            if common3_choice == 0:
                                break
                                   
                                elif common3_choice == 1:
                                    print("Delivery reports selected\n")
                                elif common3_choices == 2:
                                    print("Reply via same centre....\n")
                                elif common3_choice == 3:
                                    print("Character support selected\n")

            elif phone_book == 8:
                print("Info service \n")
            elif phone_book == 9:
                print("Voice mailbox number selected\n"))
            elif phone_book == 10:
                print("Service command editor displayed\n"))
                    
            else:
                    
                print("Invalid input")

  
    # 3. CHAT
   
    elif  main_menu_choice  == 3:
        print("Chat selected\n")

   
    # 4. CALL REGISTER

    elif  main_menu_choice  == 4:
        while True:
            print(
            
            """
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

            if call_register_menu== 0:
                break
                
            match phone_book:
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
            case _:
                print("Invalid option\n")


    # 5. TONES
  
    elif  main_menu_choice == 5:
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
            t = int(input("Select: "))

            if t == 0:
                break
            print("Selected\n")

  
    # 6. SETTINGS

    elif main_menu_choice == 6:
        while True:
            print("""
            --- Settings ---
            1. Call settings
            2. Phone settings
            3. Security settings
            4. Restore factory settings
            0. Back
            """)
            s = int(input("Select: "))

            if s == 0:
                break

            elif s == 4:
                print("Factory settings restored\n")
            else:
                print("Selected\n")

   
    # 7. CALL DIVERT

    elif  main_menu_choice == 7:
        print("Call divert selected\n")

    
    # 8. INFO SERVICE

    elif  main_menu_choice  == 8:
        print("Info service selected\n")

    # 9. VOICE MAILBOX NUMBER

    elif main_menu_choice  == 9:
        print("Voice mailbox number selected\n")

    
    # 10. SERVICE COMMAND EDITOR
 
    elif  main_menu_choice  == 10:
        print("Service command editor selected\n")


    # 11. CLOCK
    
    elif  main_menu_choice  == 11:
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
            cl = int(input("Select: "))
            if cl == 0:
                break
            print("Selected\n")


    # 12. PROFILES
 
    elif  main_menu_choice  == 12:
        print("Profiles selected\n")
        
 # 13. SIM SERVICES

    elif  main_menu_choice  == 13:
        print("SIM Services selected\n")

    else:
        print("Invalid input\n")

