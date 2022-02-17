class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def diameter(root):
    if root is None:
        return 0
    lh = diameter(root.left)
    rh = diameter(root.right)
    res.append([root.data, lh + rh + 1])
    if lh >= rh:
        return lh + 1
    return rh + 1


if __name__ == '__main__':
    res = []
    root = Node(2)
    root.left = Node(3)
    root.right = Node(4)
    root.left.left = Node(5)
    root.left.left.left = Node(6)
    root.left.right = Node(7)
    root.left.right.left = Node(8)
    diameter(root)
    print(res)
