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


def test_append_item():
    ll.append(2)
    actual = ll.to_string()
    expected = "{1} -> {4} -> {5} -> {3} -> {2} -> NULL"
    assert actual == expected


def test_append_multi_items():
    ll.append(1)
    ll.append(0)
    actual = ll.to_string()
    expected = "{1} -> {4} -> {5} -> {3} -> {2} -> {1} -> {0} NULL"


def test_insert_before_middle():
    ll.insert_before(4,7)
    actual = ll.to_string()
    expected = "{1} -> {4} -> {5} -> {7} -> {3} -> {2} -> {1} -> {0} NULL"


def test_insert_before_first_node():
    ll.insert_before(1,0)
    actual = ll.to_string()
    expected = "{0} -> {1} -> {4} -> {5} -> {3} -> {2} -> {1} -> {0} NULL"


def test_insert_after_middle():
    ll.insert_after(4,9)
    actual = ll.to_string()
    expected = "{1} -> {4} -> {5} -> {7} -> {9} -> {3} -> {2} -> {1} -> {0} NULL"


def test_insert_after_last():
    ll.insert_after(9,-1)
    actual = ll.to_string()
    expected = "{1} -> {4} -> {5} -> {7} -> {9} -> {3} -> {2} -> {1} -> {0} -> {-1} -> NULL"