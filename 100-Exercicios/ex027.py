#Exercício Python 27: Faça um programa que leia o nome completo de uma pessoa,
#mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Digite seu nome completo: ')).strip().split()
print(f'Gostei no nome {nome[0]}!')
#print('Seu primeiro nome é {}'.format(nome.split(['0]))
print(f'Seu primeiro nome é {nome [0]}')
print(f'Seu ultimo nome é {nome[len(nome)-1]}')
