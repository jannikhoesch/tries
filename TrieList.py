class TrieNode:
    def __init__(self, char=None):
        self.char = char
        self.firstChild = None
        self.nextSibling = None


class TrieList:
    def __init__(self):
        self.root = TrieNode()
        self.node_count = 0

    def insert(self, word):
        word += '#'
        node = self.root

        for c in word:
            if not node.firstChild:
                node.firstChild = TrieNode(c)
                self.node_count += 1
                node = node.firstChild
            else:
                current = node.firstChild
                prev = None

                while current and current.char < c:
                    prev = current
                    current = current.nextSibling

                if current and current.char == c:
                    node = current
                else:
                    new_node = TrieNode(c)
                    self.node_count += 1
                    if prev:
                        prev.nextSibling = new_node
                    else:
                        node.firstChild = new_node
                    new_node.nextSibling = current
                    node = new_node

    def search(self, word):
        word += '#'
        node = self.root.firstChild
        cost = 0

        for c in word:
            while node and node.char != c:
                node = node.nextSibling
                cost += 1
            if not node:
                return False, cost
            node = node.firstChild
            cost += 1

        return True, cost
