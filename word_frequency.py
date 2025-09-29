#!/usr/bin/env python3

# Word frequency exercise
# TODO: (Read detailed instructions in the Readme file)
# 1. Prompt the user: Ask the user to enter a sentence.
# 2. Split the sentence
# 3. Create lists to store words and their corresponding frequencies.
# 4. Iterate through words and update frequencies

#!/usr/bin/env python3


import re   # we use 're' to check if the sentence is valid

# Checking the function if the user inputs a proper sentence 
def is_sentence(text):
    # checking if the input is a string and not empty
    if not isinstance(text, str) or not text.strip():
        return False
    # it checks if the first character is a capital letter
    if not text[0].isupper():
        return False
    # it checks if the sentence ends with punctuation (. ! or ?)
    if not re.search(r'[.!?]$', text):
        return False
    # it checks if it has at least one word
    if not re.search(r'\w+', text):
        return False
    return True   # if all checks are passed, it is a valid sentence

#  lets the user enter a sentence
user_sentence = input("Enter a sentence: ")

# if the sentence is not valid, keep asking again until it is correct
while not is_sentence(user_sentence):
    print("This does not meet the criteria for a sentence.")
    user_sentence = input("Enter a sentence: ")

# 2. split the sentence into words using split()
# for example: "Hello world." -> ["Hello", "world."]
words = user_sentence.split()

# 3. create two empty lists
unique_words = []    # this will store each word (only once)
frequencies = []     # this will store how many times the word appears

# 4. go through each word in the list
for word in words:
    # make the word lowercase so everything is the same
    # and remove punctuation at the end (like "." or ",")
    word = word.lower().strip(".,!?")

    # check if the word is already in the list unique_words
    if word in unique_words:
        # find the index of the word and increase its count by 1
        index = unique_words.index(word)
        frequencies[index] += 1
    else:
        # if the word is new, add it to unique_words
        # and start its frequency count at 1
        unique_words.append(word)
        frequencies.append(1)

# 5. print the results
# go through each word and print it with its frequency
for i in range(len(unique_words)):
    print(unique_words[i] + ":", frequencies[i])

