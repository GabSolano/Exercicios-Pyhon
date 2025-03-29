salario = float(input("Digite o salário do funcionário: R$ "))


if salario <= 1693.72:
    aliquota = 0.08  
    desconto = salario * aliquota
elif salario <= 2822.90:
    aliquota = 0.09  
    desconto = salario * aliquota
elif salario <= 5645.80:
    aliquota = 0.11 
    desconto = salario * aliquota
else:
    aliquota = 0.11  
    desconto = 5645.80 * aliquota


print("O percentual de desconto aplicado é:", aliquota * 100, "%")
print("O valor do desconto é: R$", desconto)