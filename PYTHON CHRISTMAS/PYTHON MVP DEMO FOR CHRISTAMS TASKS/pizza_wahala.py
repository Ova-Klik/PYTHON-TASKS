import math

pizza_menu="""

                    ____________IYA SCAMBIRAH PIZZA____________
            
            _____________________________________________________________           
            |               |                       |                   |
            |   Pizza type  |   Number of Slices    |   Prices per Box  |
            |_______________|_______________________|___________________|
            |               |                       |                   |
            |   Sapa Size   |       4               |   2,000           |
            |_______________|_______________________|___________________|
            |               |                       |                   |
            |   Small Money |       6               |   2,400           |
            |_______________|_______________________|___________________|
            |               |                       |                   |
            |   Big Boys    |       8               |   3,000           |
            |_______________|_______________________|___________________|
            |               |                       |                   |
            |   Odogwu      |       12              |   4,200           |
            |_______________|_______________________|___________________|          
            

          """
          
print(pizza_menu)
number_of_people = int(input("How many people will you be serving: "))
pizza_type=input("Enter the type of pizza you like to order: ")..lower()



match pizza_type:
    case"sapa size":
        price = 2000
        slice_per_box=4
    case"small money":
        price = 2400
        slice_per_box = 6 
    case"big boys":
        price = 3000
        slice_per_box = 8
        
    case"odogwu":
        price = 4200
        slice_per_box = 12 
            
        
number_of_boxes = math.ceil(number_of_people/slice_per_box)
left_over_slices = number_of_boxes * slice_per_box - number_of_people
price = number_of_boxes * price
        
print(f"\nNumber of boxes to buy = {number_of_boxes} boxes")
print(f"Total price = {price}")     
print(f"Number of left over slice after serving = {left_over_slices} slice\n")
           
        
    


