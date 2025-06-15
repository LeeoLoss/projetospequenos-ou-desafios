from random import sample
# Criando uma lista de frutas disponíveis
frutas = ['Maçãs', 'Banana', 'Uva', 'Pêra', 'Manga', 'Coco', 'Melancia',
          'Mamão', 'Laranja', 'Abacaxi', 'Kiwi', 'Ameixa']

# Selecionando aleatoriamente 3 frutas diferentes (sem repetições)
salada = sample(frutas, k=3)
# Imprimindo as frutas geradas de forma aleatória
print(f'A salada surpresa é: {salada[0]}, {salada[1]}, {salada[2]}. Aproveite!')
