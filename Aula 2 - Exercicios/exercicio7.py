## Exercicio 7

# Desenvolva um algoritmo que converta uma temperatura em Celsius (C) para Fahrenheit (F). A
# equação de conversão é: 

C = float(input('Digite a temperatura em Celsius: '))
F = (9 * C / 5) + 32


# Forma 1 de concatenação 

print('Celsius: %.1f. Fahrenheit: %.1f' % (C, F))


# Forma 2 de concatenação 

print('Celsius: {}. Fahrenheit: {}' .format(C, F))

