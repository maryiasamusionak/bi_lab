# list
list1 = [1, 2, 3]

list2 = [a + b for a in 'abc' if a != 'c' for b in 'bcd' if b != 'a']
print(list1, list2)

# slice
sliced_list2 = list2[::2]
print(sliced_list2)

# list 3
list3 = [str(c) + 'a' for c in range(1, 5)]
print(list3)

# remove + print
print(list3.pop(1))

# add missing element back
list3.append('2a')
print(list3)
