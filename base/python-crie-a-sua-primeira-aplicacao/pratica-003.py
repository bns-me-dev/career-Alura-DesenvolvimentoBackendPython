from datetime import date

list1 =[1,2,3,4,5,6,7,8,9,10]
list2 = ['Bruno','Davi','Enzo','Paulinho']
list3 = [2001, date.today().year]

print('1 - Crie uma lista para cada informação a seguir:\n    -Lista de números de 1 a 10\n    -Lista com quatro nomes\n    -Lista com o ano que você nasceu e o ano atual.\n')
print('Lista1:', list1)
print('Lista2:', list2)
print('Lista3:', list3)

print('\n2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.\n')
for i, v in enumerate(list1):
    print(f'Lista1[{i}] = {v}')

print('\n3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.\n')
soma = 0
for i in range (1, 11):
    if i % 2 != 0:
        soma += i
print(f'Soma dos valores ímpares de 1 a 10: {soma}')

print('\n4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.\n')
for i in range (10, 0, -1):
    print('Valor: ', i)

print('\n5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.\n')
num = int(input('Digite um número: '))
print(f'     Tabuada de {num}:')
for i in range(1, 11):
    print(f'     {num} x {i} = {i * num}')

print('\n6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções\n')
soma = 0
try:
    for i, v in enumerate(list1):
            soma += v
    print(f'Soma dos valores da lista {list1}: {soma}')
except Exception as e:
    print(f'Ocorreu um erro: {e}')

print('\n7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.\n')
soma = 0
try:
    for i, v in enumerate(list1):
        soma += v
    media = soma / len(list1)
    print(f'Média dos valores da lista {list1}: {media}')
except ZeroDivisionError:
    print('Erro: Lista vazia - Divisão por zero não é permitida.')
except Exception as e:
    print(f'Ocorreu um erro: {e}')