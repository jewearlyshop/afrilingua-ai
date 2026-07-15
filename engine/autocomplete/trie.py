class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root

        for letter in word:
            if letter not in node.children:
                node.children[letter] = TrieNode()

            node = node.children[letter]

        node.is_word = True

    def search(self, word):
        node = self.root

        for letter in word:
            if letter not in node.children:
                return False

            node = node.children[letter]

        return node.is_word

    def autocomplete(self, prefix):
        node = self.root

        for letter in prefix:
            if letter not in node.children:
                return []

            node = node.children[letter]

        words = []
        self._collect_words(node, prefix, words)
        return words

    def _collect_words(self, node, current_word, words):
        if node.is_word:
            words.append(current_word)

        for letter, child in node.children.items():
            self._collect_words(child, current_word + letter, words)