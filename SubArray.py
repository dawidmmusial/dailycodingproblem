"""
Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum values of each
subarray of length k.

For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:

    10 = max(10, 5, 2)
    7 = max(5, 2, 7)
    8 = max(2, 7, 8)
    8 = max(7, 8, 7)

Do this in O(n) time and O(k) space. You can modify the input array in-place and you do not need to store the results.
You can simply print them out as you compute them.
"""


def max_val_of_subarray(array: list, k: int) -> list:
    i = 0
    out = []
    len_array = len(array)

    while len_array >= i + k:
        out.append(max(array[i:i + k]))
        i += 1

    return out


if __name__ == '__main__':
    array = [10, 5, 2, 7, 8, 7]
    print(max_val_of_subarray(array, 2))
    print(max_val_of_subarray(array, 3))
    print(max_val_of_subarray(array, 4))
    print(max_val_of_subarray(array, 5))
