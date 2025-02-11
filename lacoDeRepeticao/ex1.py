lista = []
for i in range(10):
    i = int(input(f'numero {i+1}: '))
    lista.append(i)

print(f'\nsoma: {sum(lista)}')
print(f'media: {sum(lista)/len(lista)}')
print(f'maior: {max(lista)}')
print(f'menor: {min(lista)}')