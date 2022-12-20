"""
Daily Coding Problem: Problem #57 [Medium]

This problem was asked by Amazon.

Given a string s and an integer k, break up the string into multiple lines such that each line has a length of k or less. You must break it up so that words don't break across lines. Each line has to have the maximum possible amount of words. If there's no way to break the text up, then return null.

You can assume that there are no spaces at the ends of the string and that there is exactly one space between each word.

For example, given the string "the quick brown fox jumps over the lazy dog" and k = 10, you should return: ["the quick", "brown fox", "jumps over", "the lazy", "dog"]. No string in the list has a length of more than 10.
"""


def get_k_nos_from_string(sentence: str, char_num: int) -> list:
    lst = []
    count = 0
    start_index = 0
    space_index = 0
    length = len(sentence)

    while count + start_index < length:
        if is_space(sentence[start_index + count]):
            space_index = start_index + count
        if count == char_num:
            lst.append(sentence[start_index:space_index])
            start_index = space_index + 1
            count = 0
        count += 1
    lst.append(sentence[start_index:])
    return lst


def is_space(character):
    return character == " "
