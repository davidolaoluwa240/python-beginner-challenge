# Challenge
# Count the number of vowels in a string

from re import *

# 1. Get input from user
vowel_input = input("Enter a text: ")

'''
    Function to count number of vowels in a text
'''
def vowel_counter(text):
    return len(findall("[aeiou]", text))

# 2. Print result
result = vowel_counter(vowel_input)
print(f"Total vowels=({result})")
