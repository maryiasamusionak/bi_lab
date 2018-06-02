def count_characters(count_me_string):
    dict2 = dict.fromkeys(count_me_string, 0)
    for i in count_me_string:
        dict2[i] += 1
    return dict2


def fizzbuzz(num=10):
    val_list = []
    for i in range(1, num + 1):
        if i % 15 == 0:
            val_list.append("FizzBuzz")
        elif i % 3 == 0:
            val_list.append("Fizz")
        elif i % 5 == 0:
            val_list.append("Buzz")
        else:
            val_list.append(str(i))
    return val_list


def poly(word='wow'):
    word = str(word)
    return word == word[::-1]
