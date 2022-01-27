#Exercício Python 29: Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7,00 por cada Km acima do limite.
vel = int(input('Informe a velocidade que passou pela via: '))

if vel > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h')
    print(f'Você deve pagar uma multa de R${(vel - 80)*7:.2f}') #deve ser removido o valor 80, e o que sobrar x7
    print('Dirija com cuidado! Tenha um bom dia.')
print('Dentro da velocidade permitida na via, tenha um bom dia!')