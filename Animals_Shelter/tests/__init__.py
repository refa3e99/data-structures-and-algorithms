# classes have been overwritten due to importing errors
class EmptyQueueException(Exception):
    pass


class Node:
    def __init__(self, value):
        self.value = value
        self.nextNode = None


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


class AnimalShelter:
    def __init__(self):
        self.dogs = Queue()
        self.cats = Queue()

    def enqueue(self, animal):
        if animal.type == 'Dog':
            self.dogs.enqueue(animal)
        if animal.type == 'Cat':
            self.cats.enqueue(animal)

    def dequeue(self, pref):
        if pref == 'Dog':
            return self.dogs.dequeue()
        if pref == 'Cat':
            return self.cats.dequeue
        else:
            return None


class Dog:
    def __init__(self, name):
        self.name = name
        self.type = 'Dog'


class Cat:
    def __init__(self, name):
        self.name = name
        self.type = 'Cat'