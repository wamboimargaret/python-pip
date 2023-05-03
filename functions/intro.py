# Write a Python function that takes two arguments (a and b) and returns their sum.
def addition(a,b):
    result = a + b
    return result

# Write a Python function that takes a string as input and returns the string reversed.
def reverse(str):
    reversed_string = str[::-1]
    return reversed_string

# Write a Python function that takes a list of integers as input and returns the sum of all the integers in the list.
def add_int(list):
    sum_of_int = 0
    for num in list:
        sum_of_int+=num
    return sum_of_int
# Write a Python function that takes a list of integers as input and returns a new list with all the even numbers removed.
def remove_even(numbers): 
    newlist = []
    for num in numbers:
        if num % 2 != 0:
            newlist.append(num)
    return newlist
        

# Write a Python function that takes a list of integers as input and returns the highest value in the list.
def highest_value(my_list):
    highest = sorted(my_list)
    return highest[-2]

# Write a Python function that takes a list of strings as input and returns a new list with all the strings capitalized.
def capital(names):
    newlist = []
    for name in names:
        result= name.capitalize()
        newlist.append(result)
    return newlist
       
    #    return [name.capitalize() for name in names]


    

    



