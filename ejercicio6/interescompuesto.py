"""Ejercicio N°6
Programa para calcular el tiempo en duplicar un capital con un interes compuesto del 5%"""

print("-------------------------------------")
print("---------Interes Compuesto-----------")
print("-------------------------------------")

# input

C=int(input("digite el capital: "))
D=C*2
meses=0

while C<D:
    C=C+(0.05*C)
    meses=meses+1
print("En " + str(meses) + " meses, se habra duplicado el capital")