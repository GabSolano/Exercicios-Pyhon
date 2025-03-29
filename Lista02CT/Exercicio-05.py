
dias_uteis = int(input("Digite o total de dias úteis do mês: "))
horas_trabalhadas = int(input("Digite o total de horas trabalhadas no mês: "))
valor_por_hora = float(input("Digite quanto o trabalhador recebe por hora: R$ "))


jornada_mensal = dias_uteis * 8  


if horas_trabalhadas > jornada_mensal:
    horas_extras = horas_trabalhadas - jornada_mensal
    valor_hora_extra = valor_por_hora * 1.5  
    valor_extra = horas_extras * valor_hora_extra
else:
    horas_extras = 0
    valor_extra = 0

salario_normal = jornada_mensal * valor_por_hora
salario_total = salario_normal + valor_extra


print(f"Total de horas extras trabalhadas: {horas_extras} horas")
print(f"Valor da hora extra: R$ {valor_hora_extra:.2f}")
print(f"Salário normal (sem horas extras): R$ {salario_normal:.2f}")
print(f"Salário total com horas extras: R$ {salario_total:.2f}")