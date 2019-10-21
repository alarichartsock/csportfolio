# 3 - Devising an experiment that compares the performance of delete operators on Lists and Dictionaries

import time
from collections import defaultdict # Only way to automatically populate a dictionary is to import defaultdict.

#Setting up the List version

List = []
def set_up_list(O):
    for i in range(O):
        List.append(1)

set_up_list(10000000);

def time_decorator(fn):
    def func(x):
        start = time.time()
        x = fn(x)
        end = time.time()
        return x, end-start
    return func

#Setting up the dictionary version

dictionary = defaultdict(list)

def set_up_dictionary(O):
    for i in range(O):
        dictionary['example'].append(("example",1))

set_up_dictionary(1000000)

#Testing them both

@time_decorator
def TestListDelete(O):
    """Testing the big O of the List Index method"""
    List.__delitem__([O,1])
    return O

print(TestListDelete(100))
print(TestListDelete(1000))
print(TestListDelete(10000))
print(TestListDelete(100000))
print(TestListDelete(10000000))


@time_decorator
def TestDictionaryDelete(O):
    """Testing the big O of the List Index method"""
    dictionary.get(O)
    return O

print(TestDictionaryDelete(100))
print(TestDictionaryDelete(1000))
print(TestDictionaryDelete(10000))
print(TestDictionaryDelete(100000))
print(TestDictionaryDelete(1000000))