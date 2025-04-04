numA = float(input("Digite o primeiro número: "))
op = input("Digite o operador (+ - * /)")
numB = float(input("Digite o segundo número: "))

if op == '+':
    resultado = numA + numB
elif op == '*':
    resultado = numA + numB
elif op == '-':
    resultado = numA - numB
elif op == '/':
    resultado = numA / numB
elif numB or numA == 0:
    print("NAOOOOOOOOOOOOOOOOOOOO")

print(f"O resuultado da operação {numA} {op} {numB} é igual a: {resultado}")