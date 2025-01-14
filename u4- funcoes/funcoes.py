#Sintaxe básica de uma função:

def saudacao():
    print("Olá, mundo!")

saudacao()

#Definindo uma função com (variáveis declaradas para a função receber valores quando é chamada) e chamando a mesma função passando argumentos.
#Parâmetros podem ter valores padrões caso nenhum argumento for fornecido.
def saudacoes(nome="Visitante"):
    print(f"Olá, {nome}! É um grande prazer conhecê-lo")

saudacoes(input("Olá, eu sou o computador. E você, quem é? "))


#Argumentos posicionais são passados na mesma ordem em que os parâmetros foram definidos na função

def exibir_dados(nome, idade):
    print(f"Nome: {nome}, Idade: {idade}")

exibir_dados("Carlos", 25)

#Argumentos nomeados permite passar os valores diretamente nas variáveis, facilitando a ordem de declaração dos argumentos.

exibir_dados(idade=25, nome="Jubileu")

#Argumentos Arbitrários
#*Args passam um número indefinido de argumentos posicionais, isso é, a função vai aceitar como argumentos quaisquer valores mesmo que não tenham sido definidos previamente como parâmetros.
def somar(*numeros):
    soma = sum(numeros)
    print(f"Soma: {soma}")

somar(1,2,3,4)

#**kwargs funcionam da mesma maneira, mas com argumentos nomeados

def exibir_informacoes (**dados):
    for chave, valor in dados.items():
        print(f"{chave}: {valor}")

exibir_informacoes(nome="Ana", idade=22, cidade="São Paulo")

#Funções podem retornar valores usando a palavra-chave return. Isso permite que o valor deja passado de volta para o código que chamou a função.
def adicao(a,b):
    return a + b
resultado = adicao(5,3)
print(resultado)

#Funções lambda são funções anônimas, definidas em uma linha e usadas para expressões simples.
dobro = lambda x: x *2
print(dobro(10))