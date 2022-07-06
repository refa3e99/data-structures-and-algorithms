import pytest
from breadthFirst.breadth_first import *


def test_breadth_first_one():
    tree = Tree()
    tree.root = TNode(2)
    tree.root.left = TNode(7)
    tree.root.right = TNode(5)
    tree.root.left.left = TNode(2)
    tree.root.left.right = TNode(6)
    tree.root.right.left = TNode(9)
    tree.root.right.left.left = TNode(4)
    actual = breadth_first(tree.root)
    expected = [2, 7, 5, 2, 6, 9, 4]
    assert actual == expected


def test_breadth_first_two():
    tree = Tree()
    tree.root = TNode(1)
    tree.root.left = TNode(2)
    tree.root.right = TNode(3)
    tree.root.left.left = TNode(4)
    tree.root.left.right = TNode(5)
    tree.root.right.left = TNode(6)
    tree.root.right.left.left = TNode(7)
    actual = breadth_first(tree.root)
    expected = [1, 2, 3, 4, 5, 6, 7]
    assert actual == expected


def test_breadth_first_three():
    tree = Tree()
    tree.root = TNode(1)

    actual = breadth_first(tree.root)
    expected = [1]
    assert actual == expected