from collections import defaultdict
from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord==endWord or endWord not in wordList:
            return 0
        def checkDiff(w1,w2):
            diff=0
            for i in range(len(w1)):
                if w1[i]!=w2[i]:
                    diff+=1
            return diff
        
        adj=defaultdict(list)
        
        for word in wordList:
            if checkDiff(beginWord,word)==1:
                adj[beginWord].append(word)
                # adj[word].append(beginWord)
            
        print(adj)
        for i in range(len(wordList)-1):
            for j in range(i+1,len(wordList)):
                if (checkDiff(wordList[i],wordList[j])==1):
                    adj[wordList[i]].append(wordList[j])
                    adj[wordList[j]].append(wordList[i])
        print(adj) 
        q=deque([(beginWord,1)])
        vis=set([beginWord])
        
        while q:
            w,steps=q.popleft()
            if w==endWord:
                return steps
            for neigh in adj[w]:
                if neigh not in vis:
                    vis.add(neigh)
                    q.append((neigh,steps+1))
        return 0

            
                    
        