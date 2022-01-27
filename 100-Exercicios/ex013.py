#faça um algoritimo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input('Informe seu salário para saber seu reajuste:'))
print('Seu salário após o reajuste de 15% é de R${:.2f}'.format(salario + (salario*15)/100))
