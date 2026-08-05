from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs)==1:
            return [strs]
        
        res=[]
        def makeFmap(s):
            ans=[0]*26
            for x in s:
                ans[ord(x)-ord('a')]+=1
            return tuple(ans)
        
        check=defaultdict(list)
        for word in strs:
            key=makeFmap(word)
            check[key].append(word)
        for keys,words in check.items():
            res.append(words)
        return res

        
        