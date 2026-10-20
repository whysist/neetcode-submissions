class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i,j=0,0
        while i<len(word) and j<len(abbr):
            if abbr[j]=='0':
                return False
            
            if abbr[j].isalpha():
                if word[i]!=abbr[j]:
                    return False
                i+=1
                j+=1
            
            else:
                subLen=0
                while j<len(abbr) and abbr[j].isdigit():
                    subLen=subLen*10 + int(abbr[j])
                    j+=1
                i+=subLen
        return i==len(word) and j==len(abbr)
                
        