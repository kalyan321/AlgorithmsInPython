class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfTheWord = False


def insert(root, key):
    for i in key:
        val = ord(i) - ord('a')
        if root.children[val] is not None:
            root = root.children[val]
        else:
            root.children[val] = True
            root.children[val] = TrieNode()
            root = root.children[val]
    root.isEndOfTheWord = True


def search(root, key):
    for i in key:
        val = ord(i) - ord('a')
        if not root.children[val]:
            break
        root = root.children[val]
    return root.isEndOfTheWord


if __name__ == '__main__':
    keys = ['iam', 'king', 'kalyan']
    t = TrieNode()
    for i in keys:
        insert(t, i)
    print(search(t, "kig"))
