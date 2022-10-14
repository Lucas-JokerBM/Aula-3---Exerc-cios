## Exercicio 1

# Desenvolva um algoritmo que solicite ao usuário o preço de um produto e um percentual de desconto a ser aplicado a ele.
# Calcule e exiba o valor do desconto e o preço final do produto

preco = float(input('Digite o preço do produto: '))
p = float(input('Digite o percentual de desconto (0 - 100%): '))
desconto = preco * (p / 100)
final = preco - desconto

# Forma 1 de concatenação
print('O preço do produto é %.2f. Desconto de %.0f%%.' % (preco, p))
print('Valor calculado de desconto : %.2f. Valor final do produto: %.2f' % (desconto, final))

# ou

# Forma 2 de concatenação
print('O preço do produto é {}. Desconto de {}%.' .format(preco, p))
print('Valor calculado de desconto: {}. Valor final do produto: {}' .format(desconto, final))
