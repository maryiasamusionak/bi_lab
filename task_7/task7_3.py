def div_by_zero(num):
    try:
        quo = num / 0
        return quo
    except ZeroDivisionError as div:
        for err in div.args:
            print(err)


div_by_zero(5)


def print_list_element(thelist, index):
    try:
        print(thelist[index])
    except IndexError:
        print('Error, element is out of bounds')


print_list_element([1, 2, 3], 4)


def add_to_list_in_dict(thedict, listname, element):
    try:
        l = thedict[listname]
        print("%s already has %d elements." % (listname, len(l)))
    except KeyError:
        thedict[listname] = []
        print("Created %s." % listname)
    finally:
        thedict[listname].append(element)
        print("Added %s to %s." % (element, listname))


dict_1 = {"first": [1, 2, 3, 4], "second": [3, 2, 1]}
add_to_list_in_dict(dict_1, "third", 0)
add_to_list_in_dict(dict_1, "first", 5)
