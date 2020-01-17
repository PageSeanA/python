#Small
#***1. Madlib function
# Write a function that accepts two arguments: a name and a subject.

# Part I of problem.
# The function should return a String with the name and subject interpolated in.
# For example:
# madlib("Jenn", "science")
# # "Jenn's favorite subject is science."

# def noun(name, steam):
#     print(name + "favorite subject is " + steam + ".")
# noun("Jenn's ", "science")

#***Part II of problem.
# madlib("Jeff", "history")
# # "Jeff's favorite subject is history."
# Provide default arguments in case one or both are omitted.

def student(firstname = '(First name unknown)', lastname ='(who does not have a last name)', steam ='science'):
    print(firstname, lastname, 'favorite subject is ' + steam + '.') 

# 1 positional argument 
student('John',)  

# 2 positional argument                          
student('Jeff', 'Jackson\'s', 'History') 

# #***2. Celsius to Fahrenheit conversion
# The formula to convert a temperature from Celsius to Fahrenheit is:

# F = (C * 9/5) + 32

# Write a function that takes a temperature in Celsius, converts it Fahrenheit, and returns the value.

# #***3. Fahrenheit to Celsius conversion
# The formula to convert a temperature from Fahrenheit to Celsius is:

# C = (F - 32) * 5/9

# Write a function that takes a temperature in Fahrenheit, converts it to Celsius, and returns the value.

# #***4. is_even function
# Write a function that accepts a number as an argument and returns a Boolean value. Return True if the number is even; return False if it is not even.

# #***5. is_odd function
# Write an is_odd function that uses your is_even function to determine if a number is odd. (That is, do not do the calculation - call a function that does the calculation.)

# Hint: You'll use the not keyword.

# #***6. only_evens function
# Write a function that accepts a List of numbers as an argument.

# Return a new List that includes the only the even numbers.

# only_evens([11, 20, 42, 97, 23, 10])
# # Returns [20, 42, 10]
# Hint: use your is_even() function to determine which numbers to include in your new List.

# #***7. only_odds function
# Write a function that accepts a List of numbers as an argument.

# Return a new List that includes the only the odd numbers.

# only_odds([11, 20, 42, 97, 23, 10])
# # Returns [11, 97, 23]
# Hint: use your is_odd() function to determine which numbers to include in your new List.


#Medium
# ***1. Find the smallest number.
# Write a function smallest that accepts a List of numbers as an argument.

# It should return the smallest number in the List.

# numlist = [7, 8, 2, 10, 4, 22, 17, 100]

# print("The list smallest number is:", min(numlist))

# ***2. Find the largest number.
# Write a function largest that accepts a List of numbers as an argument.

# It should return the largest number in the List.

# numlist = [7, 8, 2, 10, 4, 22, 17, 100]

# print("The list smallest number is:", max(numlist))


# ***#3. Find the shortest String.
# Write a function shortest that accepts a List of Strings as an argument.

# It should return the shortest String in the List.

# strlist_short = ['hello', 'hi', 'hola', 'hey', 'howdy']  
# print("List of " + str(strlist_short)) 

# # used len() + argument + min() 
# list_short = len(min(strlist_short, key = len)) 
# print("The length of shortest string is " + str(list_short))

# ***4. Find the longest String.
# Write a function longest that accepts a List of Strings as an argument.

# It should return the longest String in the List.

# strlist_long = ['hello', 'hi', 'hola', 'hey', 'howdy']  
# print("List of " + str(strlist_long)) 

# # used len() + argument + max() 
# list_long = len(max(strlist_long, key = len)) 
# print("The length of longest string is " + str(list_long))
