class Solution:
    def __init__(self):
        self.s=[]
        self.q=[]
    def pushCharacter(self,s):
        self.s.append(s)
    def enqueueCharacter(self,q):
        self.q.insert(0,q)
    def popCharacter(self):
        return self.s.pop();
    def dequeueCharacter(self):
        return self.q.pop()
