# 1) Desenvolver um algoritmo que efetue a soma de todos os números ímpares que são múltiplos de
# três e que se encontram no conjunto dos números de 1 até 500.

# for i in range(1,500,1):
#     if i % 3 == 0:
#         print(i)

# 2) Desenvolver um algoritmo que leia a altura de 15 pessoas. Este programa deverá calcular e
# mostrar :
# a. A menor altura do grupo;
# b. A maior altura do grupo;

# alturas = []

# for i in range(5):
#     altura = int(input(f"Digite a altura da {i+1}ª pessoa, em centímetros:"))
#     alturas.append(altura)

# maior_altura = max(alturas)
# menor_altura = min(alturas)

# print(f"A maior altura é de {maior_altura}cm e a menor altura é de {menor_altura}cm")

# 3) Faça uma Tabuada

# numero = int(input("Ensira o numero da Taboada:"))
# print (f"Taboada do {numero}")

# for i in range(1,11):
#     resultado = numero * i
#     print(f"{i} X {numero} = {resultado}")

# 3.5) Fazendo a Tabuada com limite sendo solicitado pro usuário:

# numero = int(input("Digite um número para a tabuada:"))
# limite = int(input("Digite o limite máximo a ser calculado:"))
# contador = 1

# while contador <= limite:
#     resultado = contador * numero
#     print(f"{contador} X {numero} = {resultado}")
#     contador += 1

# 4) Faça uma contagem de 1 até 10 e imprima-os na tela:

# numero = int(input("Digite um número:"))
# contador = 1

# while contador <= numero:
#     print (contador)
#     contador +=1

# 5) Estrutura simples de validação de senha com while:

# senha_correta = '123'
# senha_digitada = ''
# contador = 0

# while senha_digitada != senha_correta:
#     senha_digitada = input("Digite sua senha:")
#     if senha_digitada != senha_correta:
#         contador +=1
#         print(f"Senha incorreta. {contador}ª tentativa de login")
#     if contador >=  3:
#         print ("Bloqueado: excedeu o número de tentativas de login: {contador}")
#         break

# 6) Menu simples com estrutura de repetição

opcao = ''
while opcao != '0':
    print("1 - Nome do Aluno")
    print("2 - Nota do Aluno")
    print("3 - Situação do Aluno")
    print("0 - Sair")
    opcao = input ("Digite uma opção: ")
    if opcao == '1':
        print ("Josué")
        input("digite enter para continuar...")
    elif opcao == '2':
        print("8.5")
        input("digite enter para continuar...")
    elif opcao == '3':
        print("Aprovado!")
        input("digite enter para continuar...")
    elif opcao == '0':
        print("Saindo do Sistema...")
    else:
        print("Opção errada, tente novamente!")