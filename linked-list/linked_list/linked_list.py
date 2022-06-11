class Node:
    def __init__(self, value):
        self.value = value
        self.nextNode = None

class LinkedList:
    def __init__(self, head = None):
        self.head = head

    def insert(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            return
        currentNode = self.head
        while True:
            if currentNode.nextNode is None:
                currentNode.nextNode = node
                break
            currentNode = currentNode.nextNode

    def to_string(self):
        strng = ''
        currentNode = self.head
        while currentNode is not None:
            strng += f"{ {currentNode.value} } -> "
            currentNode = currentNode.nextNode
        print (strng + 'NULL')

    def includes(self, value):
        item = Node(value)
        current = self.head
        while current:
            if current.value == item.value:
                return True
            current = current.nextNode
        return False

#ll = LinkedList()
#ll.insert(3)
#ll.insert(4)
#ll.insert(5)
#ll.insert(6)
#ll.to_string()
#print(ll.includes(6))
#print(ll.includes(7))