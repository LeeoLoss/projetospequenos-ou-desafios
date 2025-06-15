# Solicita ao usuário o número de diárias da viagem
dias = int(input("Quantas diárias? "))

# Solicita ao usuário a cidade de destino
cidade = input("Qual a cidade? [Salvador, Fortaleza, Natal ou Aracaju]: ")

# Lista com as distâncias de cada cidade
distancias = [850, 800, 300, 550]

# Lista com o custo diário de passeios em cada cidade
passeio = [200, 400, 250, 300]

# Consumo do carro (km por litro)
km_l = 14

# Preço do litro da gasolina (R$)
gasolina = 5

# Calcula o custo do hotel com base no número de diárias
def gasto_hotel(dias):
    return 150 * dias  # R$ 150 por diária

# Calcula o gasto com gasolina para ida e volta até a cidade escolhida
def gasto_gasolina(cidade):
    if cidade == "Salvador":
        return (2 * distancias[0] * gasolina) / km_l  # Ida e volta
    elif cidade == "Fortaleza":
        return (2 * distancias[1] * gasolina) / km_l
    elif cidade == "Natal":
        return (2 * distancias[2] * gasolina) / km_l
    elif cidade == "Aracaju":
        return (2 * distancias[3] * gasolina) / km_l

# Calcula o gasto total com passeios com base na cidade e nos dias
def gasto_passeio(cidade, dias):
    if cidade == "Salvador":
        return passeio[0] * dias
    elif cidade == "Fortaleza":
        return passeio[1] * dias
    elif cidade == "Natal":
        return passeio[2] * dias
    elif cidade == "Aracaju":
        return passeio[3] * dias

# Soma todos os gastos: hotel + gasolina + passeios
gastos = gasto_hotel(dias) + gasto_gasolina(cidade) + gasto_passeio(cidade, dias)

# Exibe o custo total estimado da viagem
print(f"Com base nos gastos definidos, uma viagem de {dias} dias para {cidade} saindo de Recife custaria {round(gastos, 2)} reais")
