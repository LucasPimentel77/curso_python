inter = int(input('digite o valor inicial do intervalo desejado: '))
final = int(input('digite o valor final do intervalo desejado: '))

for numero in range(inter,final+1):
    print(numero,end='-')
print()

for numero in range(inter,final-1,-1):
    print(numero,end='-')
print()