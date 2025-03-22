aux = input("Qual valor avista:")
avista = int(aux)

aux = input("Qual valor de cada parcelas:")
parcelas = int(aux)

totalparcelas = parcelas * 10 
desconto = ((totalparcelas - avista) / totalparcelas) * 100

print(f"O desconto é de {desconto * 100}%")