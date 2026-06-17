from collections import defaultdict
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums)==1:
            return False
        
        hashmap=defaultdict(int)
        for i in range(len(nums)):
            if nums[i] in hashmap:
                print(nums[i],hashmap,i)
                if i - hashmap[nums[i]] <= k:
                    return True
                else:
                    hashmap[nums[i]]=i
            else:
                hashmap[nums[i]]=i
            # print(hashmap,i)
        return False



        