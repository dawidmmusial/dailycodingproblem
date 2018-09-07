"""
Given a string s and an integer k, break up the string into multiple texts such that each text has a length of k orless.
You must break it up so that words don't break across lines. If there's no way to break the text up, then return null.

You can assume that there are no spaces at the ends of the string and that there is exactly one space between each word.

For example, given the string "the quick brown fox jumps over the lazy dog" and k = 10, you should return:
["the quick", "brown fox", "jumps over", "the lazy", "dog"]. No string in the list has a length of more than 10.
"""


def break_it(sentence: str, k: int) -> list:
    split_sentence = sentence.split()
    fill_words = [split_sentence[0]]

    for word in split_sentence[1:]:
        if len(fill_words[-1] + word) < k:
            fill_words[-1] = ' '.join([fill_words[-1], word])
        else:
            fill_words.append(word)

    return fill_words


if __name__ == '__main__':
    sentence_to_cut = "the quick brown fox jumps over the lazy dog"
    words_number = 10
    print(break_it(sentence_to_cut, words_number))
