from decimal import Decimal
import math
print("******** Calcule o volume de uma esfera ********")

r = Decimal(input("Digite o raio da esfera: "))
r = (4/3) * (math.pi) * (math.pow(r,3))
print("O volume da esfera é: ", r)
