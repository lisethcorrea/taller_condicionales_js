# ecuaciones cuadraticas
import math 
## input
a=int(input("digite el valor de a: "))
b=int(input("digite el valor de b: "))
c=int(input("digite el valor de b: "))

#processing



d=(b**2 -4*a*c)

if d==0:
    x1= -b/(2*a)
    x2=x1
    print (x1, x2)
    print("son raices iguales")

if d>0:
    x1= (-b+math.sqrt(d))/2*a
    x2= (-b-math.sqrt(d))/2*a
    print (x1, x2)
    print("son raices diferentes")

else:
    print("son raices imaginarias")