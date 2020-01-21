"""if and else conditions using the older way of formatting strings (none f'string)"""

# greeting = "Hello %s, it is very nice to meet you and your friend %s!"

# name_of_user = input("What is your name? ")
# length_of_name = len(name_of_user)
# if length_of_name > 0:
#     name_of_friend = input("What is your friend's name? ") 
#     print(greeting % (name_of_user, name_of_friend))
# else:
#     print("Ok, I'll ask again some other time.")

"""if, elff, else conditions using the older way of formatting strings (none f'string)"""

# greeting = "Hello %s, it is very nice to meet you and your friend %s!"
# greeting2 = "You have a really long name %s, but any friend of %s is a friend of mine!"

# name_of_user = input("What is your name? ")
# length_of_name = len(name_of_user)
# name_of_friend = input("What is your friend's name? ") 
# if length_of_name < 10:
#     print(greeting % (name_of_user, name_of_friend))
# elif length_of_name >= 10:
#     print(greeting2 % (name_of_user, name_of_friend))
# else:
#     print("Ok, I'll ask again some other time.")

"""if, elif, else with an interger"""

# age =int(input('Enter your age. '))
# if age >= 21:
#     print('You are an adult and can join the military, vote and drink if you like.')
# elif age >= 18:
#     print('You are able vote and join the military.')
# else:
#     print('You are not of age to vote or join the military')

"""while condition  """

# count = 0
# while count < 10:
#     count +=1
#     print("The count is", count)
# print("Done.")

"""While Loops: Checking Input"""

# answer = ''
# while answer != 'when':
#     answer = input('Say when to stop: ')
#     answer = answer.lower()
# print('Cheese!!! lol')

"""while break"""
# while True:
#     answer = input('Say when: ')
#     if answer.lower() == 'when' :
#         break
# print('Cheese!')

"""Tuesday Small Homework"""
#1.
# greeting = "Hello %s!"
# greeting2 = "I am sorry, if you don not want to tell me that is ok."
# name_of_user = input("What is your name? ")
# length_of_name = len(name_of_user)
# if length_of_name > 0:
#     print(greeting % (name_of_user))
# else:
#     print(greeting2)

#2
# name_of_user = input("What is your name? ")
# greeting = "Hello {0} your name {1} long!" .format((name_of_user), len(name_of_user))

# length_of_name = len(name_of_user)
# if length_of_name > 0:
#     print(greeting)

#3
# name_of_user = input('What is your name? ')
# length_of_name = len(name_of_user)
# subject = input('What is your subject? ')
# length_of_subject = len(subject)
# greeting = "{0}'s favorite subject in school is {1}." .format(name_of_user, subject)


# if length_of_name > 0 and length_of_subject > 0:
#     print(greeting)
# else:
#     print("I\'m sorry to have bother you with this question.")

#4

# day = int(input('Day (0-6)? '))
# if day == 0:
#     print('Sunday')
# if day == 1:
#     print('Monday')
# if day == 2:
#     print('Tuesday')
# if day == 3:
#     print('Wednesday')
# if day == 4:
#     print('Thursday')
# if day == 5:
#     print('Friday')
# if day == 6:
#     print('Saturday')

"""#3 Middle"""
# count = 0
# print("You have {} coins.".format(count))
# while True:
#     another = input("Do you want another? (yes/no) ")
#     if another == 'yes':
#         count += 1
#         print("You have {} coins.".format(count))
#     elif another == 'no':
#         print("Bye")
#         break
#     else:
#         print("Try again")

# print("You have 0 coins. Do you want another, yes or no?")
# answer = input("")
# count = 0
# while answer == "yes":
#     count += 1
#     print("You have", count)
#     answer = input("Do you want another? ")
# print("Bye")


# total_bill = float(input("Total bill amount? "))
# service = input("Level of service? ")
# good = float(0.20 * total_bill)
# fair = float(0.15 * total_bill)
# bad = float(0.10 * total_bill)
# good_bill = float(good + total_bill)
# fair_bill = float(fair + total_bill)
# bad_bill = float(bad + total_bill)
# if service == "good":
#     print("Tip amount: {:0.2f}".format(good))
#     print("Total amount: {:0.2f}".format(good_bill))
# elif service == "fair":
#     print("Tip amount: {:0.2f}".format(fair))
#     print("Total amount: {:0.2f}".format(fair_bill))
# elif service == "bad":
#     print("Tip amount: {:0.2f}".format(bad))
#     print("Total amount: {:0.2f}".format(bad_bill))

# import random

# name_of_user = input("What is your name? ")
# greeting = "Hello {0} your name {1} long!" .format((name_of_user), len(name_of_user))

# length_of_name = len(name_of_user)
# if length_of_name > 0:
#     print(greeting)

# for x in range(1,11): 
#     for y in range(1,11):
#         result = x * y 
#         print(str(x) + " " + "X "+str(y) + " = " + str(result))

# numbers = [1,2,3]
# numbers.append(4)
# print(numbers)

# todas = ["cat", "work", "shop"]
# todas = todas + ["show", "sleep"]

# count = 0
# while count < len(todas):
#     print(todas)
#     count +=1

todas = ["cat", "work", "shop"]
user_input = input('Add an item: ')

if user_input > 0:
    print(todas.append(""))