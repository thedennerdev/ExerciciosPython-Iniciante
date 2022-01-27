#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
c = float(input('Quantos °C deseja converter em °F?'))
f = c*9/5+32
print('{}°C equivalem à {:.1f}°F!'.format(c,f))

