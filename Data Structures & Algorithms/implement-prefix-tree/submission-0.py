class Node:
    def __init__(self):
        self.children=[None]*26
        self.isEndOfWord=False

class PrefixTree:

    def __init__(self):
        self.root=Node()

    def insert(self, word: str) -> None:
        curr=self.root
        for c in word:
            index=ord(c)-ord('a')
            if curr.children[index] is None:
                curr.children[index]=Node()
            curr=curr.children[index]
        curr.isEndOfWord=True


    def search(self, word: str) -> bool:
        curr=self.root
        for x in word:
            indx=ord(x)-ord('a')
            if curr.children[indx] is None:
                return False
            curr=curr.children[indx]

        return curr.isEndOfWord

    def startsWith(self, prefix: str) -> bool:
        curr=self.root
        for c in prefix:
            indx=ord(c)-ord('a')
            if curr.children[indx] is None:
                return False
            curr=curr.children[indx]
        return True
        
        