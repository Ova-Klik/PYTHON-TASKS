from datetime import datetime
import re


account_balance=0
transaction_history=[]
amount_regex= re.compile(r"^(?!0+(\.0+)?$)\d+(\.\d{1,2})?$")


def deposit(account_balance,transaction_history):
    while True:
        amount=input("Kindly enter amount to deposit:$ ")
        if not amount_regex.fullmatch(amount):
            print("\n\tInvalid input!\n")
            continue
        else:
            amount = float(amount)
            account_balance+=amount
            transaction_time=datetime.now().strftime("%d-%m-%y %I:%M %P")
            transaction_history.append({"Date & Time": transaction_time,
            "Type":"deposit",
            "Amount": amount,
            "Balance": account_balance,
                    
                
             })
                
                         
        print(f""" 
   
                         {'':<15}{'Deposit Successful!'}
                         
                         {'Date & Time':<20}  {'Amount':<12}      {'Balance'}
                         
                         {transaction_time:<20}  ${amount:<16,}  ${account_balance:,}
                         
                  """)
                      
                
                
        more=input("Will you like to make more deposit? (yes/no): ").casefold()
        if more=="no":
            print("\nThank you for banking with us!\n")
            break
    return account_balance        
      
def withdrawal(account_balance,transaction_history):    
    
    while True:
        
        amount=input("Kindly enter amount to withdraw:$ ")
        if not amount_regex.fullmatch(amount):
            print(f"\n\tInvalid input!\n")
            continue
        else:
            amount = float(amount)
           
        if amount > account_balance:
            print("\n\t\tInsufficient funds!!!\n")
            break
            
        else:  
           
            account_balance-=amount
            transaction_time=datetime.now().strftime("%d-%m-%y %I:%M %P")
            transaction_history.append({"Date & Time": transaction_time,
            "Type":"Withdrawal",
            "Amount": amount,
            "Balance": account_balance,
                
                })
                    
            print(f"""
                
                         {'':<15} {'Withdrawal Successful!'}
                         
                         {'Date & Time':<20}  \t\tAmount:      \tBalance
                         
                         {transaction_time:<4}  \t${amount:<8,} ${account_balance:,}
                         
                      """ ) 
                
            more=input("Will you like to make more withdrawal? (yes/no): ").casefold()
            if more=="no":
            
                print("\nThank you for banking with us!\n")
                break
    return account_balance
                
def history(transaction_history):
   
        print("\n\t\t\t\t-- TRANSACTION HISTORY --\n")

        print(f"\t{'No.':<4}\t{'Date & Time':<20}\t{'Type':<15}\t{'Amount':<15}\t{'Balance':<15}")
        print(f"=" * 85)

        for index, transaction in enumerate(transaction_history, start=1):
            print(
                    f"\t{index:<4}"
                    
                    f"\t{transaction['Date & Time']:<20}"
                    
                    f"\t{transaction['Type']:<15}"
                    
                    f"\t${transaction['Amount']:<10,}"
                    
                    f"\t${transaction['Balance']:,}"
                    
                    
                )
        more =input("\n\nKindly exit to main menu: ").casefold() 
        break                    

while True:
    transaction_time=datetime.now().strftime("%d-%m-%y %I:%M %P")
    account_menu=f"""
            
            {transaction_time:4s}
                     
                               Welcome to Transaction Log App
                               
                               1. Deposit Money
                               
                               2. Withdraw Money
                               
                               3. Show transaction history
                               
                               4. Exit the App.
                            
    
                 """
    print(account_menu)
    menu_option=int(input("Enter operation: "))
    
    if menu_option==4:
        print("\nThank you for using Transaction Log App")
        break
    
    match menu_option:
        case 1:
            account_balance = deposit(account_balance, transaction_history)
                
        case 2:
            account_balance = withdrawal(account_balance,transaction_history)
                        
        case 3:
            history(account_balance,transaction_history)
            
        case _:
        
            print("\nInvalid operation\n\n")
    
    
    
