## Exercicio 5

# Desenvolva um algoritmo que solicite ao usuário uma quantidade de dias, de horas, de minutos
# e de segundos. Calcule o total de segundos resultante e imprima na tela para o usuário.

d = int(input('Quantos dias? '))
h = int(input('Quantas horas? '))
m = int(input('Quantos minutos? '))
s = int(input('Quantos segundos? '))
# 1 d = 24h | h = 60m | m = 60s

total = s + (m * 60) + (h * 60 * 60) + (d * 24 * 60 * 60)


# Forma 1 de concatenação

res = 'O total de segundos calculado é de %i.' % total
print(res)


# Forma 2 de concatenação

res = 'O tolta de segundos calculado é de {}.' .format(total)
print(res)