from StacksAndQueues.Stack_and_queue.stack_queue import Queue
from trees.binaryTree.trees import *


def breadth_first(root):
    if not isinstance(root, TNode):
        raise Exception
    queue = Queue()
    queue.enqueue(root)
    arr = []
    while not queue.is_empty():
        front = queue.dequeue()
        arr.append(front.value)
        if front.left:
            queue.enqueue(front.left)
        if front.right:
            queue.enqueue(front.right)
    return arr
