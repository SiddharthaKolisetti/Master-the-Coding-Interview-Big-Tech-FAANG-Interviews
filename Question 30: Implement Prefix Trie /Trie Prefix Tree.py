class TrieNode:
    def __init__(self):
        self.end = False
        self.keys = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, node=None):
        if node is None:
            node = self.root
        if len(word) == 0:
            node.end = True
            return
        elif word[0] not in node.keys:
            node.keys[word[0]] = TrieNode()
            self.insert(word[1:], node.keys[word[0]])
        else:
            self.insert(word[1:], node.keys[word[0]])

    def search(self, word, node=None):
        if node is None:
            node = self.root
        if len(word) == 0 and node.end:
            return True
        elif len(word) == 0:
            return False
        elif word[0] not in node.keys:
            return False
        else:
            return self.search(word[1:], node.keys[word[0]])

    def startsWith(self, prefix, node=None):
        if node is None:
            node = self.root
        if len(prefix) == 0:
            return True
        elif prefix[0] not in node.keys:
            return False
        else:
            return self.startsWith(prefix[1:], node.keys[prefix[0]])      
