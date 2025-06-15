from math import sqrt

numeros = [2, 8, 15, 23, 91, 112, 256]

raiz = []

for numero in numeros:
  raiz.append(sqrt(numero))

for i in range(len(raiz)):

  if raiz[i] // 1 == raiz[i]:
    print(f'O número {numeros[i]} possui raiz quadrada inteira igual a {int(raiz[i])}')
