from collections import defaultdict
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        p=s.split(' ')
        # print(p)
        d=defaultdict(str)
        if len(p)!=len(pattern):
            return False
        vis={}
        for i in range(len(pattern)):
            ch=pattern[i]
            word=p[i]
            if word in vis:
                if vis[word]!=ch:
                    return False
                else:
                    continue
            elif ch in vis.values():
                return False
            else:
                vis[word]=ch
                
        return True