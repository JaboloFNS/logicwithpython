# TESTE 1 - OUTPUT NUMÉRICO EM ORDEM CRESCENTE

contador = 1

while contador <=10:
    print (contador)
    contador += 1

print (f"O valor final da variável é: {contador}")

# TESTE 2 - OUTPUT NUMÉRICO EM ORDEM DECRESCENTE

contador_d = 10

while contador_d >= 1:
    print (contador_d)
    contador_d -= 1

print (f"O valor final da variável é: {contador_d}")

# TESTE 3 - DADA A CONDIÇÃO, CONFIRA SE UM NUMERO É PAR OU ÍMPAR

num = 5
while num > 0:
    if num % 2 == 0:
        print (f"{num} é par")
    else:
        print (f"{num} é ímpar")
    num -= 1
print(f"O valor final de num é: {num}")

#TESTE 4 - OUTPUT DE SEQUÊNCIA NUMÉRICA EM LOOPING INFINITO COM UMA CONDICIONAL QUE PARA ESSE LOOPING QUANDO VERIFICADA

num = 1
while num > 0:
    print (num)
    num += 1

    if num == 100:
        break

# TESTE 5 - WHILES ANINHADOS COM OUTPUT NUMÉRICO

i = 1

while i <= 3:
    j = 1
    while j <= 2:
        print(f"i={i}, j={j}")
        j += 1
    i += 1

