class Snow():
    def __init__(self,count):
        self.count=int(count)

    def __add__(self,n): 
        self.count=self.count+n
        print(self.count)

    def __sub__(self,n): 
        self.count=self.count-n
        print(self.count)

    def __mul__(self,n): 
        self.count=self.count*n
        print(self.count)

    def __truediv__(self,n): 
        self.count=round(self.count/n)
        print(self.count)

    def makeSnow(self,k):
        for x in range(0,int(self.count/k)):
            print(k*"*"+"\n")
        else:
            print("*"*(self.count-k*int(self.count/k)))
