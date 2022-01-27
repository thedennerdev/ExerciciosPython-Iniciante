#Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário
#e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%.
#Para os inferiores ou iguais, o aumento é de 15%.

#pedindo valor de salario.
sal = float(input('Por favor, informe seu salário: '))

if sal > 1250:
    novosal = sal + (sal * 10 / 100) #Calculo de 10%
    print(f'Seu salário foi reajustado para R${novosal:.2f}')
else:
    novosal = sal + (sal * 15 / 100)
    print(f'Seu salário foi reajustado para R${novosal:.2f}')