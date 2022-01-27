#Exercício Python 25: Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.
#Input do nome
nome = str(input('Digite seu nome completo: ')).strip()

#Output resposta
print('Analizando seu nome...')
print(f'Seu nome possui Silva?\n', 'silva' in nome.lower())
