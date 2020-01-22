"""#Dictionaries 06:11

#Step 2, Start
#This creates a funtiction that allows the program to cycling through the dict after they click no looking at the data that the user inputed.
In this example, the fuction outputs an introduction for the ninjas."""

#def stands for define. In this example fuction is being called ninja_intro. Fyi (dictionary) will be nijia_belts = {}
def ninja_intro(dictionary): 
    for key, val in dictionary.items():
        print(f'I am {key} and I am a {val}') #for key, val in dictionalry.items() 
                                            #(This gives the key and the value each time it cycling through the dict. 
                                            # #The .items part gets the items located in the dict.

#Step 2, Ends

#Step 1, Start
ninja_belts = {}

while True: #creates an infinite loop.
    ninja_name = input('enter a ninja name: ') #Getting users input. ninja_name is the KEY for the dict.)
    ninja_belt = input('enter a belt color: ') #ninja_belt is the VALUE for the dict.
    ninja_belts[ninja_name] = ninja_belt #Here I added the key value pair to the dictionary.

    another = input('add another belt? (y/n)')
    if another == 'y': #checking to see if the user inputed a yes or no.
        continue #if they enter yes, the user goes back to the top of the loop to input more blets
    else:
        break #breaks infinite loop. If the user inputs anthing
#Step 1, Ends

"""Step 3, Starts

Calling the fuction
"""
ninja_intro(ninja_belts)