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
        if not self.root:
            self.root = TNode(value)

        def traverse(root):
            if value < root.value:
                if root.left:
                    traverse(root.left)
                else:
                    root.left = TNode(value)
            elif value > root.value:
                if root.right:
                    traverse(root.right)
                else:
                    root.right = TNode(value)

        traverse(self.root)

    def contains(self, value):
        if not self.root:
            return False

        def traverse(root):
            if value == root.value:
                # print("true")
                return True

            else:
                try:
                    if value < root.value:
                        # print("left")
                        return traverse(root.left)

                    elif value > root.value:
                        # print("right")
                        return traverse(root.right)
                except:
                    return False

        if traverse(self.root) is None:
            return False
        else:
            return traverse(self.root)


# if __name__ == "__main__":
#     search_tree = BinarySearchTree()
#     search_tree.root = TNode(2)
#     search_tree.root.right = TNode(3)
#     search_tree.root.left = TNode(1)
