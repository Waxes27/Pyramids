import random

#element = ['a',100,'b',4,-5]
# character_set = ['a','b','C']
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
    for x in character_set:
        if type(x) != str or "" in character_set:
            return []
    list_ = []
    prefix = ""
    permutation(character_set, n, list_,prefix)
    return list_

def permutation(character_set, n, list_, prefix):
    if n == 0:
        list_.append(prefix)
        return list_
    for i in character_set:
        new_prefix = prefix + i
        permutation(character_set,n-1, list_, new_prefix)

    
if __name__ == "__main__":
    print(find_possible_strings(character_set, n))