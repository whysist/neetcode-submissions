class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0:
            return False
        if n==1:
            return True
        binary=str(bin(n))
        print(binary)
        return binary.count('1')==1

        