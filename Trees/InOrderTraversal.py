class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


class Solution:
    def recursiveSoln(self, root):
        pass

    def iterativeSoln(self, root):
        pass


if __name__ == '__main__':
    root = Node(3)
    root.left = Node(4)
    root.right = Node(5)
    root.left.left = Node(1)
    root.left.left.left = Node(2)