class TNode:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


class Tree:
    def __init__(self):
        self.root = None

    def pre_order(self):
        arr = []

        def traverse(root):
            arr.append(root.value)
            if root.left:
                traverse(root.left)
            if root.right:
                traverse(root.right)

        traverse(self.root)
        return arr

    def in_order(self):
        arr = []

        def traverse(root):
            if root.left:
                traverse(root.left)
            arr.append(root.value)

            if root.right:
                traverse(root.right)

        traverse(self.root)
        return arr

    def post_order(self):
        arr = []

        def traverse(root):
            if root.left:
                traverse(root.left)

            if root.right:
                traverse(root.right)
            arr.append(root.value)

        traverse(self.root)
        return arr

class BinarySearchTree(Tree):

    def add(self, value):
        root = self.root
        node = TNode(value)
        while root is not None:
            if node.value >= root.value:
                if root.right is None:
                    root.right = node
                    break
                root = root.right
            elif node.value < root.value:
                if not root.left:
                    root.left = node
                    break
                root = root.left

    def contains(self, value):
        root = self.root
        while root:
            if root.value == value:
                return True
            if root.value > value:
                if not root.left:
                    return False
            root = root.left
            if root.value < value:
                if root.right is None:
                    return False
                root = root.right


