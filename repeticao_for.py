numero = int(input("Você deseja gerar a tabuada de qual número?"))

print(f"Tabuada do {numero}")

for i in range(1,11):
    resultado = numero * i
    print (f"{numero} X {i} = {resultado}")

for i in range (1,51):
    if i % 2 != 0:
        print(i)

n1 = int(input("Ensira o 1º número:"))
n2 = int(input("Ensira o 2º número:"))
n3 = int(input("Ensira o 3º número:"))
n4 = int(input("Ensira o 4º número:"))
n5 = int(input("Ensira o 5º número:"))

lista = [n1,n2,n3,n4,n5]

print("O maior número é:", max(lista))
print("O maior número é:", min(lista))