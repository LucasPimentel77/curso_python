def calculaPrimo(num):
    if(num<=1):
        return False
    for i in range(num-1,1,-1):
        if num%i == 0:
            return False
    return True


x = int(input('digite um numero: '))
print(f'numeros primos do intervalo de 0 a {x}')
for i in range(0,x+1):
    if calculaPrimo(i):
        print(f'{i} é primo')