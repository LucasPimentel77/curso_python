import random
x = random.randint(0,9)
x2 = random.randint(0,9)
x3 = random.randint(0,9)
x4 = random.randint(0,9)

cont = 0

num1 = float(input('digite um numero que deseja apostar: '))
num2 = float(input('digite outro numero para apostar: '))

if (num1 == x or num1 == x2 or num1 == x3 or num1 == x4):
    cont+=1000
if (num2 == x or num2 == x2 or num2 == x3 or num2 == x4):
    cont+=1000

print(f'\nos numeros sorteados foram {x}, {x2}, {x3}, {x4}')
print(f'voce ganhou {cont} reais')



