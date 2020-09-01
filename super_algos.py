import random

#element = ['a',100,'b',4,-5]
character_set = ['a','b']
n = 3

def find_min(element):
    for i in element:
        if type(i) != int:
            return -1
    if len(element) == 0:
        return -1
    elif len(element) == 1:
        return element[0]

    elif len(element) != 1:
        if element[0] < element[1]:
            del element[1]
            print(element)
            find_min(element)
        else:
            random.shuffle(element)
            print(element)
            find_min(element)
    return element[0]


def sum_all(element):
    for i in element:
        if type(i) != int:
            return -1
    if len(element) == 1:
        return element[0]
    if len(element) == 0:
        return -1
    else:
        element[0] += element[1]
        del element[1]
        print(element)
        sum_all(element)
    return element[0]


def find_possible_strings(character_set, n):
    if n = len(step):
        print(character_set)
    for i in range(n, len(character_set))

if __name__ == "__main__":
    find_possible_strings(character_set, n)