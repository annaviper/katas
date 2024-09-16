"""
Given an array of integers, where all elements
but one occur twice, find the unique element.

Example:
a = [1, 2, 3, 4, 3, 2, 1]
The unique element is 4.
"""


def lonely_integer(array: list) -> int:
    count = {}

    for i in array:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1

    for i in count.keys():
        if count[i] == 1:
            return i


if __name__ == '__main__':
    a = [1, 2, 3, 4, 3, 2, 1]
    result = lonely_integer(a)
    print(result)
