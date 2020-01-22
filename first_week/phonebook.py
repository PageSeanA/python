# print(
#     """""
#     E-Phone Book
#     1. Look up an entry
#     2. Set an entry
#     3. Delete an entry
#     4. List all entries
#     5. Quit'
#     What do you want to do (1-5)?
#     """)

# electronic_phonebook = {}

# userAction = int(input("What do you want to do (1-5)?"):
# if menu_choice == 1:
#         print("What is the person'\s name?")


#         if menu_choice == 2: 
#             print input("What is the person'\s name & number?" )
#             for key value in electronic_phonebook.


#             if menu_choice == 3:
#                 print input("What is the person'\s name?")

#                 if menu_choice == 4: #go through all entries in the dictionary and print each out to the terminal.
#                     print()

#                     if menu_choice => 5:
#                         break



# import(electronic_phonebook)
# electronic_phonebook("name") = "Sean"
# print(electronic_phonebook)

# with open('data.pickle'. 'wb') as fh:
#     pickle.dump(electronic_phonebook, fh)

def print_menu():
    print('1. Look up an entry')
    print('2. Set an entry')
    print('3. Delete')
    print('4. List all entries')
    print('5. Quit')
    print('What do you want to do (1-5)?')

phonebook = {}
menu_choice = 0
print_menu()
while menu_choice != 5:
    menu_choice = int(input('Type in a number (1-5): '))
    if menu_choice == 1:



        print()
    elif menu_choice == 2:
        print("Set an entry")
        name = input("Name: ")
        phone = input("Number: ")
        numbers[name] = phone
    elif menu_choice == 3:
        print("Remove Name")
        name = input("Name: ")
        if name in numbers:
            del numbers[name]
        else:
            print(name, "was not found")
    elif menu_choice == 4:
        print("Lookup Number")
        name = input("Name: ")
        if name in numbers:
            print("The number is", numbers[name])
        else:
            print(name, "was not found")
    elif menu_choice != 5:
        print_menu()