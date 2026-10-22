from collections import defaultdict
class LRUCache:

    def __init__(self, capacity: int):
        
        self.cache=defaultdict(int)
        self.cap=capacity
        self.lookup=defaultdict(int)
        self.t=0

    def get(self, key: int) -> int:
        if key in self.cache:
            self.t+=1
            self.lookup[key]=self.t
            return self.cache[key]
        else:
            return -1       

    def put(self, key: int, value: int) -> None:
        # print(self.cache,self.lookup)
        if key in self.cache:
            self.cache[key]=value
            self.t+=1
            self.lookup[key]=self.t
        else:
            n=len(self.cache)
            if n==self.cap:
                lowKey,lowLook=None,float('inf')
                for k,ti in self.lookup.items():
                    if ti<lowLook:
                        lowLook=ti
                        lowKey=k
                del self.cache[lowKey]
                del self.lookup[lowKey]
            
            self.cache[key]=value
            self.t+=1
            self.lookup[key]=self.t

        # print(self.cache,self.lookup)



        
