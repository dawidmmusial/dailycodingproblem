"""
Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.
For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
You can modify the input array in-place.
"""


def lowest_pos_val(lst: list) -> int:
    # use set to remove duplicates
    pos_set = set(filter(lambda x: x > 0, sorted(lst)))

    if len(pos_set) == list(pos_set)[-1]:
        return list(pos_set)[-1]+1

    for i, v in enumerate(pos_set):
        if i + 1 != v:
            return i + 1


if __name__ == '__main__':
    arrs = ([3, 4, -1, 1], [1, 2, 0], [4, 2, 0, 3, 3])
    for arr in arrs:
        print(lowest_pos_val(arr))
 