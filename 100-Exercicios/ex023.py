#Exercício Python 23: Faça um programa que leia um número de 0 a 9999
#e mostre na tela cada um dos dígitos separados.

''''#Input de número:
numero = int(input('Informe um número: '))
nu = str(numero)

#monstra as unidades
print(f'A unidade deste número é: {nu [3]}')
#mostra as dezenas
print(f'A dezena deste número é: {nu [2]}')
#mostra as centenas
print(f'A centena deste número é: {nu [1]}')
#mostra os milheres
print(f'O milhar desde número é: {nu [0]}')'''

num = int(input('Digite um número: '))
unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10

print(f'A unidade deste numéro é {unidade}.')
print(f'A dezena deste número é {dezena}.')
print(f'A centena deste número é {centena}.')
print(f'O milhar deste número é {milhar}.')





