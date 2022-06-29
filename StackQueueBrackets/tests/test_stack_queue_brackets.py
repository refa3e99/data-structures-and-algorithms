import pytest

from StackQueueBrackets.Stack_Queue_Brackets import validate_brackets


def test_first_valid_string():
    actual = validate_brackets('(hello)[]')
    expected = True
    assert actual == expected


def test_second_valid_string():
    actual = validate_brackets('(hello)[world]{}')
    expected = True
    assert actual == expected


def test_third_valid_string():
    actual = validate_brackets('{}{Code}[Fellows](())')
    expected = True
    assert actual == expected


def test_first_not_valid_string():
    actual = validate_brackets('[({}]')
    expected = False
    assert actual == expected


def test_second_not_valid_string():
    actual = validate_brackets('(()(((()[]{{}{{{')
    expected = False
    assert actual == expected


def test_third_not_valid_string():
    actual = validate_brackets('{A][asd()(){(})')
    expected = False
    assert actual == expected