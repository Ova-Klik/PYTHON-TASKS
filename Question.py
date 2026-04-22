#1. Given a list numbers, write, a python function using map() that squares each number in the list
#    input = [1,2,3,4,5]
#    ouput = [1,4,9,16,25]
#
#
#2. Write a Python function that converts a list of strings to their corresonding lengths using the map() function.
#    words =["apples", "banana", "cherry"]
#    output:[5,6,6]
#
#3. Write a python function using filter() that returns a list of all the even numbers from a given list of integers.
#    numbers  = [1,2,3,4,5,6]
#    output:[2,4,6]
#    
#    
#4. Using filter(), create a python function that fiklters out all the words with more thatn 5 characters from the following list 
#    Samplle: words = ["apple","banana", "kiwi", "grapes","cherry"]
#    Output: ["banana", "grapes", "cherry"]
#
#5. Using reduce(), write a python function to concatenate all the Strings, in a list into a single string adding hyphen inbtween each string.
#
#    words = ["I","love","python","Snacks"]
#    output = "I-Love-python-Snacks"
#--------------------------------------------------------
from functools import reduce

numbers = [1,2,3,4,5]

def square_of_elements(element):

    return element**2
    
print(list(map(square_of_elements,numbers)))


#--------------------------------------------------------
words =["apple", "banana", "cherry"]

def get_string_length(element):

        return len(element)
    
print(list(map(get_string_length,words)))


#--------------------------------------------------------

numbers  = [1,2,3,4,5,6]

def get_list_of_even_numbers(element):

        return element%2==0
    
list_of_even_numbers = list(filter(get_list_of_even_numbers,numbers))

print(list_of_even_numbers)


#--------------------------------------------------------

words = ["apple","banana", "kiwi", "grapes","cherry"]

def get_words_of_length_greater_than_5(element):

        return len(element)>5
    
words_with_length_greater_than_five = list(filter(get_words_of_length_greater_than_5,words))

print(words_with_length_greater_than_five)

#--------------------------------------------------------

words = ["I","love","python","Snacks"]

def concatenated_strings(accumulator,element):
    
        return accumulator + "-" + element 
    
concatenated_strings = reduce(concatenated_strings,words)

print(concatenated_strings)

#---------------------------
def concat_word(element):

    print(reduce(lambda x, y: f"{x}-{y}", element))
    
concat_word(words)


#---------------------------

numbers = ["1","2","3","4","5"]

def get_integer_value(element):

    return int(element)
    
print(list(map(get_integer_value,numbers)))

#---------------------------

numbers = [0,5,10,15]

def get_integer_value(element):

    return element + 10
    
print(list(map(get_integer_value,numbers)))




numbers = [0,20,27,100]

def get_integer_value(element):

    return ((element*9/5) + 32)
    
print(list(map(get_integer_value,numbers)))



numbers = [0,20,27,100]

def convert_to_fahrenheit(element):

    return ((element*9/5) + 32)
    
print(list(map(convert_to_fahrenheit,numbers)))

#---------------------------

numbers = [1,None,3,None,5]

def remove_none(element):

    return element!=None
    
print(list(filter(remove_none,numbers)))


numbers = [1,3,4,6,9,12]

def get_odd_elements(element):

    return element%3==0
    
print(list(filter(remove_none,numbers)))



numbers = [-2,-1,0,1,2]

def get_positive_elements(element):

    return element>0
    
print(list(filter(get_positive_elements,numbers)))



#___________________________________________

numbers = [2,3,4]

def get_product(accumulator,element):

    return accumulator*element

product = reduce(get_product,numbers)
print(product)



numbers = [3,7,2,9,1]

def get_maximum_value(accumulator,element):
    
    
    return accumulator if accumulator>element else element

maximum = reduce(get_maximum_value,numbers)
print(maximum)


words = ["Hello","","World"]

def concatenate_words(accumulator,element):
    
    
    return accumulator + element

concatenated_words = reduce(concatenate_words,words)
print(concatenated_words)


board = []
number=0

board=[[number:=number+1 for column in range(3)] for row in range(3)]

print(board)



