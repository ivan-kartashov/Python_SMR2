num1 = int(input("Introduzca el primer número: "))

num2 = int(input("Introduzca el segundo número: "))

suma = num1 + num2 #También se puede hacer con el sum.

mult = num1 * num2

if num1 > num2:
    mayor=True
else:
    mayor=False

assert suma == 8
assert mult == 15
assert mayor == True
#Numeros usados en el assert son el num1= 5 y num2= 3