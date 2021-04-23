from decimal import Decimal
print("******** calculo da saída de função ********")
x = Decimal(input("Digite o valor do parâmetro: "))
fAfim = 2 * x + 1
fPoli = (x ** 3) - 2 * (x ** 2) + x - 1
print("Resultado função afim: ", fAfim, " resultado função polinomial: ", fPoli)