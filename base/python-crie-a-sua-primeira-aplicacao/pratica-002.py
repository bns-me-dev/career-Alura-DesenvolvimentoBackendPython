print('=== Prática 002 ===')
refUser = 'bns-me-dev'
refSenha = 123456

num1 = int(input('1 - Digite um número inteiro: '))
if num1 % 2 == 0:
    print(f'O número {num1} é par.')
else:
    print(f'O número {num1} é ímpar.')

idade = int(input('\n2 - Digite sua idade: '))
if 0 <= idade <= 12:
    print('Você é uma criança.')
elif 13 <= idade <= 18:
    print('Você é um adolescente.')
elif 18 < idade:
    print('Você é um adulto.')
else :
    print('Idade inválida.')

print('\n3 - ')
usuario = input('   Digite seu usuário: ')
senha = int(input('   Digite sua senha: '))
if usuario == refUser and senha == refSenha:
    print('Acesso permitido.')
else:
    print('Acesso negado.')

print('\n4 - ')
x = int(input('   Insira a coordenada x: '))
y = int(input('   Insira a coordenada y: '))
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