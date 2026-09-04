class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num<2:
            return True
        if num==2:
            return False
        x=2
        while x*x<=num:
            if (x*x==num):
                return True
            x+=1
        return False
        