# exercicio 1 - expressões booleanas

# escrever as expressões booleanas em python:
# a) 2 + 2 < 4
# b) 7 // 3 = 1 + 1
# c) 3² + 4² = 25
# d) 2 + 4 + 6 > 12

# a
# x = 2
# y = 2
# print(x + y < 4)
# false porque x + y não é menor que 4

# b 
# x = 7
# y = 3
# print(x // y == 1 + 1)
# true porque mesmo não dando um resultado exato a divisao de 7/3 é mais proximo de 2 do que 3

# c 
# x = 3**2
# y = 4**2
# print(x + y == 25)
# true pois o resultado de x + y é igual a 25

# d
# x = 2
# y = 4
# z = 6
# print(x + y + z > 12)
# false porque resultado da soma é = a 12 e não > que 12




# exercício 3 - condicional composta

# a) if ano / 4, print: 'pode ser um ano bissexto'
# else: print:'não é um ano bissexto'

# b) if up and down == True, print:'decida-se!',
# else: print: 'voce escolheu um caminho!'

# a
# ano = int(input('Quantos dias tem um ano? '))

# if ano % 2 == 0:
#     print('É um ano bissexto!')
# else:
#     print('Não é um ano bissexto!')

# b
# print('Escolhe um caminho: ')
# print('1 = up')
# print('2 = down')
# lado = int(input('Escolha um lado: '))
# if (lado == True):
#     print('Você escolheu um caminho!')
# else:
#     print('Decida-se!')


# exercício 1

# Faça um algoritmo que receba três valores,
# representando os lados de um triângulo fornecidos pelo usuário. Verifique se os valores formam um
# triângulo e classifique como:
# a) Equilátero (três lados iguais);
# b) Isósceles (dois lados iguais);
# c) Escaleno (três lados diferentes);

# x = int(input('Insira o tamanho do 1º lado do triangulo: '))
# y = int(input('Insira o tamanho do 2º lado do triangulo: '))
# z = int(input('Insira o tamanho do 3º lado do triangulo: '))
# if (x > 0) and (y > 0) and (z > 0):
#   if (x + y > z) and (x + z > y) and (y + z > x):  
#     if (x == y and x == z) or (y == x and y == z) or (z == x and z == y) :
#       print('É um triangulo equilátero.')
#     else: 
#       if (x == y or x == z) or (y == z or y == z) or (z == x or z == y) :
#         print('É um triangulo isóceles.')
#       else: 
#         if (x != y and y != z) or (y != x and y != z) or (z != x and z != y) :
#           print('É um triangulo escaleno.')
#         else:
#           print('Esse foi o resultado!')
#   else:
#     print('Ao menos um dos valores indicados não servem para formar um triangulo.')        
# else: 
#   print('Ao menos um dos valores indicados não serve para formar um triangulo.')


# exercício 2

# escreva um algoritmo que leia 2 valores numéricos e que pergunte ao usuário qual operação ele deseja realizar: adição +, subtração -, multip´licação *, ou divisão /.
# exiba na tela o resultado da operação desejada

# print('Selecione uma das operações desejadas: ')
# print('1 - Adição')
# print('2 - Subtração')
# print('3 - Multiplicação')
# print('4 - Divisão')
# op = input('Qual você deseja? ')
# if op == '1' or op == '2' or op == '3' or op == '4':
#     x = int(input('Digite um valor: '))
#     y = int(input('Digite outro valor: '))

# if (op == '1'):
#   res = x + y
#   print('O resultado da operação foi {}.'.format(res))
#   # ou print('Resultado: {} + {} = {}'.format(x, y, res))
# elif (op == '2'):
#   res = x - y
#   print('O resultado da operação foi {}.'.format(res))
# elif (op == '3'):
#   res = x * y
#   print('O resultado da operação foi {}.'.format(res))
# elif (op == '4'):
#   res = x / y
#   print('O resultado da operação foi {}.'.format(res))   
# else:
#     print('Operação inválida!')
# print('Encerrando o programa...')
      

# exercicio 3

# escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica.
# pergunte a quantidade de kWh consumida e o tipo de instalação: R para residencias, I para industrias e C para comercios

# print('Qual o tipo de instalação no local? ')
# print('R - Residências')
# print('I - Indústrias')
# print('C - Comércios')

# tipo = input('Qual o tipo de instalação? ')
# kwh = float(input('Insira quantos kwh foram gastos: '))

# if (tipo == 'R'):
#     if kwh <= 500:
#         preco = 0.4
#     else:
#         preco = 0.65
# elif (tipo == 'C'):
#     if kwh >= 1000:
#         preco = 0.6
#     else:
#         preco = 0.55
# elif (tipo == 'I'):
#     if kwh <= 5000:
#         preco = 0.55
#     else:
#         preco = 0.60
# else:
#     print('Instalação inválida.')

# print('Total a pagar: {}.'.format(kwh * preco))
