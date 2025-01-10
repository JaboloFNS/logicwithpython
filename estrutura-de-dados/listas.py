# Linha 3 -> Definida uma lista de 4 elementos. Linha 5 -> inprimindo o elemento de índice 3 na lista. Linhas 6 e 7-> imprimindo cada um dos elementos da lista.

frutas = ["maçã","banana","laranja","uva"]

print(f"Esse é o elemento de índice 3: {frutas[3]}")
for fruta in frutas:
    print(fruta)

#Modificando um elemento da lista e imprimindo os elementos atuais
frutas[2] = "morango"
print(f"Modificando um elemento da lista por outro e imprimindo a lista atualizada:{frutas}")

#---------------------------------------------------------------------------------------------------------
#Adicionando novos itens na lista: 
#append adiciona um novo elemento no final da lista.
frutas.append("kiwi")
print(f"Lista após a inserção de mais um elemento com .append: {frutas}")

#insert (indice, "elemento") insere um novo elemento na lista na posição do índice declarado
frutas.insert(2,"melancia")
print(f"Lista após a inserção de mais um elemento com insert, declarando o índice: {frutas}")

#-----------------------------------------------------------------------------------------------------------
#Removendo novos itens na lista:
#A função remove("valordoelemento") deleta o índice primeiro elemento que corresponde com o valor declarado
frutas.remove("melancia")
print(f"Lista após a exclusão do elemento declarado na função remove(): {frutas}")

#A função pop() deleta e retorna o último elemento da lista ou o elemento correspondente ao índice declarado
fruta_removida = frutas.pop(2)
print(f"A fruta removida com o função pop foi: {fruta_removida}")

print(frutas)

#Utilizando a estrutura de repetição if, conseguimos conferir se determinado elemento está registrado na lista.
nomes = ["Luana", "Cleide", "Jakeline", "Fabiano"]

nome_consultado = input("Nome a ser consultado: ")
if nome_consultado in nomes:
    print ("Nome consta em nosso banco de dados")
else:
    print ("Nome não cadastrado")    

#Utilizando estruturas de repetição, conseguimos solicitar inserções na lista até que se complete uma condição

cidades = []

for i in range(3):
    cidade = str(input("Ensira uma cidade:"))
    cidades.append(cidade)
print (cidades)


paises = []
resp = str("s")
while resp == "s":
    pais = str(input("Ensira países:"))
    paises.append(pais)
    resp = str(input("Deseja continuar a operação? [s/n]"))

print(paises)
    