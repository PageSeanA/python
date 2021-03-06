

#CLASSWORK Examples

#loops
# students = ["Matt", "Foorkhan", "Alex", "Mary"]
# for variable in students:
#     print(variable)

#nested loops
# days = ['Mon', 'Tues', 'Wed', 'Thus', 'Fri']
# weeks = ['week_1', 'week_2', 'week_3']

# for week in range(0,len(weeks)):
#     print(weeks[week])
#     for day in range(0,len(days)):
#         print(days[day])

#nested loops classwork
# days = ['Mon', 'Tues', 'Wed', 'Thus', 'Fri']
# weeks = ['week_1', 'week_2', 'week_3']

# for week in weeks:
#     print(f'{week}')
#     for day in days:
#         print(f'\t {day}')
        
#HOMEWORK
# 1. Multiply Vectors - Given two lists of numbers of the same lenght, creat a new list by
#  multiplying the pairs of number in correspoinding postions in the two list. Example:
#[2,4,5] x [2,3,6] = [4,12,30]

# a = [2,4,5] x [2,3,6] = [4,12,30]


#2. Matrix Additon - Given two two-dimensional lists of numbers of the size 2x2 two 
# dimensional list is represented as an list of lists:
#[[2,-2],
#[5,3]]



#Calculate the result of adding the two matrices. The number in each position in the
#  resulting matrix should be the sum of the numbers in the corresponding addend matrices. 
# Example: to add
#1 3
#2 4
#and
#5 2
#1 0
#results in
#6 5
#3 4

#3. Matrix Additon II
#Use your solution in Matrix Addition, and extend it to work for a pair of matrices of any
# size, as long as they have the same size.



#4. De-dup
# Given a list of numbers or strings, create a new list containing the same elements as 
# the first list, except with any duplicate values removed. Print the list.



# #5. Leetspeak
# Given a paragraph of text as a String, print the paragraph in leetspeak.
leet = {'A': '4','E': '3','G': '6','I': '1','O': '0','T': '7','S': '5'}
para = ("I pledge allegiance to the Flag of the United States of America, and to the Republic for which it stands, one Nation under God, indivisible, with liberty and justice for all.")
para = para.upper()
for i, j in leet.items():
    para = para.replace(i, j)
print (para)




# To translate a String to leetspeak, you need to replace make the following character 
# replacements (treat all input characters as uppercase):

# Letter	Translates To
# A	4
# E	3
# G	6
# I	1
# O	0
# S	5
# T	7
# Example: If your program is given the String "I am a leet programmer", it 
# should print "1 4m 4 l337 pr0gr4mm3r" as the leetspeak translation


# #6. Long-long Vowels
# Given a word as a string, print the result of extending any long vowels to the 
# length of 5.

# Examples:
# Good => Goooood 
# Cheese => Cheeeeese 
# Man => Man 
# Spoon => Spooooon

#7. Caesar Cipher
# Given a string, print the Caesar Cipher (or ROT13) of that string. What is Caesar Cipher?
# Use your solution to decipher the following text: 
# "lbh zhfg hayrnea jung lbh unir yrnearq"


