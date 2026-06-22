class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=len(numbers)
        L,R=0,n-1
        ans=[]
        while L<R:
            if numbers[L]+numbers[R]==target:
                ans.append(L+1)
                ans.append(R+1)
                break
            elif numbers[L]+numbers[R]>target:
                R-=1
            else:
                L+=1
        return ans
        
        