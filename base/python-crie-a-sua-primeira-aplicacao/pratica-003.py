from datetime import date
print('=== Prática 003 ===')
list1 =[1,2,3,4,5,6,7,8,9,10]
list2 = ['Bruno','Davi','Enzo','Paulinho']
list3 = [2001, date.today().year]

print('1 - ')
print('     Lista1:', list1)
print('     Lista2:', list2)
print('     Lista3:', list3)

print('\n2 - ')
for i, v in enumerate(list1):
    print(f'     Lista1[{i}] = {v}')

print('\n3 - ')
soma = 0
for i in range (1, 11):
    if i % 2 != 0:
        soma += i
print(f'     Soma dos valores ímpares de 1 a 10: {soma}')

print('\n4 - ')
for i in range (10, 0, -1):
    print('     Valor: ', i)

print('\n5 - ')
num = int(input('     Digite um número: '))
print(f'     Tabuada de {num}:')
for i in range(1, 11):
    print(f'     {num} x {i} = {i * num}')

print('\n6 - ')
soma = 0
try:
    for i, v in enumerate(list1):
            soma += v
    print(f'     Soma dos valores da lista {list1}: {soma}')
except Exception as e:
    print(f'     Ocorreu um erro: {e}')

print('\n7 - ')
soma = 0
try:
    for i, v in enumerate(list1):
        soma += v
    media = soma / len(list1)
    print(f'     Média dos valores da lista {list1}: {media}')
except ZeroDivisionError:
    print('     Erro: Lista vazia - Divisão por zero não é permitida.')
except Exception as e:
    print(f'     Ocorreu um erro: {e}')