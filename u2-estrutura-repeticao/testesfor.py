frutas = ["banana", "laranja", "maçã", "melancia", "limão"]

for fruta in frutas:
    print (fruta)


palavra = "Python"

for letra in palavra:
    print(letra)

aluno = {"nome":"Carlos", "idade": "20", "nota":"8"}

for chave, valor in aluno.items():
    print(f"{chave}:{valor}")


for i in range(5):
    for j in range(3):
        print (f"i={i}, j={j}")

matriz = [[1,2,3], [4,5,6], [7,8,9]]

for linha in matriz:
    for elemento in linha:
        print(elemento, end="")
    print()

for i in range(1,10):
    if i == 6:
        break
    print(i)

for i in range (5):
    if i ==2:
        continue
    print(i)

numeros = [1,2,3,4,5,6,7,8,9,10]

for numero in numeros:
    if numero % 2 == 0:
        print (f"{numero} é par")
    else:
        print(f"{numero} é ímpar")