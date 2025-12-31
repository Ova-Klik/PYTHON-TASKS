book_title= ["The Hobbit", "The Mystery"]
book_pages= ["47","12"]
book_author= ["wisdom craig","victor byte"]


while True:
    
    book_menu= """
    
                    --- Welcome To The Book Suggestion System ---
                    
                        1.  Get Suggetstion
                        2.  Add Book
                        3.  Remove Book
                        4.  Update Book
                        5.  Show all Books
                        
                        0.  Exit
                        
               """
    print(book_menu)
    
    
    
    menu_option=int(input("Enter operation:"))
    if menu_option==0:
        print(f"\n      Thank you for visiting the library...\n")
        break
    
    
    match menu_option:
        case 1:
            index=0
            more="yes"
            while True: 
                if index >= len(book_title):
                    suggest_more=input("No more books to suggest\n\n Would you like to add a book? (yes/no)")
                    if suggest_more=="yes":
                        print("Thank you for contributing, please press 2 to add book.")
                        break 
                        
                    else:
                        print("\n\nThe for visiting the library....\n\n")
                        break 
                else:
                    print(f"""

                        ---Book For The Day---
                           
                           Book Title: {book_title[index]}
                           Pages: {book_pages[index]}
                           Book Author: {book_author[index]}
                
                          """)         
                    index+=1      
                    
                    more=input("Would you like to get another suggestion? (yes/no): ").casefold()
                
                    if more=="no":
                        print(f"Thank you!Kindly check back later!\n\n")
                        break
                    
        case 2:
            counter=0
            while True:
                book_exists = False

                add_book = input("Kindly enter the Book Title to add: ").casefold()

                for index in range(len(book_title)):
                    if book_title[index].casefold() == add_book:
                        book_exists = True
                        break

                if book_exists:
                    print(f"\n'{add_book}' already exists in record!")
                  
                else:
                    book_title.append(add_book)
                    
                    book_pages.append(input("Kindly enter the Number of pages: "))

                    book_author.append(input("Kindly enter the Name of author: "))
                    counter+=1
                    print(f"\n'{add_book}' added to the record successfully!")

                more=input("Would you like to add another book? (yes/no): ").casefold()
                
                if more=="no":
                    print(f"\n You have added {counter} Books to the record!\n")
                    print(f"\n Thank you!Kindly check back later!\n\n")
                    break
               
                                                         
            
        case 3:
            counter=0
            while True:
                index_match = -1
                more="yes"
                rem_book = input("Kindly enter the Book Title to remove: ").casefold()

                for index in range(len(book_title)):
                    if book_title[index].casefold() == rem_book:
                        index_match = index
                        break

                if index_match != -1:
                    removed = book_title.pop(index_match)
                    del book_pages[index_match]
                    del book_author[index_match]
                    
                    counter+=1
                    
                    print(f"\n'{removed}' removed successfully!")
                else:
                    print("\n         Book title not found in record!!!\n")
                    index_match = -1
                    
                more=input("Would you like to remove another book? (yes/no): ").casefold()
                    
                if more=="no":
                    print(f"\n You hav removed {counter} Book(s)! \n")
                    print(f"Thank you! \n\n")
                    break       

        case 4:
            counter=0
            while True:
                index_match = -1
                more="yes"
                update_book = input("Kindly enter the Book Title to remove: ").casefold()

                for index in range(len(book_title)):
                    if book_title[index].casefold() == update_book:
                        index_match = index
                        break

                if index_match != -1:
                    book_title[index_match]=input("Kindly enter new Book Title: ")
                    book_pages[index_match]=input("Kindly enter new Number of pages: ")
                    book_author[index_match]=input("Kindly enter new name of author: ")
                    
                    counter+=1
                    
                    print(f"\n'{update_book}' updated successfully!")
                else:
                    print("\n         Book title not found in record!!!\n")
                    index_match = -1
                    
                more=input("Would you like to update another book? (yes/no): ").casefold()
                    
                if more=="no":
                    print(f"\n You have updated {counter} Book(s)! \n")
                    print(f"Thank you! \n\n")
                    break
                    
        case 5:
            
            while True:
                print(f"                ---List of Books in Library---")
                for index in range(len(book_title)):
                    
                    print(f"""
                                Book: {index+1}
                                Title: {book_title[index]}
                                Pages: {book_pages[index]}
                                Author: {book_author[index]}
                                
                    
                            """)
               
                break                                  
        
    
               
              
           

