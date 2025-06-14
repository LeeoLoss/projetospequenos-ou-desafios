## 1
# O código verifica se o número informado pelo usuário é par ou ímpar e se é um número inteiro.

try:
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        print(f'O número {numero} é par.')
    else:
        print(f'O número {numero} é ímpar.')     
except: Retorna a mensagem de erro caso o usuário não digite um número inteiro
    print('Entrada inválida. Por favor, digite um número inteiro.')


## 2 
# O usuário informa o horário atual e exibe uma mensagem de saudação baseada no período do dia.
try:
    horario = int(input('Digite o horário atual: '))
    if horario > 0 and horario <= 11:
        print('Bom dia!')
    elif horario >= 12 and horario <= 17:
        print('Boa tarde!')
    elif horario >= 18 and horario <= 23:
        print('Boa noite!')
    else:
        print('Horário inválido. Por favor, digite um horário entre 0 e 23.')
except: ## Retorna a mensagem de erro caso o usuário não digite um número inteiro
    print('Informação inválida. Por favor, digite um número inteiro.')

## 3
# O código verifica o nome informado pelo usuário e classifica seu tamanho, além de validar se contém apenas letras.
nome = input('Digite seu nome: ')
tamanho = len(nome)

if not nome.isalpha() or tamanho <= 2:
    print('O nome não pode conter números ou caracteres especiais. Digite mais de duas letras.')
elif tamanho <= 4:
    print('Seu nome é curto.')
elif tamanho >= 5 and tamanho <= 6:
    print('Seu nome é normal.')
else:
    print('Seu nome é muito grande.')

