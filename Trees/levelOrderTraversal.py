
# Approach 1 (Using Recursion and height of tree)
# Approach 2 (Using Queue following Breadth First Traversal)
# Approach 3 (Using Preorder Traversal and hashing)

class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


class Solution:
    def recursive(self, root):
        pass

    def iterative(self, root):
        pass


if __name__ == '__main__':
    root = Node(3)
    root.left = Node(2)
    root.right = Node(4)
    root.left.left = Node(1)
    root.right.right = Node(5)
