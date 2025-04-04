'''
11. Escreva um algoritmo que calcule o que deve ser pago por um produto, considerando o preço
normal de etiqueta e a escolha da condição de pagamento. Utilize os códigos da tabela a
seguir para ler qual a condição de pagamento escolhida e efetuar o cálculo adequado.
código condição de pagamento
1 A vista em dinheiro ou cheque, recebe 10% de desconto
2 A vista no cartão de crédito, recebe 5% de desconto
3 Em duas vezes, preço normal de etiqueta sem juros
4 Em quatro vezes, preço normal de etiqueta mais juros de 7%
'''

preco = float(input("Digite o valor do produto: "))
forma_pagamento = int(input("Qual a forma de pagamento: \n 1- Dinheiro ou Cheque \n 2- Cartão de Crédito \n 3- Parcelado em duas vezes \n 4- Parcelado em quatro vezes\n"))

if forma_pagamento == 1:
    preco_final = preco * 0.90  
elif forma_pagamento == 2:
    preco_final = preco * 0.95  
elif forma_pagamento == 3:
    preco_final = preco  
elif forma_pagamento == 4:
    preco_final = preco * 1.07  
else:
    print("Opção de pagamento inválida!")
    preco_final = None

if preco_final is not None:
    print(f"O valor final a ser pago é: R$ {preco_final:.2f}")