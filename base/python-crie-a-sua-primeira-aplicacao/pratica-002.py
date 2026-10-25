refUser = 'bns-me-dev'
refSenha = 123456

print('\n1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.\n')
num1 = int(input('Digite um número inteiro: '))
if num1 % 2 == 0:
    print(f'O número {num1} é par.')
else:
    print(f'O número {num1} é ímpar.')

print('\n2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:\n    - Criança: 0 a 12 anos\n    - Adolescente: 13 a 18 anos\n    - Adulto: acima de 18 anos\n')
idade = int(input('Digite sua idade: '))
if 0 <= idade <= 12:
    print('Você é uma criança.')
elif 13 <= idade <= 18:
    print('Você é um adolescente.')
elif 18 < idade:
    print('Você é um adulto.')
else :
    print('Idade inválida.')

print('\n3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.\n')
usuario = input('Digite seu usuário: ')
senha = int(input('Digite sua senha: '))
if usuario == refUser and senha == refSenha:
    print('Acesso permitido.')
else:
    print('Acesso negado.')

print('\n4 - Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else para determinar em qual quadrante do plano cartesiano o ponto se encontra.\n')
x = int(input('Insira a coordenada x: '))
y = int(input('Insira a coordenada y: '))
if x > 0 and y > 0:
    print('O ponto está no 1º quadrante.')
elif x < 0 and y > 0:
    print('O ponto está no 2º quadrante.')
elif x < 0 and y < 0:
    print('O ponto está no 3º quadrante.')
elif x > 0 and y < 0:
    print('O ponto está no 4º quadrante.')
else:
    print('O ponto está na origem.')

