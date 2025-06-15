# Importando a bibiloteca e seus métodos
from math import pi, pow

raio = float(input('Digite o raio da área circular em metros: '))

# Calculando a área e o custo em reais com os métodos da biblioteca math
area = pi * pow(raio, 2)
valor = area * 25.0

# Exibindo o cálculo e custo na tela
print(f'Você vai precisar pagar R${round(valor, 2)} por uma área de {round(area, 2)} metros de grama.')
