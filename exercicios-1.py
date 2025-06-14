## 1 - informando o nome a idade e, em seguida, o código retorna com as seguintes informações dentro de uma única frase
nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))

if nome and idade:
    idade = idade
    print(f'Seu nome é {nome} e você tem {idade} anos.')
else:
    print('Dados inválidos. Preencha corretamente.')


## 2 - informa o nome e o código o retorna invertido
nome = input('Informe seu nome: ')
nome_invertido = nome[::-1]
print(f'Seu nome invertido é {nome_invertido}')


## 3 - verifica se o nome contém espaçamentos em branco. Caso haja, retorna ao usuário a mensagem de nome inválido
nome = input('Digite seu nome:')
if ' ' in nome:
    print('Nome inválido. Contém espaços em branco, digite novamente.')
else:
    print('Dados válidos. Seu nome é:', nome)


## 4 - informa ao usuário a quantidade de letras que o seu nome possui
nome = input('Digite seu nome: ')
print(f'Seu nome contém {len(nome)} letras')


## 5 - informa ao usuário a última letra de seu nome. Caso não seja informado algum nome, o código retornará com uma mensagem de erro
nome = input('Digite seu nome: ')
if nome:
    print(f'A última letra do seu nome é: {nome[-1]}')
else:
    print('Nome não informado. Digite novamente.')
