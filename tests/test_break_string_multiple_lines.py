from src.medium.break_string_multiple_lines import *


def test_get_k_nos_from_string_with_10_chars():
    assert get_k_nos_from_string("the quick brown fox jumps over the lazy dog", 10) == [
        "the quick",
        "brown fox",
        "jumps over",
        "the lazy",
        "dog",
    ]


def test_get_k_nos_from_string_with_9_chars():
    assert get_k_nos_from_string("the quick brown fox jumps over the lazy dog", 8) == [
        "the",
        "quick",
        "brown",
        "fox",
        "jumps",
        "over the",
        "lazy dog",
    ]
