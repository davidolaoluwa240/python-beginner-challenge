# Challenge
# Create a calculator app that perform basic math operation

msg = '''
=============================================
================Welcome Guest================
      Please select -
      1. Add
      2. Subtract
      3. Multiply
      4. Divide
      5. Remainder
      6. Exponential
=============================================
=============================================
'''

'''
      Function to add two numbers
'''
def add(a, b):
    return a + b

'''
      Function to subtract two numbers
'''
def subtract(a, b):
    return a - b

'''
      Function to divide two numbers
'''
def divide(a, b):
    return a / b

'''
      Function to multiply two numbers
'''
def multiply(a, b):
      return a * b

'''
      Function to get remainder
'''
def remainder(a, b):
     return a % b

'''
      Function to calculate exponential
'''
def exponential(a, b):
     return a**b

calculate_map = {
      1: add,
      2: subtract,
      3: multiply,
      4: divide,
      5: remainder,
      6: exponential
}

should_continue = True

while should_continue is True:
      print(msg)

      a = float(input("Enter first number: "))
      op = int(input("Select operator eg 1-6: "))
      b = float(input("Enter second number: "))

      # Validate operator input
      if op not in range(1, 7):
         print('Error: Invalid operator, try again')
         continue

      result = calculate_map[op](a, b)

      print('Your result=({0})'.format(int(result) if result.is_integer() else result))

      continue_calc = input("Continue (y/n): ")

      if continue_calc != 'y':
           should_continue = False
           print("Exiting....")