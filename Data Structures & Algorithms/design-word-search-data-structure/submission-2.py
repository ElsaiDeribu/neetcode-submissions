class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.trie = TrieNode()
        
        
    def addWord(self, word: str) -> None:
        curr = self.trie

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]

        curr.is_end = True
        

    def search(self, word: str) -> bool:

        curr = self.trie

        def dfs(idx, curr):
            if idx == len(word):
                return curr.is_end
            
            if word[idx] == ".":
                for child in curr.children:
                    if dfs(idx + 1, curr.children[child]):
                        return True

            elif word[idx] in curr.children:
                return dfs(idx + 1, curr.children[word[idx]])

            return False


        return dfs(0, curr)

        







        
