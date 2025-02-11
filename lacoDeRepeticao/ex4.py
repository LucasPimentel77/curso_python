x = int(input('digite um numero: '))

for i in range(1,x+1):
    for j in range(1, 2*x):
        if j == x+1-i:
            for k in range(i):
                print('* ',end='')
            print()
            break
        else:
            print(' ',end='')

