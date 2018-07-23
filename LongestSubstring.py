"""
Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".
"""

import re


def longest_substring(in_str: str, k: int) -> str:
    if not in_str or k < 2:
        return 'No result'

    # iterate for unique chars
    unique_chars = set(in_str)
    # global change value indexer
    indexer_value = k - 1
    substring = ''

    for c in unique_chars:
        # find all char indexes
        char_indexes = [x.start() for x in re.finditer(c, in_str)]
        len_char_index = len(char_indexes)
        if len_char_index >= k:
            i = 0
            # cut all substring from string
            while i < len_char_index - 1:
                cut_str = in_str[char_indexes[i] + 1:char_indexes[i + indexer_value]]
                # set the longest substring
                if len(cut_str) > len(substring):
                    substring = cut_str
                i += indexer_value
    if substring:
        return substring
    else:
        return 'No conditions'


if __name__ == '__main__':
    args = [('abcba', 2),('abcbaa', 3),('abcbaa', 2),('abacbdx', 2),('ababbax', 2),('abacbax', 3),('abcba', 3),('abcba', 1),('', 2)]

    for arg in args:
        print(longest_substring(*arg))

