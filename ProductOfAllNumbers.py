"""
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""
from functools import reduce
from operator import truediv

def product_of_array(arr: list) -> list:
    sum_array = reduce(lambda x, y: x * y, arr)
    product = [sum_array//x for x in arr]
    return product


if __name__ == '__main__':
    print(product_of_array([1, 2, 3]))
    # print(product_of_array([3, 2, 1]))
    print(product_of_array([1, 2, 3, 4, 5]))
