"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""
from timeit import repeat


def is_sum_on_list(list_in: list, k: int) -> bool:
    for _ in list_in:
        x = list_in.pop()
        if k in [x + y for y in list_in]:
            return True
        else:
            return False


if __name__ == '__main__':
    print(is_sum_on_list([10, 15, 3, 7], 17))
    print(is_sum_on_list([10, 15, 3, 7], 10))
    print(is_sum_on_list([10, 15, 3, 7], 14))

    print(repeat(stmt=lambda: is_sum_on_list([10, 15, 3, 7], 17), number=20, repeat=3))
