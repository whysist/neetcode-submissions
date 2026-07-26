class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        n=len(words)
        ans=0
        for i in range(n-1):
            for j in range(i+1,n):
                x=len(words[i])
                s,y=words[j],len(words[j])
                # print(s,x,y)
                if(s[:x]==words[i] and s[(y-x):]==words[i]):
                    ans+=1
        return ans
        