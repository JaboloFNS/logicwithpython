nota1 = float(input("Digite a nota do 1º Bimmestre: "))
nota2 = float(input("Digite a nota do 2º Bimmestre: "))
nota3 = float(input("Digite a nota do 3º Bimmestre: "))
nota4 = float(input("Digite a nota do 4º Bimmestre: "))

soma = (nota1 + nota2 + nota3 + nota4) / 4

if soma >= 7:
    print (f"Notal final: {soma}. Parabéns você foi aprovado!")
elif soma < 7 and soma >= 5:
    print (f"Sua nota foi de: {soma}. O mínimo de aprovação é de 7 pontos, você está habilitado para a recuperação.")
else:
    print(f"Lamentamos, mas você foi reprovado! Dedique-se mais no próximo ano letivo. Nota final: {soma}.")