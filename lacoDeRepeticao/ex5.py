a = int(input('numero A: '))
b = int(input('numero B: '))

for i in range(1,b+1):
    for j in range(1,a+1):
        if(i==1 or i == b or j ==1 or j ==a):
            print('*',end='')
        else:
            print(' ',end='')
    print()
        