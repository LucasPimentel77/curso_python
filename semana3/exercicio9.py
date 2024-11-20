x = float(input('entre com o valor inicial do investimento: '))
ap = float(input('entre com o valor do aporte mensal: '))
taxa = float(input('entre com a taxa de juros de período: '))
T = int(input('entre com o numero de periodos: '))

init = x

for i in range(0,T):
    x = (x)*(1+taxa)+ap

print(f'\no valor total do investimento nesse periodo é de: {x} reais')
print(f'total aportado: {ap*T} reais')
print(f'o ganho em juros foi de: {x-init-ap*T} reais')