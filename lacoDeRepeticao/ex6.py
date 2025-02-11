x = int(input('digite um numero: '))

for i in range(1,x+1):
    for j in range(1,x+1):
        if(i==1 or i == x or j ==1 or j ==x or i==j or i+j==x+1):
            print('*',end='')
        else:
            print(' ',end='')
    print()