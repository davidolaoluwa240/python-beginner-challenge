# Challenge
# Find the second largest number and remove duplicates from a list without set()

list = [22, 2, 3, 2, 4, 22, 4, 30, 5, 4, 1, 50, 1, 12, 10]

'''
    Function to get second largest value from a list
'''
def second_largest(list):
    return sorted(list)[-2]

'''
    Function to remove duplicates from a list
'''
def remove_duplicates(list):
    temp_list = []

    for item in list:
        if item not in temp_list: temp_list.append(item)

    return temp_list

print(f"Original list=({list})")

# 1. Result for second largest
result = second_largest(list)
print(f"Second largest=({result})")

# 2. Result for remove duplicates
result = remove_duplicates(list)
print(f"List without duplicates=({result})")
