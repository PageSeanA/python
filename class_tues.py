"""#Objects 102, Powerpoint from Week 1, Tuesday"""


# class Greeting:
#     def say_hello(self):
#         print('hello')

# newGreetingObj = Greeting()

# newGreetingObj1.say_hello()

# class Student:
#     def say_goodmorning(self):
#         print('good morning')

# Alina = Student()              #ObjectName = ClassName()
# Alina.say_goodmorning()

# Sean = Student()
# Sean.say_goodmorning()

# Alex = Student()
# Alex.say_goodmorning()




# class Student:

# def __init__(self):
#     print('constructor called')

# def say_goodmorning(self):
#      print('good morning')

# Alina = Student()              #ObjectName = ClassName()
# # Alina.say_goodmorning()

# Sean = Student()
# # Sean.say_goodmorning()

# Alex = Student()
# # Alex.say_goodmorning()

# # class Animal:
# #     def __init__ (self, name):
# #     self.name = name
# # class Dog (Animal):
# #     def woof (self):
# #     print("Woof")
# # # class Cat (Animal):
# #     def meow (self):
# #     print("Meow")

# # class Animal:
# #     def __init__ (self, name):
# #         self.name = name
# # dog = Animal('dog')
# # cat = Animal('cat')
# # horse = Animal('horse')
# # print(dog.name)
# # print(cat.name)
# # print(horse.name)

# name = 'alina'
# lname = 'belova'

# class Student:
#     def __init__(self, name, lname):
#         self.name = name
#         self.lname = lname
#         print(f'Hello there {self.name} {self.lname}')
    
#     alina = Student('alina', 'belova')
#     sean = Student('sean', 'page')

# import datetime

# class Person:
#     def __init__(self, fname, lname, birthdate, address, email):
#         self.fname = fname
#         self.lname = lname
#         self.birthdate = birthdate
#         self.address = address
#         self.email = email
        
#     def age(self):
#         today = datetime.date.today()
#         age = today.year - self.birthdate.year

#         if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
#             age -= 1

#         return age


# sammy = Person('Sammy', 'Kry', datetime.date(1998, 8, 21), '123 sesame street', 'sammy@gmail.com')

# print(f'{sammy.fname} {sammy.lname}')

# age = sammy.age()

# print(age)

"""example"""

# def greeting(name):
#     count = 0 #
#     print(f"hello {name}")
#     count += 1

# greeting("Daniela")
# greeting("Alex")
# greeting("John")
# greeting("Meryem")


"""Class Example 29/53"""
# class Person:
#     def __init__(self, name, email, phone):
#         self.name = name
#         self.email = email
#         self.phone = phone

#     def greet(self, other_person):
#         print(f'hello {other_person.name}. I am {self.name}!')

# Sonny = Person('Sonny', 'sonny@hotmail.com', 483-485-4948) #Sonny and Jordan are objects.
# Jordan = Person('Jordan', 'jordan@aol.com', 495-586-3456) #Created an object called Jordan of the person type. You'll pass an arguemnt to the parameters.
# Sonny.greet(Jordan)

"""Example"""

# class Person:

#     def __init__(self, name):
#         self.name = name
#         self.count = 0

#     def greet (self):
#         self._greet()
#     def _greet (self):
#         self.count += 1
#         if self.count > 1:
#             print("Stop being so nice")
#             self.__reset_count()
#         else:
#             print("Hello", self.name)
#     def __reset_count(self):
#         self.count = 0

# alex = Person('Alex')
# alex.greet()

# class Person:
#     def __init__(self, fname, lname, birthdate, address, email):
#         self.fname = fname
#         self.lname = lname
#         self.birthdate = birthdate
#         self.address = address
#         self.email = email
        
#     def age(self):
#         today = datetime.date.today()
#         age = today.year - self.birthdate.year

#         if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
#             age -= 1

#         return age
# """Creating a new Python String Methods. Created a Reverse String""" #33/53 Inheritance

# class VString(str):
    
#     def reverse(self, name):

#         rstring = "" #empty string

#         for char in name:  #char means character
#             rstring = char + rstring

#         return rstring

# myString = VString("hello")

# print(myString.capitalize())

# reversed = myString.reverse("hello") #pass in the stream

# print(reversed)
# """Implicit Inheritance 35/53"""
# class Parent(object):
#     def implicit(self):
#         print("PARENT implicit()")

# class Child(Parent):
#     pass
# dad = Parent()
# dad.implicit()

# son = Child()
# son.implicit()

"""Override Explicitly 35/53"""

"""Implicit Inheritance 36/53, Need to do, didin't have time in class."""
# class Parent(object):
#     def implicit(self):
#         print("PARENT implicit()")

# class Child(Parent):
#     pass
# dad = Parent()
# dad.implicit()

# son = Child()
# son.implicit()

"""Using super() with int 39/53"""

# class Character:
#     def __init__(self, name, power, health):
#         self.name = name 
#         self.power = power 
#         self.health = health
    

# class Hero(Character):
#     def __init__(self, weapon, name, power, health):
#         self.weapon = weapon
#         super(Hero, self).__init__(name, power, health)

# alina = Hero('pink gun', 'alina', 3, 10)

# print(alina.weapon)


"""Class Project 40/53"""

#Start Make your own class
# class Vehicle:   #4053
#     def __init__(self, make, model, year):
#         self.make = make 
#         self.model = model 
#         self.year = year
    

"""Ignore for Class Project 40/53 # class Hero(Character):
#     def __init__(self, weapon, name, power, health):
#         self.weapon = weapon
#         super(Hero, self).__init__(name, power, health)"""

# car = Vehicle('Nissan', 'Leaf', 2015)

# print(car.make)
# print(car.model)
# print(car.year)

#End Make your own class

# #Start of Add a method 2, 41/53
# class Person:
#     def __init__(self, name, email, phone, friends):
#         self.name = name
#         self.email = email
#         self.phone = phone   # def greet(self, ):
#     #     print(f'hello {other_person.name}. I am {self.name},!')

#     def print_contact_info(self):
#         print(f'{self.name}\'s contact info: {self.email}, {self.phone}.', vars(el))

# Sonny = Person('Sonny', 'sonny@hotmail.com', 483-485-4948, 'Jordan') #Sonny and Jordan are objects.

# Jordan = Person('Jordan', 'jordan@aol.com', 495-586-3456, 'Sonny') #Created an object called Jordan of the person type. You'll pass an arguemnt to the parameters.
# # Sonny.greet(Jordan)
# el = Person()
# Sonny.friends.append(Jordan) 
# Sonny.print_contact_info()

# Jordan.friends.append(Sonny)
# Jordan.print_contact_info()

# print dir(el)

# #len(jordan.friends) ?

# #https://www.geeksforgeeks.org/class-instance-attributes-python/ example I used but have questions about.

# #42/53

class Person:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.greeting_count = 0
        self.unique_greeted = []

    def greet(self, other_person):
        print('Hello {}, I am {}!'.format(other_person.name, self.name))
        self.greeting_count += 1
        self.unique_greeted.append(other_person.name)

    def print_contact_info(self):
        print(f"{self.name}'s email: {self.email}, {self.name}'s phone number: {self.phone}")

    def add_friend(self, friend):
        self.friends.append(friend.name)

    def num_of_friends(self):
        print(len(self.friends))

    def __str__(self):
        return 'Person: Name - {}, Email - {}, Phone - {}'.format(self.name, self.email, self.phone)

    def num_unique_people_greeted(self):
        uniques = set(self.unique_greeted)
        uniques_greeted = list(uniques)
        print(len(uniques_greeted))

    # 1
    sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948')

    # 2
    jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456')

    # 3
    sonny.greet(jordan)
    sonny.greet(jordan)
    sonny.greet(jordan)

    # 4
    jordan.greet(sonny)
    bill = Person('Bill', 'bob@yahoo.com', '236-897-9001')
    jordan.greet(bill)

    # 5
    #print(f"{sonny.name}: Email - {sonny.email}; Phone - {sonny.phone}")
    sonny.print_contact_info()

    # 6
    #print(f"{jordan.name}: Email - {jordan.email}; Phone - {jordan.phone}")
    jordan.print_contact_info()

    # Add a friend
    sonny.add_friend(jordan)
    jordan.add_friend(sonny)
    jordan.add_friend(bill)
    #print(sonny.friends)
    #print(jordan.friends)

    # Count number of friends
    sonny.num_of_friends()
    jordan.num_of_friends()

    # Count number of greetings
    print(sonny.greeting_count)
    print(jordan.greeting_count)

    # Convert object to string
    print(sonny)
    print(jordan)

    # Number of unique people greeted
    sonny.num_unique_people_greeted()
    jordan.num_unique_people_greeted()

class Person:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.greeting_count = 0
        self.unique_greeted = []

    def greet(self, other_person):
        print('Hello {}, I am {}!'.format(other_person.name, self.name))
        self.greeting_count += 1
        self.unique_greeted.append(other_person.name)

    def print_contact_info(self):
        print(f"{self.name}'s email: {self.email}, {self.name}'s phone number: {self.phone}")

    def add_friend(self, friend):
        self.friends.append(friend.name)

    def num_of_friends(self):
        print(len(self.friends))

    def __str__(self):
        return 'Person: Name - {}, Email - {}, Phone - {}'.format(self.name, self.email, self.phone)

    def num_unique_people_greeted(self):
        uniques = set(self.unique_greeted)
        uniques_greeted = list(uniques)
        print(len(uniques_greeted))

    # 1
    sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948')

    # 2
    jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456')

    # 3
    sonny.greet(jordan)
    sonny.greet(jordan)
    sonny.greet(jordan)

    # 4
    jordan.greet(sonny)
    bill = Person('Bill', 'bob@yahoo.com', '236-897-9001')
    jordan.greet(bill)

    # 5
    #print(f"{sonny.name}: Email - {sonny.email}; Phone - {sonny.phone}")
    sonny.print_contact_info()

    # 6
    #print(f"{jordan.name}: Email - {jordan.email}; Phone - {jordan.phone}")
    jordan.print_contact_info()

    # Add a friend
    sonny.add_friend(jordan)
    jordan.add_friend(sonny)
    jordan.add_friend(bill)
    #print(sonny.friends)
    #print(jordan.friends)

    # Count number of friends
    sonny.num_of_friends()
    jordan.num_of_friends()

    # Count number of greetings
    print(sonny.greeting_count)
    print(jordan.greeting_count)

    # Convert object to string
    print(sonny)
    print(jordan)

    # Number of unique people greeted
    sonny.num_unique_people_greeted()
    jordan.num_unique_people_greeted()