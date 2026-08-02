class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

# Time: O(L) for all three operations, where L is the length of the input string.
# Space: O(N·L) total for the trie structure (N = number of inserted words, L = average word length); O(1) auxiliary space for search/startsWith calls.

class PrefixTree:

    def __init__(self):
        self.trie = TrieNode()
        

    def insert(self, word: str) -> None:
        curr = self.trie

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()

            curr = curr.children[c]

        curr.is_end = True    

    def search(self, word: str) -> bool:
        curr = self.trie

        for c in word:
            if c not in curr.children:
                return False
                
            curr = curr.children[c]

        return curr.is_end
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.trie

        for c in prefix:
            if c not in curr.children:
                return False
                
            curr = curr.children[c]

        return True
        
        
        