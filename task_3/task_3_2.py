# tuple from list
list1 = ['a', 'b', 'c']
tuple1 = tuple(list1)
print(tuple1)

# list from tuple
tuple2 = ('a', 'b', 'c')
list2 = list(tuple2)
print(list2)

# ['a', 2, 'gamma'] var1
for i in range(0, len(list2)):
    if str(list2[i]) == 'a':
        list2[i] = 'a'
    elif str(list2[i]) == 'b':
        list2[i] = 2
    elif str(list2[i]) == 'c':
        list2[i] = 'gamma'
tuple2 = tuple(list2)
print(tuple2)

# ['a', 2, 'gamma'] var2
a, b, c = tuple('a'), tuple('2'), tuple('gamma')
print(type(a), type(b), type(c))


def tuple_function(**kwargs):
    print(kwargs)


tuple_function(a='a', b='2', c='gamma')

# length
tuple3 = (['a', 'b', 'c'], )
print(len(tuple3))
