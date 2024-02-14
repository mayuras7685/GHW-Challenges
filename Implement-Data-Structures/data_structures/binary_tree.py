# binary_tree.py
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self._insert_recursively(self.root, data)

    def _insert_recursively(self, node, data):
        if data < node.data:
            if node.left:
                self._insert_recursively(node.left, data)
            else:
                node.left = Node(data)
        elif data > node.data:
            if node.right:
                self._insert_recursively(node.right, data)
            else:
                node.right = Node(data)

    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.data, end=" ")
            self.inorder_traversal(node.right)

    def search(self, node, value):
        if not node or node.data == value:
            return node
        if value < node.data:
            return self.search(node.left, value)
        else:
            return self.search(node.right, value)

    def find_min(self, node):
        current = node
        while current.left:
            current = current.left
        return current.data

    def find_max(self, node):
        current = node
        while current.right:
            current = current.right
        return current.data

    def height(self, node):
        if not node:
            return -1
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        return max(left_height, right_height) + 1

    def size(self, node):
        if not node:
            return 0
        return self.size(node.left) + self.size(node.right) + 1

    def is_balanced(self, node):
        if not node:
            return True
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        if abs(left_height - right_height) <= 1 and self.is_balanced(node.left) and self.is_balanced(node.right):
            return True
        return False
