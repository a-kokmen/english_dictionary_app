# English Dictionary Application

# Import necessary modules 
import json
from difflib import get_close_matches
# get_close_matches(string, [strings], cutoff = [0:1])
# returns the most simmilar strings as list of strings to the string with the ratio of cutoff in decscending order   

# Opem data.json file content and store it in data
data = json.load(open("data.json"))

# Argument = a word from the user
# Return value = messages to the user
# Function to define a word if there is one
def define(word):
    word = word.lower() # Lowercase all letters of the entered word
    # if word exists in data return the values as a list
    if word in data:
        return data[word]
    # if word has a specific meaning as capitilied in data return that value as a list
    elif word.title() in data:
        return data[word.title()]
    # if word has a specific meaning in uppercase in data return that value as a list
    elif word.upper() in data:
        return data[word.upper()]
    # if the length of the list greater than 0 get a user input and store it in answer
    elif len(get_close_matches(word, data.keys(), cutoff = 0.5)) > 0:
        answer = input("\nDid you mean %s instead? If so please enter 'yes' or 'no': " % get_close_matches(word, data.keys(), cutoff = 0.5)[0])
        # if lowercase answer is "yes" return first element of the list
        if answer.lower() == "yes":
            return data[get_close_matches(word, data.keys(), cutoff = 0.5)[0]]
        # if lowercase answer is "no" return message 
        elif answer.lower() == "no":
            return "\nThan go fuck yourself bitch!"
        # if neither return message
        else:
            return "\nAre you a retard man? Answer it correctly you assbut!"
    # if the word doe not exists in the dictionary return a message    
    else:
        return "\nThe word you entered doesn't exist. Please double check it."

while True:
    # get user input and store it into word
    word = input("\nEnter word: ")
    # if word is not "/end/" continue
    if word != "/end/":
        # Call the define() function with word as an argument and store it into definitions
        definitions = define(word)
        # if definition is a list 
        if type(definitions) == list:
            i = 1
            # print all list items in a orderly way
            for meanings in definitions:
                print("\n" + str(i) + " - " + meanings)
                i = i + 1
        # if definition is not a list print the string
        else:
            print(definitions)
    else:
        print("\nBye Bye")
        break