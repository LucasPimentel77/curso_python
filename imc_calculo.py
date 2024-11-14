peso = float(input("entre com o seu peso: "))
altura = float(input("entre com a sua altura: "))

imc = peso/altura**2
pIdeal1 = 19*altura**2
pIdeal2 = 25*altura**2

print(f'seu IMC é: {round(imc,2)}, portanto ')

if(imc <= 19):
    print("abaixo do peso")
elif(imc > 19 and imc <= 25):    
    print('peso normal')
elif(imc > 25 and imc <= 30):
    print('acima do peso')
elif(imc > 30 and imc <= 40):
    print('obesidade grau I')
else:
    print('obesidade grau II')

print(f'o seu peso ideal está entre {round(pIdeal1,2)} e {round(pIdeal2,2)}\n')
