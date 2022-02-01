#Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.

import random
import pyfiglet
from time import sleep

ascii_banner = pyfiglet.figlet_format("JoKemPo")
print(ascii_banner)

itens = ('Pedra', 'Papel', 'Tesoura')

print('''Qual jogada escolhe: 
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')

computador = random.randint(0,2)
jogador = int(input('Qual opção escolhe: '))
print('='*18)

print('JO')
sleep(1)
print('KEM')
sleep(1)
print('PO!!')
sleep(2)

print('='*18)
print(f'O computador jogou {itens[computador]}')
print(f'O jogador jogou {itens[jogador]}')
print('='*18)

if computador == 0: #computador jogou pedra
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('GANHOU')
    elif jogador == 2:
        print('PERDEU')
    else:
        print('Jogada invalida')
elif computador == 1: #computador jogou papel
    if jogador == 1:
        print('EMPATE')
    elif jogador == 0:
        print('PERDEU')
    elif jogador == 2:
        print('GANHOU')
    else:
        print('Jogada invalida')
