num_a = float(input("Digite um numero meu amigo:"))
op = input("Digite um operador (+-*/):")
num_b = int(input("Digite um numero meu amigo:"))



if op == '+':
    resultado = num_a + num_b 
elif op == '-':
    resultado = num_a - num_b
elif op == '*':
   resultado = num_a * num_b
elif op == '/':
    resultado = num_a / num_b
else:
    print("PRESTA ATENCAO NAS OPCOES")    
    resultado = None
    
print(f"Seu resultado é {resultado}")