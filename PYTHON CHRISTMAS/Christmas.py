while True:
    christmas_song_playlist=    """
                                --Twelve Days of Christmas playlist--
                                
                                1.  First day of christmas
                                2.  Second day of christmas
                                3.  Third day of christmas
                                4.  Fourth day of christmas
                                5.  Fifth day of christmas
                                6.  Sixth day of christmas
                                7.  Seventh day of christmas
                                8.  Eight day of christmas
                                9.  Ninth day of christmas
                                10. Tenth day of christmas
                                11. Eleventh day of christmas
                                12. Twelfth day of christmas 
                                
                                0.  exit
                                

                            """
    print(christmas_song_playlist)

    christmas_playlist=int(input("Select the day of christmas: "))
    if christmas_playlist==0:
        print("Merry Christmas and a Happy new year in advance!!!!!")
        break
    match christmas_playlist:
            case 1: 
                while True:
                    print( """
                            --First day of christmas--
                                                                
                            1.  First day's Lyrics
                            0.  Done.
                          """)
                    first_day_lyrics=int(input("select to options: "))
                    if first_day_lyrics==0:
                        print ("Party continues tommorrow")
                        break
                        
                    match first_day_lyrics:
                        case 1: print("""
                                        On the first day of Christmas
                                        My true love gave to me
                                        A partridge in a pear tree
                        
                                """)
                        case _: print("Invalid option")           
              
            case 2: 
                while True:
                    print( """
                            --Second day of christmas--
                                                                
                            1.  Second day's Lyrics
                            0.  Done.
                          """)
                    second_day_lyrics=int(input("select to options: "))
                    if second_day_lyrics==0:
                        print ("Party continues tommorrow")
                        break
                        
                    match second_day_lyrics:
                        case 1: print("""
                                        On the second day of Christmas
                                        My true love gave to me
                                        Two turtle doves
                                        And a partridge in a pear tree





                        
                                """)  
                               
            case 3: 
                while True:
                    print( """
                            --Third day of christmas--
                                                                
                            1.  Third day's Lyrics
                            0.  Done.
                          """)
                    third_day_lyrics=int(input("select to options: "))
                    if third_day_lyrics==0:
                        print ("Party continues tommorrow")
                        break
                        
                    match third_day_lyrics:
                        case 1: print("""
                                        On the third day of Christmas
                                        My true love gave to me
                                        Three French hens
                                        Two turtle doves
                                        And a partridge in a pear tree (how wonderful)
                        
                                """)                    
                  
            
                    
            case 4: 
                while True:
                    print( """
                            --Fourth day of christmas--
                                                                
                            1.  Fourth day's Lyrics
                            0.  Done.
                          """)
                    fourth_day_lyrics=int(input("select to options: "))
                    if first_day_lyrics==0:
                        print ("Party continues tommorrow")
                        break
                        
                    match fourth_day_lyrics:
                        case 1: print("""
                                        On the fourth day of Christmas
                                        My true love gave to me
                                        Four calling birds
                                        Three French hens
                                        Two turtle doves
                                        And a partridge in a pear tree
                        
                                """)  
            case 5: 
                while True:
                    print( """
                            --Fifth day of christmas--
                                                                
                            1.  Fifth day's Lyrics
                            0.  Done.
                          """)
                    fifth_day_lyrics=int(input("select to options: "))
                    if fifth_day_lyrics==0:
                        print ("Party continues tommorrow")
                        break
                        
                    match fifth_day_lyrics:
                        case 1: print("""
                                        On the fifth day of Christmas
                                        My true love gave to me
                                        Five golden rings
                                        Four calling birds
                                        Three French hens
                                        Two turtle doves
                                        And a partridge in a pear tree (fantastic)
                        
                                """)
                                
            case 6: 
                while True:
                    print( """
                            --Sixth day of christmas--
                                                                
                            1.  Sixth day's Lyrics
                            0.  Done.
                          """)
                    sixth_day_lyrics=int(input("select to options: "))
                    if sixth_day_lyrics==0:
                        print ("Party continues tommorrow")
                        break
                        
                    match sixth_day_lyrics:
                        case 1: print("""
                                        On the sixth day of Christmas
                                        My true love gave to me
                                        Six geese a-laying
                                        Five golden rings
                                        Four calling birds
                                        Three French hens
                                        Two turtle doves
                                        And a partridge in a pear tree
                                                                
                                """)
            
            case 7: 
                while True:
                    print( """
                            --Seventh day of christmas--
                                                                
                            1.  Seventh day's Lyrics
                            0.  Done.
                          """)
                    seventh_day_lyrics=int(input("select to options: "))
                    if seventh_day_lyrics==0:
                        print ("Party continues tommorrow")
                        break
                        
                    match seventh_day_lyrics:
                        case 1: print("""
                                        On the seventh day of Christmas
                                        My true love gave to me
                                        Seven swans a-swimming
                                        Six geese a-laying
                                        Five golden rings
                                        Four calling birds
                                        Three French hens
                                        Two turtle doves
                                        And a partridge in a pear tree
                                                                
                                """)  
              
            case 8: 
                while True:
                    print( """
                            --Eight day of christmas--
                                                                
                            1.  Eight day's Lyrics
                            0.  Done.
                          """)
                    eight_day_lyrics=int(input("select to options: "))
                    if eight_day_lyrics==0:
                        print ("Party continues tommorrow")
                        break
                        
                    match eight_day_lyrics:
                        case 1: print("""
                                        On the eighth day of Christmas
                                        My true love gave to me
                                        Eight maids a-milking
                                        Seven swans a-swimming
                                        Six geese a-laying
                                        Five golden rings
                                        Four calling birds
                                        Three French hens
                                        Two turtle doves
                                        And a partridge in a pear tree (beautiful)
                        
                                """) 
                        case _: print("Invalid option") 
                               
            case 9: 
                while True:
                    print( """Ninth day of christmas--
                                                                
                            1.  Ninth day's Lyrics
                            0.  Done.
                          """)
                    ninth_day_lyrics=int(input("select to options: "))
                    if ninth_day_lyrics==0:
                        print ("Party continues tommorrow")
                        break
                        
                    match ninth_day_lyrics:
                        case 1: print("""
                                        On the ninth day of Christmas
                                        My true love gave to me
                                        Nine ladies dancing
                                        Eight maids a-milking
                                        Seven swans a-swimming
                                        Six geese a-laying
                                        Five golden rings
                                        Four calling birds
                                        Three French hens
                                        Two turtle doves
                                        And a partridge in a pear tree
                        
                                """)                    
                  
                        case _: print("Invalid option") 
                    
            case 10: 
                while True:
                    print( """
                            --Tenth day of christmas--
                                                                
                            1.  Tenth day's Lyrics
                            0.  Done.
                          """)
                    tenth_day_lyrics=int(input("select to options: "))
                    if tenth_day_lyrics==0:
                        print ("Party continues tommorrow")
                        break
                        
                    match tenth_day_lyrics:
                        case 1: print("""
                                        On the tenth day of Christmas
                                        My true love gave to me
                                        Ten lords a-leaping
                                        Nine ladies dancing
                                        Eight maids a-milking
                                        Seven swans a-swimming
                                        Six geese a-laying
                                        Five golden rings
                                        Four calling birds
                                        Three French hens
                                        Two turtle doves
                                        And a partridge in a pear tree
                                                                
                                """)  
                        case _: print("Invalid option") 
            case 11: 
                while True:
                    print( """
                            --Eleventh day of christmas--
                                                                
                            1.  Eleventh day's Lyrics
                            0.  Done.
                          """)
                    eleventh_day_lyrics=int(input("select to options: "))
                    if eleventh_day_lyrics==0:
                        print ("Party continues tommorrow")
                        break
                        
                    match first_day_lyrics:
                        case 1: print("""
                                        On the eleventh day of Christmas
                                        My true love gave to me
                                        Eleven pipers piping
                                        Ten lords a-leaping
                                        Nine ladies dancing
                                        Eight maids a-milking
                                        Seven swans a-swimming
                                        Six geese a-laying
                                        Five golden rings
                                        Four calling birds
                                        Three French hens
                                        Two turtle doves
                                        And a partridge in a pear tree (how lovely)
                        
                                """)
                        case _: print("Invalid option") 
                                
            case 12: 
                while True:
                    print( """
                            --Twelfth day of christmas--
                                                                
                            1.  Twelfth day's Lyrics
                            0.  Done.
                          """)
                    twelfth_day_lyrics=int(input("select to options: "))
                    if twelfth_day_lyrics==0:
                        print ("Party continues tommorrow")
                        break
                        
                    match twelfth_day_lyrics:
                        case 1: print("""
                                        On the twelfth day of Christmas
                                        My true love gave to me
                                        Twelve drummers drumming
                                        Eleven pipers piping
                                        Ten lords a-leaping
                                        Nine ladies dancing
                                        Eight maids a-milking
                                        Seven swans a-swimming
                                        Six geese a-laying
                                        Five golden rings
                                        Four calling birds
                                        Three French hens
                                        Two turtle doves
                                        And a partridge in a pear tree

                        
                                """)
                        case _: print("Invalid option") 
                                
                                
                                
            case _: print("Invalid option")         
