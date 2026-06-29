class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s)==1:
            return 1
        s=s.strip()
        # print(s)
        lst=list(s.split(' '))
        return len(lst[-1])

        