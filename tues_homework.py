class Person:  #class is the keyword.
    def __init__(self, name, email, phone): #Defintion of the constructor. A constructor method gets involed as soon as the object is called.
        self.name = name #These are examples of instance variables. They go inside the constructor method.
        self.email = email
        self.phone = phone
        self.friends = []
        self.greeting_count = 0
        self.unique_greeted = []

    def greet(self, other_person): #Method called greet. The other_person part is the parameter.
        print('Hello {}, I am {}!'.format(other_person.name, self.name)) #this could have been don in an f'string as well. Ex. print('Hello {other_person.name}, I am {})
        self.greeting_count += 1
        self.unique_greeted.append(other_person.name)

    def print_contact_info(self):  #Add a method 2. Go back to the Person class. Add a print_contact_info method to the Person class that will print out the contact info for a object instance of Person. 

        print(f"{self.name}'s email: {self.email}, {self.name}'s phone number: {self.phone}")

    def add_friend(self, friend): #Add an instance variable (attribute). Add a friends instance variable (attribute) to the Person class. You will initialize it to an empty list within the constructor __init__. Once you've done this you should be able to add a friend to a person using the list's append method.
        self.friends.append(friend.name)    #This examples states sonny.friends.append(jordan.name)

    def num_of_friends(self):
        print(len(self.friends))

    def __str__(self):
        return 'Person: Name - {}, Email - {}, Phone - {}'.format(self.name, self.email, self.phone)

    def num_unique_people_greeted(self):
        uniques = set(self.unique_greeted)
        uniques_greeted = list(uniques)
        print(len(uniques_greeted))

    # 1. Instantiate an instance object of Person with name of 'Sonny', email of 'sonny@hotmail.com', and phone of '483-485-4948', store it in the variable sonny.
#sonny is the object. Person is the type. The parts in the () is "passed in."
sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948')  

    # 2. Instantiate another person with the name of 'Jordan', email of 'jordan@aol.com', and phone of '495-586-3456', store it in the variable 'jordan'.

jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456') #in this example, jordan is the object.

    # 3 Have Sonny greet jordan using the greet method.

sonny.greet(jordan) #This data that is being passed in comes from the def greet(self, other_person):
sonny.greet(jordan) #The breakdown of this is object.mode()
sonny.greet(jordan)

    # 4.Have Jordan greet jordan using the greet method.

jordan.greet(sonny)
sean = Person('Sean', 'sean_slightly_confused@yahoo.com', '333-333-3333') #in this example, sean is the object.
jordan.greet(sean)

    # 5. Write a print statement to print the contact info (email and phone) of Sonny.

    #print(f"{sonny.name}: Email - {sonny.email}; Phone - {sonny.phone}") These are how the objects are going to print at def print_contact_into(self)'s print command.
sonny.print_contact_info()

    # 6. Write another print statement to print the contact info of Jordan. These are how the objects are going to print at def print_contact_into(self)'s print command.

    #print(f"{jordan.name}: Email - {jordan.email}; Phone - {jordan.phone}")
jordan.print_contact_info()

    # Add a num_friends method. Similarly, to get the number of friends a person has, we'd like to hide the implementation detail that there is a friends attribute which is a list. Implement a num_friends method which returns the number of friends the person currently has.
sonny.add_friend(jordan)
jordan.add_friend(sonny)
jordan.add_friend(sean)
    #print(sonny.friends)
    #print(jordan.friends)

    # Add a num_friends method. Similarly, to get the number of friends a person has, we'd like to hide the implementation detail that there is a friends attribute which is a list. Implement a num_friends method which returns the number of friends the person currently has.
sonny.num_of_friends()
jordan.num_of_friends()

    # Count number of greetings. We want to count the number of times a person has greeted someone. To do this, we'll add another attribute, call it say greeting_count, and initialize it to 0. Then each time the greet method is called, we'll increment greeting_count by 1.

print(sonny.greeting_count)
print(jordan.greeting_count)

    # Convert object to string
print(sonny)
print(jordan)

    # Bouns Problem. Keep track of the number of unique people a person has greeted, and be able to report that number via the num_unique_people_greeted method:

sonny.num_unique_people_greeted()
jordan.num_unique_people_greeted()