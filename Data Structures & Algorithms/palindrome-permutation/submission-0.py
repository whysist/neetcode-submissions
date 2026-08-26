from collections import Counter
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        count=Counter(s)
        num_odd=0
        for x in count:
            if count[x]%2!=0:
                num_odd+=1
                if num_odd>1:
                    return False
            else:
                continue
        return True
            
        