#Exercício Python 46: Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep
import pyfiglet

for c in range(10, -1, -1):
    print(c)
    sleep(1)
ascii_banner = pyfiglet.figlet_format('FELIZ ANO NOVO!!')
print(ascii_banner)
