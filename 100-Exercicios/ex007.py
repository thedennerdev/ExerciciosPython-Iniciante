#desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média.
n1 = float(input('Inclua a primeira nota do aluno:'))
n2 = float(input('Inclua a segunda nota to aluno:'))
n3 = float(input('Inclua a terceira nota do aluno:'))
n4 = float(input('Inclua a quarta nota do aluno:'))
m = (n1+n2+n3+n4)/4
print('A média final deste aluno é {:.1f}!'.format(m))
