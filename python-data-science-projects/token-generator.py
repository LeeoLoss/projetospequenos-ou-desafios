# Importando a biblioteca randon e o seu método randrange
from random import randrange

nome = input('Qual é o seu nome? ')

# Geração de um token par de 1000 a 9998
token = randrange(1000, 10000, 2)
print(f'Olá, {nome}! O seu token de acesso é {token}! Seja bem-vindo(a).')
