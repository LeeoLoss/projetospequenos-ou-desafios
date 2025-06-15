# Importando a biblioteca e o seu método
from random import randint

# O código solicita ao usuário o número de participantes no sorteio e, com base nessa quantidade, gera um número aleatório para escolher o vencedor.
num = int(input('Digite o número de participantes do sorteio: '))
print(f'O número sorteado foi {randint(1,num)}')
