import math
#8.1
print(1/2+1/4)
print("\n\n")

#8.2
a = int( input("a= "))
b = int(input("b= "))
z = (a+4*b)*(a-3*b)+a*a
print(z)
print("\n\n")

#8.3
x = int( input("x= "))
z = abs(x)+math.pow(x,5)
print(z)
print("\n\n")

8.5
x = float( input("x= "))
z = math.pow(x+1,2)+3*(x+1)
print(z)
print("\n\n")


#8.5
x = float( input("x= "))
z = (abs(x-5)-math.sin(x))/3+math.sqrt(pow(x,2)+2014)*math.cos(2*x)-3
print(z)
print("\n\n")

#8.6
x = float( input("x= "))
z = pow(math.e,x-2)+abs(math.sin(x))-math.pow(x,4)*math.cos(1/x)
print(z)
print("\n\n")

#8.7
x = float( input("x= "))
a = float( input("a= "))
b = float( input("b= "))
z = math.pow(x*x+b,1/5)-(math.pow(b,2)*math.pow(math.sin(x+a),3)/x)
print(z)
print("\n\n")
