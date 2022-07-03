import pytest

from trees.BinaryTree.trees import *

def test_instantiate_empty():

    tree = BinarySearchTree()
    actual = tree.root
    expected = None
    assert actual == expected


def test_add_to_empty():

    tree = BinarySearchTree()
    tree.add(10)
    actual = tree.root.value
    expected = 10
    assert actual == expected


def test_add_left():

    tree = BinarySearchTree()
    tree.add(10)
    tree.add(5)
    actual = tree.root.left.value
    expected = 5
    assert actual == expected


def test_add_right():

    tree = BinarySearchTree()
    tree.add(10)
    tree.add(15)
    actual = tree.root.right.value
    expected = 15
    assert actual == expected


def test_add_to_right(tree):

    tree.add(30)
    actual = tree.root.right.right.value
    expected = 30
    assert actual == expected


def test_add_to_left(tree):

    tree.add(1)
    actual = tree.root.left.left.left.value
    expected = 1
    assert actual == expected


def test_contains(tree):

    actual = tree.contains(3)
    expected = True
    assert actual == expected


def test_doesnt_contain(tree):

    actual = tree.contains(100)
    expected = False
    assert actual == expected