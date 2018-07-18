class Calculator:
    def power(self,a,b):
        if(a<0 or b<0):
            raise Exception("n and p should be non-negative")
        else :
            p=1
            for i in range(b):
                p=p*a
            return p
