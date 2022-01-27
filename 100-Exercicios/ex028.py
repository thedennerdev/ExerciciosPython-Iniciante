#Exercício Python 28: Escreva um programa que faça o computador “pensar”
#em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual
#foi o número escolhido pelo computador. O programa deverá escrever na tela se o
#usuário venceu ou perdeu.
from random import randint
from time import sleep
maquina = randint (0,5)
print('.-' *29)
print('Irei pensar em um numero entre 0 e 5! Adivinhe qual será...')
print('.-' *29)
numero = int(input('Informe um número entre 0 e 5: '))
print('PROCESSANDO...')
sleep(3)
print('')
if maquina == numero:
    print(f'PARABÉS VOCÊ GANHOU!\nPensei no número {maquina} e você escolheu {numero}.')
else:
    print(f'Infelizmente você perdeu!\nPensei no número {maquina} e você escolheu {numero}.')
