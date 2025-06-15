# Definindo a quantidade de gols feitos e sofridos
gols_marcados = [2, 1, 3, 1, 0]
gols_sofridos = [1, 2, 2, 1, 3]

# Calculando a quantidade de pontos e o aproveitamento
def calcula_pontos(gols_marcados, gols_sofridos):
  pontos = 0
  for i in range(len(gols_marcados)):
    if gols_marcados[i] > gols_sofridos[i]:
      pontos += 3
    elif gols_marcados[i] == gols_sofridos[i]:
      pontos += 1
  aprov = 100 * pontos / (len(gols_marcados) * 3)
  return (pontos, aprov)

# Informando o resultado final
pontos, aprov = calcula_pontos(gols_marcados, gols_sofridos)
print(f"A pontuação do time foi de {pontos} e seu aproveitamento foi de {round(aprov)}%")
