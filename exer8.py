from decimal import Decimal
import math
print("******** área do circulo ********")
r = Decimal(input("Digite o raio do circulo: "))
r = math.pow(r, 2) * math.pi
print("A área deste circulo é: ",r )