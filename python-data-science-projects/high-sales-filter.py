# Informação da quantidade de vendas por ano
vendas = [('2023', 4093), ('2021', 4320), ('2021', 5959), ('2022', 8883), ('2023', 9859), ('2022', 5141), ('2022', 7688), ('2022', 9544), ('2023', 4794), ('2021', 7178), ('2022', 3030), ('2021', 7471), ('2022', 4226), ('2022', 8190), ('2021', 9680), ('2022', 5616)]

# Criação de uma list comprehension para filtrar valores de 2022 e que as vendas sejam > 6000
vendas_2022 = [venda for ano, venda in vendas if ano == '2022' and venda > 6000]  

# Exibindo a quantidade de vendas > 6000
print(f'Segue abaixo as vendas de 2022 acima de 6000: {vendas_2022}')        
