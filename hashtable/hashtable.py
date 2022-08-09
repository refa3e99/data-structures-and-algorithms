"""
In this module we will have the linked list and hashmap implementation

"""


class Node:
    """
    Node Instantiator.
    This class will have only an __init__ method to create nodes.
    """

    def __init__(self, value, next=None):
        """
        Takes two arguments:
        1. Value: str, int, ..., etc.
        2. Next: Node
        returns: None
        """
        self.value = value
        self.next = next


class LinkedList:
    """
    A Linked List class with a single head node
    """

    def __init__(self):
        """
        Instantiates a singly-linked list with an empty head node.
        Args: head (None by default)
        Outputs: None
        """
        self.head = None

    def insert(self, value):
        """
        This method will insert a node at the start of the linked list
        arguments :
        value
        returns:
        None
        """
        node = Node(value)
        node.next = self.head
        self.head = node


class HashTable:
    """
    HashTable class will have multiple methods, set, get,
    contains, keys and hash.
    It is a data structure that uses keys and values to store
    data to provide easy and fast access to its items.
    """

    def __init__(self, size=1024):
        """
        Takes one arguments:
        1. size: int
        returns: None
        """
        self.__size = size
        self.__buckets = [None] * size
        self.__keys = []

    def __hash(self, key):
        """
        This method will take a key as an argument and returns
        the index in the collection of buckets for that key.
        """
        return sum([ord(i) for i in key]) * 283 % self.__size

    def set(self, key, value):
        """
          this method will  hash the key and set the value and key pair in the buckets,
          also handling the collisions as needed
          Return: Nothing
          Arguments: Key , value
        """
        hashed_key = self.__hash(key)
        if self.__buckets[hashed_key] == None:
            hash_list = LinkedList()
            self.__buckets[hashed_key] = hash_list
        self.__keys.append(key)
        self.__buckets[hashed_key].insert((key, value))

    def get(self, key):
        """
        Used to find the value that is associated with the passed key.
        :param key: Hash key
        :retern: referenced value by passed key
        """
        hashed_key = self.__hash(key)
        ll = self.__buckets[hashed_key]
        current = ll.head
        while current:
            if current.value[0] == key:
                return current.value[1]
            current = current.next
        return None

    def contains(self, key):
        """
        This method will take a key
        returns : True if the key exists in the hashmap, and False if it doesn't exist
        """
        idx = self.__hash(key)
        bucket = self.__buckets[idx]
        if bucket is not None:
            current = bucket.head
            while current:
                if current.value[0] == key:
                    return True
                current = current.next
        return False


    def key(self):
        """
        this method will return a collections of all the keys in hashmap as an object
        """
        return self.__keys


if __name__ == '__main__':
    hash_map = HashTable()
    hash_map.set('key_1', 'yousef')
    hash_map.set('key_2', 'ahmad')
    hash_map.set('key_3', 'mohammad')

    print(hash_map.contains('key_1'))
    print(hash_map.contains('key_5'))

    print(hash_map.key())

    print(hash_map.get('key_5'))