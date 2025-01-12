#declaração de um conjunto novo
conjunto_exemplo = {1,2,3,4,5}

#adicionando novo elemento ao conjunto
conjunto_exemplo.add(6)
print(conjunto_exemplo)

#dois métodos de remoção de ume elemento no conjunto: remove() retorna erro se o elemento não for encontrado
conjunto_exemplo.remove(5)
conjunto_exemplo.discard(7)
print(conjunto_exemplo)

#exclui todos os elementos do conjunto, deixando-o vazio
conjunto_exemplo.clear()
print(conjunto_exemplo)

#OPERAÇÕES DE CONJUNTOS MATEMÁTICOS
n1 = {1,2,3}
n2 = {3,4,5}

#União - Cria-se um novo conjunto contendo os elementos de ambos os conjuntos raízes(sem repeti-los)
uniao = n1.union(n2)
print(uniao)

#Interseção - Cria-se um novo conjunto contendo os elementos em comum de ambos os conjuntos.
intersecao = n1.intersection(n2)
print(intersecao)

#Diferença - Cria-se um novo conjunto contendos os elementos que pertencem ao conjunto A que não pertencem a B.
diferenca = n1.difference(n2)
print(diferenca)

#Diferença Simétrica - Cria-se um novo conjunto contendo os elementos que pertencem ao conjunto A que não pertencem a B e vice-versa.
diferenca_simetrica = n1.symmetric_difference(n2)
print(diferenca_simetrica)

#SUBCONJUNTO E SUPERCONJUNTOS
#Um conjunto é um subconjunto se todos os seus elementos estão presentes em outro conjunto comparado.
n3 = {1,2}
print(n3.issubset(n1))

#Um conjunto é um superconjunto se possui todos os elementos de outro conjunto
print(n1.issuperset(n3))

#Conjuntos Disjuntos
#Quando um conjunto não possui nenhum elemento de outro eles são disjuntos
n4 = {6,7,8}

print(n1.isdisjoint(n4))

#Com o uso de conjuntos é possível remover valores duplicados de uma lista, convertendo a lista em conjunto.
lista = [1,1,1,2,2,2,3,4,4,5,6,6,]
print(f"Lista com duplicatas: {lista}")
lista_unica = list(set(lista))
print(f"Lista arrumada: {lista_unica}")