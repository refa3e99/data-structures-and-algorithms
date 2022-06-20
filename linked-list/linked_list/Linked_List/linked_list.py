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
        if currentNode is None:
            self.head = node
        else:
            while True:
                if currentNode.nextNode is None:
                    currentNode.nextNode = node
                    break
                currentNode = currentNode.nextNode

    def insert_after(self, target, value):
        self.target = target
        self.value = value
        node = Node(value)
        current = self.head
        try:
            if current.value == target:
                node.nextNode = current.nextNode
                current.nextNode = node
            else:
                while True:
                    if current.value == target:
                        node.nextNode = current.nextNode
                        current.nextNode = node
                        return True
                    current = current.nextNode
                return False
        except:
            print(f"The node of value {target} does not exist")

    def insert_before(self, target, value):
        self.target = target
        self.value = value
        node = Node(value)
        current = self.head
        if current.value == target:
            node.nextNode = current
            self.head = node
        else:
            while current.nextNode is not None:
                if current.nextNode.value == target:
                    node.nextNode = current.nextNode
                    current.nextNode = node
                    return True
                current = current.nextNode
            print(f"The node of value {target} does not exist")

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

    def kth_from_end(self, k):
        self.k = k

        current = self.head
        length = 0
        while current.nextNode != "NULL":
            if current.nextNode is None:
                break
            length += 1
            current = current.nextNode
        # print(f"length is {length}")
        if k > length or k < 0:
            print("length is out of range")
            return "length is out of range"
        start = length
        current = self.head
        while start != k:
            # print(current.value)
            if current.nextNode is None:
                break
            start -= 1
            current = current.nextNode
        print(f"{current.value}")
        return current.value


#ll = LinkedList()
#ll.insert(2)
#ll.append(1)
#ll.insert(4)
#ll.insert(5)
#ll.insert(6)
#ll.insert(7)
#ll.insert(8)
#ll.insert_after(8, 3)
#ll.insert_before(9, 0)
#ll.insert_before(0, 7)
#ll.insert_after(1, 0)
#print(ll.to_string())
# print(ll.includes(6))
# print(ll.includes(7))
