class Solution:
    def countOdds(self, low: int, high: int) -> int:
        n=(high-low)+1
        return n//2 if (low%2==0 or high%2==0) else (n//2 + 1)

        