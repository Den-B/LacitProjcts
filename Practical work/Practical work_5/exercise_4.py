class Point():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def getXY(self):
        return [self.x,self.y]

    def Show(self):
        print("X: ",self.x," ,Y: ",self.y)

    def __add__(self,other):
        return Point(self.x+other.x,self.y+other.y)

    def __sub__(self,other):
        return Point(self.x-other.x,self.y-other.y)

    def __mul__(self,other):
        return Point(self.x*other.x,self.y*other.y)

    def __truediv__(self,other):
        return Point(self.x/other.x,self.y/other.y)

    def __eq__(self,other):
        if self.x==other.x:
            if self.y == other.y:
                return True
            return False
        return False

a = Point(3,5)
b = Point(3,4)
c = a-b
d = a*b
e = a/b
c.Show()
d.Show()
e.Show()
print(a==b)
