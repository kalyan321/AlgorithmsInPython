class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def balanced_height(root):
    if root is None:
        return 0
    lh = balanced_height(root.left)
    rh = balanced_height(root.right)
    if lh == -1 or rh == -1:
        return -1
    if abs(lh - rh) > 1:
        return -1
    if lh > rh:
        return lh + 1
    else:
        return rh + 1


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.right.left = Node(6)
    root.left.right = Node(7)
    root.left.left = Node(4)
    root.left.left.right = Node(5)
    if balanced_height(root) == -1:
        print(False)
    else:
        print(True)
