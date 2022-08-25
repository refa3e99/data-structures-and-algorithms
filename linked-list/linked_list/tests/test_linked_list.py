from linked_list import (LinkedList)

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


def test_k_where_list_size_is_one():
    actual = ll.kth_from_end(0)
    expected = 3
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
    expected = "{1} -> {4} -> {5} -> {3} -> {2} -> {1} -> {0} -> NULL"
    assert actual == expected


def test_insert_before_middle():
    ll.insert_before(3, 7)
    actual = ll.to_string()
    expected = "{1} -> {4} -> {5} -> {7} -> {3} -> {2} -> {1} -> {0} -> NULL"
    assert actual == expected


def test_insert_before_first_node():
    ll.insert_before(1, 10)
    actual = ll.to_string()
    expected = "{10} -> {1} -> {4} -> {5} -> {7} -> {3} -> {2} -> {1} -> {0} -> NULL"
    assert actual == expected


def test_insert_after_middle():
    ll.insert_after(7, 9)
    actual = ll.to_string()
    expected = "{10} -> {1} -> {4} -> {5} -> {7} -> {9} -> {3} -> {2} -> {1} -> {0} -> NULL"
    assert actual == expected


def test_insert_after_last():
    ll.insert_after(0, -1)
    actual = ll.to_string()
    expected = "{10} -> {1} -> {4} -> {5} -> {7} -> {9} -> {3} -> {2} -> {1} -> {0} -> {-1} -> NULL"
    assert actual == expected


def test_k_is_greater_than_length():
    actual = ll.kth_from_end(12)
    expected = "length is out of range"
    assert actual == expected


def test_k_is_equal_to_length():
    actual = ll.kth_from_end(10)
    expected = 10
    assert actual == expected


def test_k_is_not_positive():
    actual = ll.kth_from_end(-1)
    expected = "length is out of range"
    assert actual == expected


def test_k_in_middle():
    actual = ll.kth_from_end(5)
    expected = 9
    assert actual == expected