import math

#1
class Sphere:
    def __init__(self,r = 1,x = 0,y = 0 ,z = 0):
        self.xOfCentre = x
        self.yOfCentre = y
        self.zOfCentre = z
        self.r = r

    def get_volume(self):
        volume = float(4/3*math.pi*pow(self.r,3))
        print(volume)
        return volume

    def get_square(self):
        square = float(4*math.pi*pow(self.r,2))
        print(square)
        return square

    def get_radius(self):
        print(self.r)
        return self.r

    def get_centre(self):
        buff=(self.xOfCentre,self.yOfCentre,self.zOfCentre)
        print(buff)
        return buff


    def set_radius(self,r):
        self.r=r


    def set_centre(self,x,y,z):
        self.xOfCentre = x
        self.yOfCentre = y
        self.zOfCentre = z

    def is_point_inside(self,x,y,z):
        checker=self.r>=math.sqrt(pow(x-self.xOfCentre,2)+pow(y-self.yOfCentre,2)+pow(z-self.zOfCentre,2))
        print(checker)
        return checker

