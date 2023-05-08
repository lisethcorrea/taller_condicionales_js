# programa Programa que permita realizar un préstamo bancario

print("-------------------------------------------")
print("programa para realizar un prestamo bancario")
print("-------------------------------------------")



# input
ing=int(input("digite sus ingresos mensuales: "))
deu=int(input("digite su número de deudas: "))

# processing
if ing>945000:
    if deu==0:
        rta=("prestamo aprobado")
    else:
        rta=("prestamo no aprobado")
else:
    rta=("prestamo no aprobado")

# output


print("")
print("-----------------------")
print("resultados del prestamo")
print("-----------------------")
print("")
print(rta)