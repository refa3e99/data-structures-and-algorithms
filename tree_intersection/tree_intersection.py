from hashtable.hashtable import HashTable
from trees.binaryTree.trees import BinarySearchTree


def tree_intersection(t1, t2):

    hash_map = HashTable()
    values = set()

    t1_vals = BinarySearchTree.pre_order(t1)
    t2_vals = BinarySearchTree.pre_order(t2)

    for i in t1_vals:
        hash_map.set(str(i), i)

    for i in t2_vals:
        if hash_map.contains(str(i)):
            values.add(i)

    return sorted(values)