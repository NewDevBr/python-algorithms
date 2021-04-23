from decimal import Decimal
print("******** Saída da função de segundo grau ********")
param = Decimal(input("Digite o valor do parâmetro: "))
result = (param**2) + (5 * param) - 4
print("A saída da função é: ", result)