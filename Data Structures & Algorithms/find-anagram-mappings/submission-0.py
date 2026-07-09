from collections import defaultdict
class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d=defaultdict(int)
        for i,x in enumerate(nums2):
            d[x]=i
        for i in range(len(nums1)):
            nums1[i]=d[nums1[i]]
        return nums1
        