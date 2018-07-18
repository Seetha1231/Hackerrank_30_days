class Student(Person):
    def __init__(self,first,last,id,scores):
        self.p=Person(first,last,id)
        self.sc=scores
    def printPerson(self):
        self.p.printPerson()
    def calculate(self):
        sum=0
        for i in self.sc:
            sum+=i
        gn=sum//len(self.sc)
        if gn>=90 and gn<=100:
            g='O'
        elif gn>=80 and gn<90:
            g='E'
        elif gn>=70 and gn<80:
            g='A'
        elif gn>=55 and gn<70:
            g='P'
        elif gn>=40 and gn<55:
            g='D'
        else:
            g='T'
        return g
