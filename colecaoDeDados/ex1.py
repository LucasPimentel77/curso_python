lista = []
par = []
impar = []
negativos = []
maior = []

for i in range(10):
    x = int(input(f'numero {i+1}: '))
    lista.append(x)
    if x % 2 == 0:
        par.append(x)
    else:
        impar.append(x)
    if x < 0:
        negativos.append(x)

media = sum(lista)/ len(lista)

for i in range(len(lista)):
    if lista[i] > media:
        maior.append(lista[i])
        
print(f'numeros pares: {par}')
print(f'numeros impares: {impar}')
print(f'numeros negativos: {negativos}')
print(f'numeros maior que a media ({media}): {maior}')