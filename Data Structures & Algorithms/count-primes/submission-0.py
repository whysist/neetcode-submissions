class Solution:
    def countPrimes(self, n: int) -> int:
        if n<3:
            return 0
        # limit=n-1
        arr=[True]*(n)
        arr[0]=arr[1]=False
        # p=2
        for p in range(2,int(n**(0.5))+1):
            if arr[p]:
                for i in range(p*p,n,p):
                    arr[i]=False

        # print(arr)
        return arr.count(True)

