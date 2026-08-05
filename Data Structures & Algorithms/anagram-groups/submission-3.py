from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs)==1:
            return [strs]
        
        res=[]
        check=defaultdict(list)
        for word in strs:
            key=[0]*26
            for c in word:
                key[ord(c)-ord('a')]+=1
            
            check[tuple(key)].append(word)
        
        for keys,words in check.items():
            res.append(words)
        return res

        
        