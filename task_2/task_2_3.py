val_list = []
for i in range(1, 101):
    if i % 15 == 0:
        val_list.append("FizzBuzz")
    elif i % 3 == 0:
        val_list.append("Fizz")
    elif i % 5 == 0:
        val_list.append("Buzz")
    else:
        val_list.append(str(i))
print(' '.join(val_list))
