"""Programa para 
comparar numeros pares e impares"""



print("--------------------------------")
print("-------- Pares e impares -------")
print("--------------------------------")
# Imput
n = int(input("Ingrese un número entero y positivo: "))
# Processing
par = 0
impar = 0
while n != 0:
    r = n % 2
    if r == 0:
        par = par + 1
    else:
        impar = impar + 1
    Num=0
n = int(input("Ingrese un número entero y positivo: "))
while n != 0:
    r = n % 2
    if r == 0:
        par = par + 1
    else:
        impar = impar + 1
    Num=0
# Output
print("Se ingresaron " + str(par) + " números pares")
print("Se ingresaron " + str(impar) + " números impares")