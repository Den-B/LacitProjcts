class Point():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def getXY(self):
        print(self.x,self.y)
        return [self.x,self.y]

    def Show(self):
        print("X: ",self.x,",Y: ",self.y)

test=Point(2,7)
test.getXY()
test.Show()
