lista1 = []
lista2 = []
lista3 = []
dic = {}

def adcLista1(lista):
    global lista1
    for elemento in lista:
        lista1.append(elemento)
    return lista1

def adcLista2(nome, notas):
    global lista2
    
    tupla = (nome,notas)
    lista2.append(tupla)
    
    return lista2

def adcLista3(nome, notas):
    global lista3
    
    aluno = {}
    aluno['nome'] = nome
    aluno['notas'] = notas
    
    lista3.append(aluno)
    return lista3
        
def adcDicionario(nome,notas):
    global dic
    
    dic[nome] = notas
    
    return dic
    
while True:
    nome = input("Digite o nome do aluno: ")
    nota1 = float(input('nota 1: '))
    nota2 = float(input('nota 2: '))
    nota3 = float(input('nota 3: '))
    
    li = [nome,nota1,nota2,nota3]
    notas = [nota1,nota2,nota3]
    
    lista1 = adcLista1(li)
    lista2 = adcLista2(nome,notas)
    lista3 = adcLista3(nome,notas)
    dic = adcDicionario(nome,notas)
    
    op = input('deseja inserir mais um aluno(s ou n): ')
    if op != 's':
        break

print(f'lista formarto 1: {lista1}')
print(f'lista formato 2: {lista2}')
print(f'lista formato 3: {lista3}')
print(f'dicionario: {dic}')
print('\n')

print('-----lista formato 1-----')
for i,elemento in enumerate(lista1):
    if i%4 == 0:
        print(f'nome: {elemento} \nnotas:',end='')
    elif i%4 == 1 or i%4 == 2:
        print(f'{elemento},',end=' ')
    elif i%4 == 3:
        print(f'{elemento}\n')

print('-----lista formato 2-----')
for tupla in lista2:
    print(f'nome: {tupla[0]} \nnotas: {tupla[1]}\n')
    
print('-----lista formato 3-----')
for pessoa in lista3:
    print(f'nome: {pessoa['nome']} \nnotas: {pessoa['notas']}\n')
    
print('-----dicionario-----')
for nome in dic:
    print(f'nome: {nome} \nnotas: {dic[nome]}\n')   

