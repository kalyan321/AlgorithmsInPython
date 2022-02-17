from collections import defaultdict


class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def constructTree(inorder, preorder, start, end):
    if start > end:
        return None
    root = Node(preorder[constructTree.counter])
    constructTree.counter += 1
    if start == end:
        return root
    root.left = constructTree(inorder, preorder, start, d[root.data] - 1)
    root.right = constructTree(inorder, preorder, d[root.data] + 1, end)
    return root


def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)


if __name__ == '__main__':
    inOrder = ['D', 'B', 'E', 'A', 'F', 'C']
    preOrder = ['A', 'B', 'D', 'E', 'C', 'F']
    d = defaultdict(int)
    for i in range(len(preOrder)):
        d[inOrder[i]] = i
    constructTree.counter = 0
    root = constructTree(inOrder, preOrder, 0, len(inOrder) - 1)
    inorder(root)
