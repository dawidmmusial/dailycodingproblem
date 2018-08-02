"""
Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list.
If there is more than one possible reconstruction, return any of them. If there is no possible reconstruction,
then return null.

For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox",
you should return ['the', 'quick', 'brown', 'fox'].

Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond",
return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].
"""


def corecting(words: list, sentence: str) -> list:

    dict_words = {}

    for word in words:
        find_word = sentence.find(word)
        if find_word != -1:
            # find index
            dict_words[sentence.find(word)] = word
            # remove because of avoid double write
            sentence = sentence.replace(word,'_')

    # Python 3.6 return dict with sorted keys
    return list(dict_words.values())

if __name__ == '__main__':
    words = ['bed', 'bath', 'bedbath', 'and', 'beyond']
    sentence = 'bedbathandbeyond'
    print(corecting(words,sentence))
