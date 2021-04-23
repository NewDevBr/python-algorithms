from decimal import Decimal

print("******** Média de 5 números ********")
med = Decimal(0)
for x in range(5):
    med += Decimal(input("Digite um número: "))
med = med/5
print("A média artimética simples desses 5 números é: ", med)