# Write a Python function that returns the Nth Fibonacci number.
def fibonacci(n):
    a =0
    b = 1
    if n ==1:
        print(a)
    else:
        print(a)
        print(b)    
        for i in range(2,n):
            c = a+b
            a = b
            b = c
            print(c)
# Write a Python function that takes a list of numbers and returns the sum of all even numbers in the list.
def even_numbers(nums):
    sum =0
    for i in nums:
      if(i % 2  ==0):
        sum+=i
    return sum

# Write a Python function that takes a string and returns the reverse of the string.
def rerverse(str):
    reversed = str[::-1]
    return reversed

# Write a Python function that takes a list of strings and returns the longest string in the list.
def longest(string):
    max_val = -1
    for str in string:
       if len(str) > max_val:
          max_val = len(str)
          word = str
    return word   

# Write a Python function that takes a list of integers and returns the second largest number in the list.
def second_largest(integers):
   sorted_list= sorted(integers)
   return sorted_list[-2]


# Write a Python function that takes two strings and returns True if they are anagrams, False otherwise.
def anagram(a,b):
   word = a.lower()
   word2 = b.lower()

   if len(word)== len(word2):
      sorted_word = sorted(word)
      sorted_word2 = sorted(word2)

      if sorted_word == sorted_word2:
         return ("True")
   else :
         return("False")
   
   

# Write a Python function that takes a string and returns True if the string is a palindrome, False otherwise.
def palindrome(a):
   if a[::-1]==a:
      return ("True")
   else:
      return ("False") 
    


