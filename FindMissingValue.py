"""
Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.
For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
You can modify the input array in-place.
"""


def lowest_pos_val(lst: list) -> int:
    # add 0 prevent indexing issue
    lst.append(0)
    # use set to remove duplicates, sort and put negative numbers at the end
    pos_set = set(lst)

    for i, v in enumerate(pos_set):
        if i != v:
            return i
    else:
        return len(lst) - 1


if __name__ == '__main__':
    arrs = ([3, 4, -1, 1], [1, 2, 0], [4, 2, 0, 3, 3])
    for arr in arrs:
        print(lowest_pos_val(arr))
