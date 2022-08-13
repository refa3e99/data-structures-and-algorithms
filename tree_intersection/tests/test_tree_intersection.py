import pytest
from tree_intersection.tree_intersection import tree_intersection
from trees.binaryTree.trees import TNode, BinarySearchTree


def test_exits():
    assert tree_intersection


def test_return_common_values(t1, t2):
    actual = tree_intersection(t1, t2)
    expected = [100, 125, 160, 175, 200, 350, 500]
    assert actual == expected


@pytest.fixture
def t1():
    t1 = BinarySearchTree()
    t1.root = TNode(150)
    t1.root.left = TNode(100)
    t1.root.right = TNode(250)
    t1.root.left.left = TNode(75)
    t1.root.left.right = TNode(160)
    t1.root.left.right.left = TNode(125)
    t1.root.left.right.right = TNode(175)
    t1.root.right.left = TNode(200)
    t1.root.right.right = TNode(350)
    t1.root.right.right.left = TNode(300)
    t1.root.right.right.right = TNode(500)
    return t1


@pytest.fixture
def t2():
    t2 = BinarySearchTree()
    t2.root = TNode(42)
    t2.root.left = TNode(100)
    t2.root.right = TNode(600)
    t2.root.left.left = TNode(15)
    t2.root.left.right = TNode(160)
    t2.root.left.right.left = TNode(125)
    t2.root.left.right.right = TNode(175)
    t2.root.right.left = TNode(200)
    t2.root.right.right = TNode(350)
    t2.root.right.right.left = TNode(4)
    t2.root.right.right.right = TNode(500)
    return t2