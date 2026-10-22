from collections import defaultdict,OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        
        self.cache=OrderedDict()
        self.cap=capacity
        # self.lookup=defaultdict(int)
        # self.t=0

    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache.move_to_end(key=key)
            return self.cache[key]
        else:
            return -1       

    def put(self, key: int, value: int) -> None:
        # print(self.cache,self.lookup)
        if key in self.cache:
            self.cache[key]=value
            self.cache.move_to_end(key=key)
        else:
            n=len(self.cache)
            if n==self.cap:
                self.cache.popitem(last=False)
            
            self.cache[key]=value
            self.cache.move_to_end(key=key)
        # print(self.cache,self.lookup)



        
