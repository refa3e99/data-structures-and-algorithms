# Other Classes has been overwritten due to importing errors on my computer
class EmptyStackException(Exception):
    pass


class Node:
    def __init__(self, value):
        self.value = value
        self.nextNode = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        node = Node(value)
        node.nextNode = self.top
        self.top = node

    def pop(self):
        try:
            temp = self.top
            self.top = temp.nextNode
            temp.nextNode = None
            return temp.value
        except:
            print("can't pop from an empty stack")

    def peek(self):
        if self.top is not None:
            return self.top.value
        else:
            raise EmptyStackException("peek from empty stack is not allowed")

    def is_empty(self):
        return True if self.top is None else False

    def __str__(self):
        tmp = self.top
        string = ''
        bgn = '***\n'
        while tmp is not None:
            string += bgn + f"{tmp.value}\n"
            tmp = tmp.nextNode
        print(string)


class PseudoQueue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, value):
        self.stack1.push(value)

    def dequeue(self):
        while not self.stack1.is_empty():
            popped = self.stack1.pop()
            self.stack2.push(popped)
        return self.stack2.pop()

# ps = PseudoQueue()
# ps.enqueue(5)
# ps.enqueue(4)
# ps.enqueue(3)
# ps.enqueue(2)
# ps.enqueue(1)
# print(ps.dequeue())
# print(ps.dequeue())
# print(ps.dequeue())
# print(ps.dequeue())
# print(ps.dequeue())
