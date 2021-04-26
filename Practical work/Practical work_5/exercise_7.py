class Human():
    default_name = "Jhon"
    default_age = 32

    def __init__(self,age = default_age,name=default_name):
        self.name = name
        self.age = age
        self.__money = 0
        self.__property = []
    
    def info(self):
        print(self.name,self.age,self.__money,self.__property)
        return (self.name,self.age,self.__money,self.__property)

    def default_info(self):
        print(Human.default_name,Human.default_age)
        return (Human.default_name,Human.default_age)

    def make_deal(self,prop,deal):
        if((self.__money-deal)>=0):
            self.__money=self.__money-deal
            self.__property.append(prop)
            print(self.__money)
        else:
            print("Недостаточно денег")

    def earn_money(self,deal):
        self.__money=self.__money+deal

    def buy(self,deal):
        if((self.__money-deal)>=0):
            self.__money=self.__money-deal
            print(money)
        else:
            print("Недостаточно денег")

    def __ge__(self,other):
        checker = (len(self.name)+self.age)>=(len(other.name)+other.age)
        print(checker)
        return checker

    def __iadd__(self,other):
        self.__money=self.__money+int(other)
        print(self.__money)
        return self


    def __isub__(self,other):
        self.__money=self.__money-int(other)
        print(self.__money)
        return self

    def __imul__(self,other):
        self.__money=self.__money*int(other)
        print(self.__money)
        return self

    def __itruediv__(self,other):
        self.__money=self.__money/int(other)
        print(self.__money)
        return self

    

a = Human(41,"Jack")
a.default_info()
a.earn_money(100)
a.make_deal("House",100)
a.buy(10)
a.info()
b = Human(40,"Julian")
a>=b
a+=19
a-=6
a*=8
a/=10
