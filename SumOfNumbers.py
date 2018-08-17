"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""


def is_sum_on_list(list_in: list, k: int) -> bool:
    while len(list_in) > 0:
        x = list_in.pop()
        if k - x in list_in:
            return True
    else:
        return False


if __name__ == '__main__':
    print(is_sum_on_list([10, 15, 3, 7], 17)) #True
    print(is_sum_on_list([10, 15, 3, 7], 10)) #True
    print(is_sum_on_list([10, 15, 3, 7], 14)) #False
