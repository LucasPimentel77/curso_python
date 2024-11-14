x = float(input('entre com o valor inicial do investimento: '))
ap = float(input('entre com o valor do aporte mensal: '))
taxa = float(input('entre com a taxa de juros de período: '))
T = int(input('entre com o numero de periodos: '))

for i in range(0,T):
    x = (x)*(1+taxa)+ap
print(f'o valor total do investimento nesse periodo é de: {x} reais')