row = input("Input array:")
if row != '':
    array = [float(i) for i in row.split(' ')]
    print(max(array)-min(array))
else:
    print(0)
