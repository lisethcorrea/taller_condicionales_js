# programa para mirar si dados 3 numeros, la suma de los 2 primeros es igual al tercero
print("------------------------------")
print("-----digite los numeros-------")
print("------------------------------")
# input

a=int(input("digite el primer numero entero: "))
b=int(input("digite el segundo numero entero: "))
c=int(input("digite el tercer numero entero: "))



# processing
p1=a+b
p2=a+c
p3=b+c
if p1 ==c:
    suma=("la suma de: " + str(c) + " es: " + str (a)  + " + " + str(b))
else:
    if p2 == b:
        suma=("la suma de: " + str(b) + " es: " + str (a) + " + " + str(c))
    else:
        if p3 == a:
         suma=("la suma de: " + str(a) + " es: " + str (b)  + " + " + str(c))
        else:
           suma=("la suma no equivale a otro entero de la suma")

# output
print("")
print(suma)