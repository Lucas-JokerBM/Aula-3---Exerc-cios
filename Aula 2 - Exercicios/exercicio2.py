## Exercicio 2

# Escreva um programa que pergunte ao usuário a quantidade de km percorridos por um carro alugado pelo usuário, assim como foi alugado. Calcule o preço a pagar, sabendo que o carro custa r$ 60 por dia e 0,15 por kd rodado.

km = int(input('Quantos km foram percorridos? '))
dias = int(input('Quantos dias o veículo foi alugado? '))
preco = 60 * dias + 0.15 * km

print('Km = {}. Dias = {}.' .format(km, dias))
print('Valor a ser pago {}.' .format(preco))