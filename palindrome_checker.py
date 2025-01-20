# Challenge
# Check if a string is a palindrome

# 1. Get input from user
palindrome_input = input("Enter a word: ")

'''
    Function to check if a string is a palindrome
'''
def palindrome_checker(word):
    return word == word[::-1]

# 2. Print result
result = palindrome_checker(palindrome_input)
print(f"{palindrome_input} is {"a" if result else "not"} palindrome")