#Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
#– O primeiro valor é maior
#– O segundo valor é maior
#– Não existe valor maior, os dois são iguais

a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))

if a > b:
    print(f'O primeiro valor é maior')
elif b > a:
    print(f'O segundo valor é maior')
else:
    print('Não existe valor maior, os dois são iguais')