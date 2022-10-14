## Exercício 4

# Desenvolver um algoritmo que solicite ao usuário dois números inteiros. Imprima a soma destes dois numeros.

nota1 = int(input('Qual sua primeira nota? '))
nota2 = int(input('Qual sua segunda nota? '))
print((nota1 + nota2) / 2);

nota1 = int(input('Qual sua primeira nota? '))
nota2 = int(input('Qual sua segunda nota? '))

# Forma 1 de concatenação

res = 'O resultado da soma de %i com %i é %i.' % (nota1, nota2, nota1 + nota2)
print(res)

# Forma 2 de concatenação

res = 'O resultado da soma de {} com {} é {}.' .format(nota1, nota2, nota1 + nota2)
print(res)