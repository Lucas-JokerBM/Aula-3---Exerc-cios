## Exercicio 6

# Desenvolva um algoritmo que solicite ao usuário o preço de um produto e um percentual de
# desconto a ser aplicado a ele. Calcule e exiba o valor do desconto e o preço final do produto.   

preco = float(input('Digite o valor do produto: '))
p = int(input('Percentual de desconto (0 - 100%) '))
desconto = preco *(p / 100)
final = preco - desconto


# Forma 1 de concatenação 

print('O preço do produto é %.2fR$. Desconto de %.0f%%.' % (preco, p))
print('Valor calculado de desconto: %.2fR$. Valor final do produto: %.2fR$' % (desconto, final))


# Forma 2 de concatenação 

print('O preço do produto é {}R$. Desconto de {}%.' .format(preco, p))
print('Valor calculado de desconto: {}R$. Valor final do produto: {}R$' .format(desconto, final))

