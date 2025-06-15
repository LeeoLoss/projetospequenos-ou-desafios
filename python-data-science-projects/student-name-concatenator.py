# Nomes dos estudantes
nomes = ["leonardo", "IonArA", "JOSÉ"]
sobrenomes = ["LOSS", "silva", "Delfino"]

# Função lambda que recebe duas listas e itera em cada uma concatenando seu nome e sobrenome
nome_completo = map(lambda nome, sobrenome: f'{nome.title()} {sobrenome.title()}', nomes, sobrenomes)

# Leitura do objeto mapa(iterável)
for n in nome_completo:
  print(f'Nome completo: {n}')

