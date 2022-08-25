from StacksAndQueues.Stack_and_queue.stack_queue import Queue
from trees.binaryTree.trees import TNode
from copy import deepcopy


class KArrTree:
    def __init__(self):
        self.root = None


class KTNode:
    def __init__(self, value):
        self.value = value
        self.child = []


def fizz_buzz(node):
    if node.value % 3 == 0 and node.value % 5 == 0:
        return "FizzBuzz"
    elif node.value % 3 == 0:
        return "Fizz"
    elif node.value % 5 == 0:
        return "Buzz"
    else:
        return str(node.value)


def fizz_buzz_tree(root):
    arr = []
    if not isinstance(root, KTNode):
        raise Exception

    new_root = deepcopy(root)
    new_tree = new_root
    new_node = fizz_buzz(new_root)
    new_root.value = new_node
    queue = Queue()
    queue.enqueue(new_root)
    before = []
    after = []
    while not queue.is_empty():
        new_root = queue.dequeue()
        for i in new_root.child:
            queue.enqueue(i)
            before.append(i.value)
            i.value = fizz_buzz(i)
            after.append(i.value)
    print(before)
    print(after)
    return new_tree


if __name__ == "__main__":
    k_tree = KArrTree()

    # create the root
    k_tree.root = KTNode(1)

    # the root children
    k_tree.root.child.append(KTNode(2))
    k_tree.root.child.append(KTNode(3))
    k_tree.root.child.append(KTNode(4))
    k_tree.root.child.append(KTNode(5))
    k_tree.root.child.append(KTNode(6))

    # first child children
    k_tree.root.child[0].child.append(KTNode(7))
    k_tree.root.child[0].child.append(KTNode(8))
    k_tree.root.child[0].child.append(KTNode(9))

    # second child children
    k_tree.root.child[1].child.append(KTNode(10))
    k_tree.root.child[1].child.append(KTNode(11))
    k_tree.root.child[1].child.append(KTNode(12))

    # third child children
    k_tree.root.child[2].child.append(KTNode(13))
    k_tree.root.child[2].child.append(KTNode(14))
    k_tree.root.child[2].child.append(KTNode(15))

    print(fizz_buzz_tree(k_tree.root).value)