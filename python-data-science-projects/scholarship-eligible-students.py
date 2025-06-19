# Lista que contém os nomes dos estudantes
nomes_estudantes = [ "Enrico Monteiro", "Luna Pereira", "Anthony Silveira", "Letícia Fernandes", 
                    "João Vitor Nascimento", "Maysa Caldeira", "Diana Carvalho", "Mariane da Rosa",
                    "Camila Fernandes", "Levi Alves", "Nicolas da Rocha", "Amanda Novaes", 
                    "Laís Moraes", "Letícia Oliveira", "Lucca Novaes", "Lara Cunha", 
                    "Beatriz Martins", "João Vitor Azevedo", "Stephany Rosa", "Gustavo Henrique Lima" ]

# Lista que contém as médias dos estudantes
medias_estudantes = [5.4, 4.1, 9.1, 5.3, 6.9, 3.1, 10.0, 5.0, 8.2, 5.5,
                    8.1, 7.4, 5.0, 3.7, 8.1, 6.2, 6.1,5.6,6.7,8.2]

# Calculando a média de cada estudante
# e imprimindo o resultado caso hajam médias >= 9.0
bolsistas = {nome: media
             for nome, media in zip(nomes_estudantes, medias_estudantes)
             if media >= 9.0}

print('Os bolsistas são: ', bolsistas)
