from math import sqrt

numeros = [2, 8, 15, 23, 91, 112, 256]

# Iniciando uma lista vazia para receber as raízes dos números contidos na lista
raiz = []

# Calculando cada raiz da lista de números e adicionado a lista raiz
for numero in numeros:
  raiz.append(sqrt(numero))

# Lendo a raiz e exibe um texto apenas quando a raiz for de um valor inteiro
for i in range(len(raiz)):

  # Validando se o número é inteiro
  if raiz[i] // 1 == raiz[i]:
    print(f'O número {numeros[i]} possui raiz quadrada inteira igual a {int(raiz[i])}')
