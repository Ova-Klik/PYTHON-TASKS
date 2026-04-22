

def merge_dictionary(dictionary1,dictionary2):
 
    dictionary1.update(dictionary2)
    return dictionary1
    

Students = {
                "John": [70,80,98],
                "Musa": [55,60,99],
                "Ola": [75,66,50]

                }    
                
                
for name,grades in Students.items():
    total = sum(grades)
    print(f'Total for {name} is {total:.2f}')
    print(f'Average for {name} is {total/len(grades):.2f}')
    best_student = total/len(grades)
    
    if
    

    

