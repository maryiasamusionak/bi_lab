row = input("Input array: ")
array = [int(i) for i in row.split(' ')]
print(max(array)-min(array))
