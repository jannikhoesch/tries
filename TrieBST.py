class TrieNode:
    def __init__(self, c=None):
        self.data = c
        self.left = None
        self.cen = None
        self.right = None


class TrieBST:
    def __init__(self):
        self.root = None
        self.node_count = 0

    def insert(self, word):
        word += '#'

        def _insert(node, word, i):
            if i == len(word):
                return node

            c = word[i]
            if not node:
                node = TrieNode(c)
                self.node_count += 1

            if c < node.data:
                node.left = _insert(node.left, word, i)
            elif c > node.data:
                node.right = _insert(node.right, word, i)
            else:
                node.cen = _insert(node.cen, word, i + 1)
            return node

        self.root = _insert(self.root, word, 0)

    def search(self, word):
        word += '#'

        def _search(node, word, i, cost):
            if not node:
                return False, cost
            if i == len(word):
                return True, cost

            c = word[i]
            if c < node.data:
                return _search(node.left, word, i, cost + 1)
            elif c > node.data:
                return _search(node.right, word, i, cost + 1)
            else:
                return _search(node.cen, word, i + 1, cost + 1)

        return _search(self.root, word, 0, 0)
