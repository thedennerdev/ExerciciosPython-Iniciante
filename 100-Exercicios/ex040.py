#Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#– Média abaixo de 5.0: REPROVADO
#– Média entre 5.0 e 6.9: RECUPERAÇÃO
#– Média 7.0 ou superior: APROVADO

nota_1 = float(input('Informe a primeira nota:' ))
nota_2 = float(input('Informe a segunda nota:' ))
nota_3 = float(input('Informe a terceira nota:' ))
nota_4 = float(input('Informe a quarta nota:' ))
media = (nota_1 + nota_2 + nota_3 + nota_4) / 4
print('')
if media < 5.0: 
    print(f'Sua média final é: {media:.1f}')
    print('Você está REPROVADO!')
elif media > 5.0 and media < 6.9: 
    print(f'Sua média final é: {media:.1f}')
    print('Você está de RECUPERAÇÃO!')
else:
    print(f'Sua média final é: {media:.1f}')
    print('Você está APROVADO! PARABÉNS.')
print('Att, Diretoria.')
