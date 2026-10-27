print('1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.\n')
refDicionario1 = {'nome':'Bruno', 'idade': 24, 'cidade':'Salvador'}

print('\n2 - Utilizando o dicionário criado no item 1:\n    -Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa)\n    -Adicione um campo de profissão para essa pessoa\n    -Remova um item do dicionário.\n')
refDicionario1['idade'] = 25
refDicionario1['profissao'] = 'Desenvolvedor & Engenheiro'    
del refDicionario1['cidade']

print('\n3 - Crie um dicionário que relacione os números de 1 a 5 aos seus respectivos quadrados.\n')
dicionario2 = {f'Item_{i}': i**2 for i in range(1,6)}

print('\n4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.\n')
if 'cidade' in refDicionario1:
    print(f'A chave cidade existe no dicionário {refDicionario1}.')
elif 'nome' in refDicionario1:
    print(f'A chave "nome" existe no dicionário {refDicionario1}')
else:
    print('A chave não existe no dicionário')

print('\n5 - Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.\n')
texto = 'Atividade prática realizada em 20/10/2026 - 05:31'
defContLetras= {}
letras = texto.split()
for l in letras:
    defContLetras[l] = defContLetras.get(l, 0) + 1
print(f'Frequência de letras na frase "{texto}" : \n {defContLetras}')