class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def lowestCommonAncestor(root, n1, n2):
    if root is None:
        return None
    if root.data == n1 or root.data == n2:
        return root.data
    left = lowestCommonAncestor(root.left, n1, n2)
    right = lowestCommonAncestor(root.right, n1, n2)
    if left and right:
        return root.data
    return left if left else right


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)
    print(lowestCommonAncestor(root, 1, 21))
