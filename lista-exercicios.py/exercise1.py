## 1 - solicitando o nome e a idade e, em seguida, o código informa o nome e a idade definidos pelo usuário. Em caso de não preenchimento, uma mensagem de erro é enviada.
nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))


if nome and idade:
    idade = idade
    print(f'Seu nome é {nome} e você tem {idade} anos.')
else:
    print('Dados inválidos. Preencha corretamente.')


## 2 - solicita o nome ao usuário e retorna o retorna de forma invertida
nome = input('Informe seu nome: ')
nome_invertido = nome[::-1]
print(f'Seu nome invertido é {nome_invertido}')


## 3 - verifica se o nome informado pelo usuário contém espaços em brancos. se sim, é enviada uma mensagem de erro
nome = input('Digite seu nome:')
if ' ' in nome:
    print('Nome inválido. Contém espaços em branco, digite novamente.')
else:
    print('Dados válidos. Seu nome é:', nome)


## 4 - informa ao usuário a quantidade de letras que seu nome possui
nome = input('Digite seu nome: ')
print(f'Seu nome contém {len(nome)} letras')


## 5 - retorna ao usuário com a quantidade de letras que o seu nome detém
nome = input('Digite seu nome: ')
if nome:
    print(f'A última letra do seu nome é: {nome[-1]}')
else:
    print('Nome não informado. Digite novamente.')
