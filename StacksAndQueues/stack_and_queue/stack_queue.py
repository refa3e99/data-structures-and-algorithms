class EmptyStackException(Exception):
    pass


class EmptyQueueException(Exception):
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


class Queue:
    def __init__(self):
        self.rear = None
        self.front = None

    def enqueue(self, value):
        node = Node(value)

        if self.front is None:
            self.front = node
            self.rear = node
        else:
            self.rear.nextNode = node
            self.rear = node

    def dequeue(self):
        try:
            temp = self.front
            self.front = temp.nextNode
            temp.nextNode = None
            return temp.value
        except:
            print("cannot dequeue from an empty queue")

    def peek(self):
        if self.front is not None:
            return self.front.value
        else:
            raise EmptyQueueException("peek from empty queue is not allowed")

    def is_empty(self):
        return True if self.front is None else False

    def __str__(self):
        tmp = self.front
        string = ''
        bgn = ' ## '
        end = ' ## '
        while tmp is not None:
            string += bgn + f"{tmp.value}" + end
            tmp = tmp.nextNode
        print(string)


