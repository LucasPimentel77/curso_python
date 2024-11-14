n = int(input('digite um numero inteiro e positivo: '))

while n<0:
    n = int(input('digite um numero positivo: '))

for i in range(0,n+1):
    for j in range(0,i+1):
        print(str(j),end='')
    print()
    