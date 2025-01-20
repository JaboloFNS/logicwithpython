# 1) Faça um algoritmo que leia os valores A, B, C e imprima na tela se a soma de A + B é menor que C.

# A = int(input("Ensira o primeiro valor:"))
# B = int(input("Ensira o segundo valor:"))
# C = int(input("Ensira o terceiro valor:"))
# soma_ab = A+B

# if soma_ab < C:
#     print(f"A soma de {A} + {B} é igual a {soma_ab}, que é menor que {C}")
# else:
#     print(f"A soma de {A} + {B} é igual a {soma_ab}, que é maior que {C}")

# ----------------------------------------------------------------------------------------------------------

# 2) Faça um algoritmo que leia o nome, o sexo e o estado civil de uma pessoa. Caso sexo seja “F” e estado civil seja “CASADA”, 
# solicitar o tempo de casada (anos).

# nome = str(input("Ensira seu nome: "))
# sexo = str(input("Ensira 'F' para o sexo feminino e 'M' para sexo masculino: "))
# estado_civil = int(input("Estado Civil, ensira '1' para Casado, '2' para Solteiro ou '3' para União Estável: "))

# if sexo == "F" and estado_civil == 1:
#     tempo_casado = int(input("Ensira o tempo de casado em anos completos: "))
#     print (f"Caramba! {tempo_casado} anos de casado, parabéns. ")

# ----------------------------------------------------------------------------------------------------------

# # 3) Faça um algoritmo para receber um número qualquer e informar na tela se é par ou ímpar. 

# n = int(input("Ensira um número: "))

# if n % 2 == 0:
#     print (f"O número {n} é par!")
# else:
#     print (f"O número {n} é ímpar!")

# ----------------------------------------------------------------------------------------------------------

# 4) Faça um algoritmo que leia dois valores inteiros A e B se os valores forem iguais deverá se
# somar os dois, caso contrário multiplique A por B. Ao final de qualquer um dos cálculos deve-se
# atribuir o resultado para uma variável C e mostrar seu conteúdo na tela. 

# print ("Bem vindo a calculadora maluca. Números iguais serão somados, números diferentes serão multiplicados")
# a = int(input("Ensira o primeiro número: "))
# b = int(input("Ensira o segundo número: "))

# if a == b:
#     c = a+b
#     print(f"A operação será uma soma com resultado igual a: {c}")
# else:
#     c = a*b
#     print (f"A operação será uma multiplicação com resultado igual a: {c}")

# print ("Obrigado por usar a calculadora maluca.")

# ----------------------------------------------------------------------------------------------------------

# 5) Encontrar o dobro de um número caso ele seja positivo e o seu triplo caso seja negativo,
# imprimindo o resultado.

# n = int(input("Ensira o número: "))

# if n > 0:
#     dobro = n * 2
#     print (f"O dobro de {n} é igual a {dobro}")
# else:
#     triplo = n * 3
#     print (f"O triplo de {n} é igual a {triplo}")

# 6)Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um algoritmo que
# calcule seu peso ideal, utilizando as seguintes fórmulas:
# ● para homens: (72.7 * h) - 58;
# ● para mulheres: (62.1 * h) - 44.7. 

# nome = str(input("Ensira seu nome: "))
# sexo = int (input("Ensira '1' para o sexo Masculino e '2' para o sexo Feminino: "))
# altura = float(input("Ensira sua altura em metros. Exemplo: 1.76 m: "))

# if sexo == 1:
#     alt_man = (72.7 * altura) - 58
#     print (f"{nome}, seu peso ideal é {alt_man}")
# else:
#     alt_woman = (62.1 * altura) - 44.7
#     print (f"{nome}, seu peso ideal é {alt_woman}")

#7) Um vendedor recebe uma comissão por suas vendas. Dependedo do valor da venda, a comissão varia.
# - 5% para vendas até R$ 1000,00
# - 7,5% para vendas entre 1000,01 e 5000,00
# - 10% para vendas entre 5.000,01 e 10000,00
# Escreva um programa em Python que calcule a comissão do vendedor,
# dado o valor da venda e o nome do vendedor.

nome_vendedor = str(input("Olá, vendedor! Para começar, ensira seu nome: "))
valor_venda = float(input(f"{nome_vendedor}, ensira o valor de sua última venda para calcularmos sua comissão: R$ "))


if valor_venda <= 1000.00:
    comissao = valor_venda * 0.05
    print(f"Sua comissão é de {comissao}")
elif valor_venda <= 5000.00:
    comissao = valor_venda * 0.075
    print(f"Sua comissão é de {comissao}")
elif valor_venda <= 10000.00:
    comissao = valor_venda * 0.1
    print(f"Sua comissão é de {comissao}")
else:
    comissao = valor_venda * 0.15
    print(f"Sua comissão é de {comissao}")

