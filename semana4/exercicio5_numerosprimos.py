def calculaPrimo(num):
    if(num<0):
        print('numero invalido')
    cont = 0
    for i in range(num,0,-1):
        if num%i == 0:
            cont+=1
    if(cont==2):
        return True
    return False


x = int(input('digite um numero: '))
if calculaPrimo(x):
    print('primo')
else:
    print('nao primo')

