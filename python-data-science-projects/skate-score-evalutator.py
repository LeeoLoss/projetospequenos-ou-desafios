# Declarando a lista de notas
notas = []
# Laço for para pedir as 5 notas e armazená-las na lista notas
for i in range(1,6):
  nota = float(input(f"Digite a {i}ª nota: "))
  notas.append(nota)

# Função para remover a maior e menor nota e retornar a média das notas restantes
def media(lista):
  lista.remove(max(lista))
  lista.remove(min(lista))
  return sum(lista) / len(lista)

# Chamando a função e imprimindo a nota do(a) skatista
media = media(notas)
print(f"Nota da manobra: {round(media, 1)}") 
