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

    def append(self, value):
        node = Node(value)

        currentNode = self.head
        while True:
            if currentNode.nextNode is None:
                currentNode.nextNode = node
                break
            currentNode = currentNode.nextNode

    def insert_after(self, index, value):
        self.index = index
        self.value = value
        node = Node(value)
        current = self.head
        try:
            if index < 1:
                print("please stick to the range of the list")
            else:
                for i in range(1, index):
                    current = current.nextNode
                node.nextNode = current.nextNode
                current.nextNode = node
        except:
            print("please stick to the range of the list")

    def insert_before(self, index, value):
        self.index = index
        self.value = value
        node = Node(value)
        current = self.head
        try:
            if index == 1:
                node.nextNode = current
                self.head = node
            elif index < 1:
                print("please stick to the range of the list")
            else:
                for i in range(1, index - 1):
                    current = current.nextNode
                node.nextNode = current.nextNode
                current.nextNode = node
        except:
            print("please stick to the range of the list")

    def to_string(self):
        strng = ''
        currentNode = self.head
        while currentNode is not None:
            strng += f"{ {currentNode.value} } -> "
            currentNode = currentNode.nextNode
        return strng + 'NULL'

    def includes(self, value):
        item = Node(value)
        current = self.head
        while current:
            if current.value == item.value:
                return True
            current = current.nextNode
        return False


ll = LinkedList()
#ll.insert(1)
#ll.insert(2)
#ll.insert(4)
#ll.insert(5)
# ll.insert(5)
#ll.insert_after(2, 3)
#ll.insert_before(5, 0)
#ll.insert_before(1, 7)
#ll.insert_after(7, 0)
#print(ll.to_string())
# print(ll.includes(6))
# print(ll.includes(7))
