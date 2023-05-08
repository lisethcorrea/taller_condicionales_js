# programa para definir el precio a pagar de la factura del agua
print("-----------------------------")
print("-----digite su consumo-------")
print("-----------------------------")
# input

co=int(input("digite su consumo: "))


# processing
cf=10000

if co<=50:
    total_pagar= cf
else:
    if co<=200:
        total_pagar= cf + 2000*(co-50)
    else:
        if co>200:
         total_pagar=cf + 3000*(co-50)
        
  

# output


print("")
print("----------------------------")
print("este es el valor de su factura")
print("-----------------------------")
print("")
print(total_pagar)