
import random
class RandomizedSet(object):

    def __init__(self):
        self.pos = {}
        self.arr = []
       

    def insert(self, val):
        if val in self.pos:
            return False 
        else:
            self.arr.append(val)
            self.pos[val] = len(self.arr) - 1
            return True 

        #[10, 20, 30]
    
        

    def remove(self, val):
        if val not in self.pos:
            return False 
        else:
            index = self.pos[val]
            last = self.arr[-1]
            self.arr[index] = last
            self.pos[last] = index
            self.arr.pop()
            del self.pos[val]
            return True 

        
        

    def getRandom(self):
        return random.choice(self.arr)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
