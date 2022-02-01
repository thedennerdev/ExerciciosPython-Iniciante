#Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

import datetime
current_year = datetime.datetime.today().year
ano_nasc = int(input('Informe o ano de seu nascimento: '))
idade_alistamento = current_year - ano_nasc

if idade_alistamento < 18:
    print('Ainda não está na hora de se alistar')
    print(f'Sua idade ainda é {idade_alistamento} anos, faltam {18 - idade_alistamento } anos. Aguarde mais um pouco!')
elif idade_alistamento == 18:
    print(f'Sua idade já é {idade_alistamento} anos')
    print('Você está na idade de se alistar. Não perca tempo!')
else:
    print('Você passou do prazo de alistamento.')
    print(f'Sua idade  é {idade_alistamento} anos, já passou {idade_alistamento - 18} anos. Regularize a situação!')