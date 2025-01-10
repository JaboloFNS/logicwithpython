tupla_numero = (1,2,3,4,5,6,7,8,9,10)

#Selecionando um intervalo de elementos que serão impressos
print(tupla_numero[0:4])

#Selecionando um elemento através de seu índice
print(tupla_numero[9])

#Verificando se determinado elemento existe na tupla. Retornará um valor em booleano.
print (1 in tupla_numero)

#Concatenando e repetindo tuplas para gerarem novas tuplas maiores
tupla1 = (1,2,3)
tupla2 = (4,5,6)

tupla3 = tupla1 + tupla2
print (tupla1)
print (tupla2)
print (tupla3)

tupla_repetida = tupla1 *4
print(tupla_repetida)

#Desempacotamento de tuplas em diversas variáveis
tupla_pessoa = ("Fabiano", 25, "Desenvolvedor")
nome, idade, profissao = tupla_pessoa
print(nome)
print(idade)
print(profissao)
