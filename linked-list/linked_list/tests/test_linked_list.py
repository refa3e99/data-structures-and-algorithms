import pytest

from linked_list.linked_list import (LinkedList)

ll = LinkedList()


def test_empty_linked_list():
    actual = ll.to_string()
    expected = "NULL"
    assert actual == expected


def test_insert():
    ll.insert(3)
    actual = ll.to_string()
    expected = '{3} -> NULL'
    assert actual == expected


def test_insert_multi():
    ll.insert(5)
    ll.insert(4)
    actual = ll.to_string()
    expected = '{4} -> {5} -> {3} -> NULL'
    assert actual == expected


def test_included_item():
    actual = ll.includes(5)
    expected = True
    assert actual == expected


def test_not_included_item():
    actual = ll.includes(9)
    expected = False
    assert actual == expected


def test_returned_linked_list():
    ll.insert(1)
    actual = ll.to_string()
    expected = "{1} -> {4} -> {5} -> {3} -> NULL"
    assert actual == expected
