import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        while k:
            gifts.sort(reverse=True)
            gifts[0]=math.floor(gifts[0]**0.5)
            k-=1
        return sum(gifts)