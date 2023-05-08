# programa para calcular el índice de masa corporal de una persona
print("-----------------------------------")
print("-----indice de masa corporal-------")
print("-----------------------------------")


# input
m=float(input("digite el peso de la persona (kg): "))
p=float(input("digite la altura de la persona (m): "))

# processing
imc=float((m)/(p**2))
if imc<16:
    msj=("Criterio de ingreso en hospital")
else:
    if imc>=16 and imc<17:
        msj=("Infrapeso")
    else:
        if imc>=17 and imc<18:
             msj=("bajo peso")
        else:
            if  imc>=18 and imc<25:
                msj=("peso normal") 
            else:
                if imc>=25 and imc<30:
                    msj=("Sobrepeso (obesidad de grado I)")
                else:
                    if  imc>=30 and imc<35:
                        msj=("Sobrepeso crónico (obesidad de grado II)")
                    else:
                        if imc>=35 and imc<=40:
                            msj=("Obesidad premórbida (obesidad de grado III)")
                        else:
                            if imc>40:
                                msj=("Obesidad mórbida (obesidad de grado IV)")

# input

print("")
print("------------------")
print("resultados del imc")
print("------------------")
print("")
print("el imc de la persona es: ")
print("")
print(imc)
print(msj)
