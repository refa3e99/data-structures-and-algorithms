import pytest

from zipLists.linked_list_zip import *


def test_one_item_for_both_lists():
    ll = LinkedList()
    ll.insert(9)

    ll2 = LinkedList()
    ll2.insert(4)

    actual = zipLists(ll, ll2)
    expected = "{9} -> {4} -> NULL"
    assert actual == expected


def test_first_list_is_longer():
    ll = LinkedList()
    ll.insert(9)
    ll.insert(8)
    ll.insert(7)

    ll2 = LinkedList()
    ll2.insert(4)

    actual = zipLists(ll, ll2)
    expected = "{7} -> {4} -> {8} -> {9} -> NULL"
    assert actual == expected


def test_same_length():
    ll = LinkedList()
    ll.insert(9)
    ll.insert(8)
    ll.insert(7)

    ll2 = LinkedList()
    ll2.insert(4)
    ll2.insert(3)
    ll2.insert(2)

    actual = zipLists(ll, ll2)
    expected = "{7} -> {2} -> {8} -> {3} -> {9} -> {4} -> NULL"
    assert actual == expected


def test_second_list_is_longer():
    ll2 = LinkedList()
    ll2.insert(9)
    ll2.insert(8)
    ll2.insert(7)

    ll = LinkedList()
    ll.insert(4)

    actual = zipLists(ll, ll2)
    expected = "{7} -> {4} -> {8} -> {9} -> NULL"
    assert actual == expected