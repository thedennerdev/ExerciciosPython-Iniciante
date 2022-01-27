#Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km.
#Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45
#parta viagens mais longas.

dist = float(input('Informe a distância em Km de sua viagem: '))

if dist <= 200:
    print(f'O custo da passagem será R${dist * 0.50:.2f}')
else:
    print(f'O custo da passagem será R${dist * 0.45:.2f}')
