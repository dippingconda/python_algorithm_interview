"""
https://leetcode.com/problems/implement-trie-prefix-tree
"""


class TrieNode:
    def __init__(self):
        self.word = False
        self.children = {}


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

        node.word = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]

        return node.word

    def starts_with(self, prefix: str):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]

        return True


if __name__ == '__main__':
    test_case = 'apple'
    trie_tree = Trie()
    trie_tree.insert('apple')
    trie_tree.insert('appear')
    trie_tree.insert('appeal')
    print(f'{trie_tree.search("apple")}')
    print(f'{trie_tree.starts_with("app")}')
    print(f'{trie_tree.starts_with("p")}')
