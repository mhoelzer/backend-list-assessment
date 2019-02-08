#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Additional basic list exercises

# D. Given a list of numbers, return a list where
# all adjacent == elements have been reduced to a single element,
# so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or
# modify the passed in list.
# Hint: Don't use `set()`


def remove_adjacent(nums):
    """remove adjacent because there can be only one... in a row"""
    unique = []
    for num in nums:
        if len(unique) == 0 or num != unique[-1]:
            # need the len of 0 b/c wont append if nothing is inside otherwise
            unique.append(num)
    return unique

    # result = []
    # result = [result.append(n) for n in nums if not result or n != result[-1]]
    # # list exists with othing in it, so dont need to check length
    # return result


# E. Given two lists sorted in increasing order, create and return a merged
# list of all the elements in sorted order. You may modify the passed in lists.
# The solution should work in "linear" time/making a single pass of both lists.
# Hint: Don't use `sort` or `sorted` -- they are not linear time.
# linear means merge lists one time through; one pass through list
# sorted looks in elements and sorts then keeps going all over list and not one time
def linear_merge(list1, list2):
    """sort w/o sort because we want to be together but want to be difficult"""
    list_sorted = []
    list_combo = list1 + list2
    while list_combo:
        alpha_top = min(list_combo)
        list_sorted.append(alpha_top)
        list_combo.pop(list_combo.index(alpha_top))
        # popping wants index
    return list_sorted

    # result = []
    # while list1 and list2:  # just chekcing for emptiness
    #     if list1[0] < list2[0]:
    #         # sorted in own ways
    #         result.append(list1.pop(0))
    #     else:
    #         result.append(list2.pop(0))
    # # result.extend(list1)
    # # # wont hurt if list1 is empty
    # # result.extend(list2)
    # # # wont hurt if list2 is empty
    # result.extend(list1 if list1 else list2)
    # return result


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


# Calls the above functions with interesting inputs.
def main():
    print('remove_adjacent')
    test(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
    test(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
    test(remove_adjacent([]), [])
    test(remove_adjacent([2, 2, 3, 3, 3, 4, 5, 2, 3]), [2, 3, 4, 5, 2, 3])

    print('linear_merge')
    test(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']),
         ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']),
         ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']),
         ['aa', 'aa', 'aa', 'bb', 'bb'])


# Standard boilerplate (python idiom) to call the main() function.
if __name__ == '__main__':
    main()
