"""
Your mission here is to create a function that gets an tuple and returns a tuple with 3 elements - first, third and second to the last for the given array
"""

row = input("Input array: ")
array = row.split(' ')
print("First element:", array[0], "\nThird element:", array[2], "\nPenultimate element:", array[len(array)-2])
