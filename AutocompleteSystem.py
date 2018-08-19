"""
Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all
strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.
"""


def autocomplete(list_strings: list, query: str) -> list:

    return [s for s in list_strings if s.startswith(query)]


if __name__ == '__main__':
    lst = ['dog', 'deer', 'deal']
    query = 'de'

    print(autocomplete(lst,query))