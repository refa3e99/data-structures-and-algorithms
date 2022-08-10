import pytest
from hashmap_repeated_word.hashmap_repeated_word import repeated_word


def test_empty_string():
    actual = repeated_word('')
    expected = None
    assert actual == expected


def test_two_words():
    actual = repeated_word('ahmad plays with ahmad')
    expected = 'ahmad'
    assert actual == expected


def test_word_with_symbols():
    actual = repeated_word('hi? is there! hi')
    expected = 'hi'
    assert actual == expected


def test_capital_cases():
    actual = repeated_word('hello HellO   HELLO')
    expected = 'hello'
    assert actual == expected


def test_case_1():
    actual = repeated_word('Once upon a time, there was a brave princess who...')
    expected = 'a'
    assert actual == expected


def test_case_2():
    actual = repeated_word('It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..')
    expected = 'it'
    assert actual == expected


def test_case_3():
    actual = repeated_word('It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York...')
    expected = 'summer'
    assert actual == expected