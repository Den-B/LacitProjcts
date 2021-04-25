class Point():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def getXY(self):
        return [self.x,self.y]

    def Show(self):
        print("X: ",self.x,",Y: ",self.y)

    def __add__(self,other):
        return Point(self.x+other.x,self.y+other.y)

a = Point(1,2)
b = Point(3,4)
c = a+b
c.Show()
