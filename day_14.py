class Difference:
    def __init__(self, a):
        self.__elements = a
    def computeDifference(self):
        max=-1
        l=len(self.__elements)
        for i in range(l):
            for j in range(i+1,l):
                if max<abs(self.__elements[i]-self.__elements[j]):
                    max=abs(self.__elements[i]-self.__elements[j])
        self.maximumDifference=max
    def maximumDifference(self):
        return self.maximumDifference
        
_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
