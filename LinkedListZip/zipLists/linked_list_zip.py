# CLASSES HAS BEEN OVERWRITTEN DUE TO IMPORTS ERROR

class Node:
    def __init__(self, value):
        self.value = value
        self.nextNode = None


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert(self, value):
        node = Node(value)
        node.nextNode = self.head
        self.head = node

    def to_string(self):
        strng = ''
        currentNode = self.head
        while currentNode is not None:
            strng += f"{ {currentNode.value} } -> "
            currentNode = currentNode.nextNode
        return strng + 'NULL'

    def Length(self):
        current = self.head
        length = 0
        while current != None:
            length += 1
            current = current.nextNode
        return length

def zipLists(list1, list2):
    if list2.Length() > list1.Length():
        list1 , list2 = list2 , list1

    a = list1.head
    b = list2.head

    while a != None and b != None:

        c = a.nextNode
        d = b.nextNode


        b.nextNode = c
        a.nextNode = b

        a = c
        b = d
        list2.head = b

    return list1.to_string()

ll = LinkedList()
ll.insert(2)
ll.insert(1)
ll.insert(4)
ll.insert(5)

ll2 = LinkedList()
ll2.insert(2)
ll2.insert(1)
ll2.insert(4)
ll2.insert(5)

zipLists(ll,ll2)