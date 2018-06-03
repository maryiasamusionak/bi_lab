import re


def email(string_1):
    return re.findall(r'[\w|\-|_]*[@][a-zA-Z]*[\.][a-zA-Z]*', string_1)


print(email('Maryia_Samusionak@epam.com jufdg  marysamus7@gmail.com'))


def characters(string_2):
    return re.findall(r"\b\w{3,5}\b", string_2)


print(characters('Maryia_Samusionak@epam.com jufdg jfdr '
                 'i;ter marysamus7@gmail.com'))


def numbers(string_3):
    return print(re.findall(r"\d", string_3))


numbers('Maryia_Samusionak@epam.56com jufdg'
        ' tuyj66jfdr i;ter marysamus7@gmail.com')

string_4 = 'Soft kitty, warm kitty\nLittle ball of fur.'
string_5 = 'Lazy_kitty,_pretty_kitty\nPurr,_purr,_purr.'


def underscores(string):
    string = re.sub(r' ', "_", string)
    return string


print(underscores(string_4))


def whitespaces(string):
    string = re.sub(r'_', " ", string)
    return string


print(underscores(string_4))
print(whitespaces(string_5))
print()
print(whitespaces(string_4))
print(underscores(string_5))
