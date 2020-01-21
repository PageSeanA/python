"""Medium

#1 Letter Summary Medium

Write a letter_histogram program that asks the user for input, 
and prints a dictionary containing the tally of how many times 
each letter in the alphabet was used in the word.""" 

user_input = input("Enter a word: ")

user_input = user_input.lower()   # convert input to lowercase

alphabet = 'abcdefghijklmnopqrstuvwxyz'

letter_count = {} # empty dictionary
for char in user_input:
    if char in alphabet:
        if char in letter_count:
            letter_count[char] = letter_count[char] + 1
        else:
            letter_count[char] = 1

keys = letter_count.keys()
for char in sorted(keys):
    print(char, letter_count[char])

"""#2 Word Summary
Write a word_histogram program that asks the user for a sentence as its input, 
and prints a dictionary containing the tally of how many times each word in 
the alphabet was used in the text."""

# user_input = input("Please enter a sentence: ")
# empty_dict = {}
# word_dump = ""
# for letter in user_input:
#     if letter == " "  or letter == ".":
#         if word_dump not in empty_dict:
#             empty_dict[word_dump] = 0
#             empty_dict[word_dump] += 1
#             word_dump = ""
#         else:
#             empty_dict[word_dump] += 1
#             word_dump = ""
#     else:
#         word_dump += letter
# print(empty_dict)

"""#3 Sorting a histogram
Given a histogram tally (one returned from either letter_histogram or 
word_histogram), print the top 3 words or letters. """

# user_input = input("Please enter a sentence: ")
# empty_dict = {}
# word_dump = ""
# for letter in user_input:
#     if letter == " "  or letter == ".":
#         if word_dump not in empty_dict:
#             empty_dict[word_dump] = 0
#             empty_dict[word_dump] += 1
#             word_dump = ""
#         else:
#             empty_dict[word_dump] += 1
#             word_dump = ""
#     else:
#         word_dump += letter
# for letter in range(len(empty_dict)):
#     print(word_dump, empty_dict[word_dump])

