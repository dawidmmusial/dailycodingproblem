"""
Given a list of integers, write a function that returns the largest sum of non-adjacent numbers.
Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10,
since we pick 5 and 5.
"""


def sum_of_numbers(lst: list) -> int:
    # assuming that the largest multiple of the list will be 13
    run = [2, 3, 5, 7, 11, 13]
    out = lst[0]

    # two last value of the list doesn't meet the condition
    for i in range(len(lst)-2):
        for r in run:
            # choose slice of the list
            if len(lst[i::r]) < 2:
                break
            sum_list = sum(lst[i::r])
            # save greatest value
            if out < sum_list:
                out = sum_list

    return out


if __name__ == '__main__':
    lst = [2, 4, 6, 2, 5]
    print(sum_of_numbers(lst))