#Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#– Até 9 anos: MIRIM
#– Até 14 anos: INFANTIL
#– Até 19 anos: JÚNIOR
#– Até 25 anos: SÊNIOR
#– Acima de 25 anos: MASTER

from datetime import datetime
print('~'*28)
print('   DEFININDO SUA CATEGORIA')
print('~'*28)
print('')
current_year = datetime.today().year
ano_nasc = int(input('Informe o ano de seu nascimento: '))
categoria = current_year - ano_nasc

if categoria <= 9:
    print('Categoria: MIRIM')
elif categoria <= 14:
    print('Categoria: INFANTIL')
elif categoria <= 19:
    print('Categoria: JÚNIOR')
elif categoria <= 25: 
    print('Categoria: SÊNIOR')
else:
    print('Categoria: MASTER')