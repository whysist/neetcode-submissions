from collections import defaultdict
class Solution:
    def countElements(self, arr: List[int]) -> int:
        s=set(arr)
        c=0
        for num in arr:
            if num+1 in s:
                c+=1
        return c