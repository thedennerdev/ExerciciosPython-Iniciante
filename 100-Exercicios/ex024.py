#Exercício Python 24: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

#Input de uma cidade
cidade = str(input('Digite uma cidade: ')).strip()

#Output se a cidade tem ou não SANTO
print(cidade[:5].lower() == 'santo')

#print(f'A cidade informada -> {cidade} <- não possui SANTO no nome!')
