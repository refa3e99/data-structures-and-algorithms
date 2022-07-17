import pytest
from tree_fizz_buzz.fizzBuzz import *


def test_create_new_tree_arr():
    kTree = KArrTree()
    actual = kTree.root
    expected = None
    assert actual == expected


def test_tree_structure(tree):
    actual = tree.child[2].value
    expected = 4
    assert actual == expected


def test_fizz_buzz_1(tree):
    actual = fizz_buzz(KTNode(15))
    expected = 'FizzBuzz'
    assert actual == expected


def test_fizz_buzz_2(tree):
    actual = fizz_buzz(KTNode(2))
    expected = '2'
    assert actual == expected


def test_fizz_buzz_3(tree):
    actual = fizz_buzz(KTNode(3))
    expected = 'Fizz'
    assert actual == expected


def test_fizz_buzz_4(tree):
    actual = fizz_buzz(KTNode(5))
    expected = 'Buzz'
    assert actual == expected


def test_return_new_tree(tree):
    actual = fizz_buzz_tree(tree)
    expected = tree
    assert actual != expected


@pytest.fixture
def tree():
    k__tree = KArrTree()
    k__tree.root = KTNode(1)
    k__tree.root.child.append(KTNode(2))
    k__tree.root.child.append(KTNode(3))
    k__tree.root.child.append(KTNode(4))
    return k__tree.root