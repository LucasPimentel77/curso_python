a = float(input('entre com o A: '))
b = float(input('entre com o B: '))
c = float(input('entre com o C: '))

delta = b**2-4*a*c

if delta < 0:
    print('nenhuma rais real')
if delta > 0:
    print('duas raízes reais')
if delta == 0:
    print('apenas uma raíz real')   