class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_map=[0]*26
        sliding_map=[0]*26
        if len(s2)<len(s1):
            return False
        if len(s1)==len(s2):
            return Counter(s1)==Counter(s2)
        for ch in s1:
            s1_map[ord(ch)-ord('a')]+=1
        k=len(s1)
        for i in range(k):
            sliding_map[ord(s2[i])-ord('a')]+=1
    
        s,e=0,k-1
        N=len(s2)
        while e<N:
            if sliding_map==s1_map:
                return True
            sliding_map[ord(s2[s])-ord('a')]-=1
            s+=1
            e+=1
            if e<N:
                sliding_map[ord(s2[e])-ord('a')]+=1
        return False
        
        