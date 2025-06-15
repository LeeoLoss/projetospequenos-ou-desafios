# Requisitando uma frase e separando-a pelos espaços. Usando replace para trocar pontuações por espaço.
frase = input("Digite uma frase: ")
frase = frase.replace(',',' ').replace('.',' ').replace('!',' ').replace('?',' ').split()

# Filtrando a frase no formato de lista, passando para a lista tamanho apenas as palavras com 5 ou mais caracteres e imprimindo-a na tela
tamanho = list(filter(lambda x: len(x) >= 5, frase))
print(tamanho)
