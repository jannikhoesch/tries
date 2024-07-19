class TrieNode:
    def __init__(self):
        self.children = [None] * 27


class TrieArray:
    def __init__(self):
        self.root = TrieNode()
        self.node_count = 0

        # Create mappping
        self.index_map = {}
        for i in range(ord('a'), ord('z') + 1):
            self.index_map[chr(i)] = i - ord('a')
        self.index_map['#'] = 26

    def insert(self, word):
        word += '#'
        node = self.root

        for c in word:
            i = self.index_map[c]
            if not node.children[i]:
                node.children[i] = TrieNode()
                self.node_count += 1
            node = node.children[i]

    def search(self, word):
        word += '#'
        node = self.root
        cost = 0

        for c in word:
            i = self.index_map.get(c)
            if i is None or not node.children[i]:
                return False, cost
            node = node.children[i]
            cost += 1

        return True, cost
