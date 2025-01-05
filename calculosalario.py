horas_trab = float(input("Digite aqui suas horas trabalhadas:"))
valor_hora = float(input("Digite aqui seu salário por hora:"))

if (horas_trab >= 100):
    bonus = 500.00
else:
    bonus = 0

salario = horas_trab * valor_hora + bonus

print (f"Seu salário é {salario}")