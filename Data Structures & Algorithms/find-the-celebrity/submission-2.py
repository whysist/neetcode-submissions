# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        # for a single call, if akb is true then there's a chance b is the celeb and not a
        # if akb is false then a might be a celeb and not b

        #so for i,i+1 if iki+1 is true then celeb=i+1
        # if iki+1 is false then celeb=i

        candidate=0
        for i in range(n):
            if knows(candidate,i):
                candidate=i
        for j in range(n):
            if candidate!=j:
                if knows(candidate,j) or not knows(j,candidate):
                    return -1
        return candidate
            