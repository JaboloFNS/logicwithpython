# senha = input("Digite sua senha: ")
# senhaJoao = "etevaldo123"

# while senha != senhaJoao:
#     print("Senha incorreta, tente novamente.")
#     senha = input("Digite sua senha: ")

# print ("Logado com sucesso!")

# Mesma lógica, mas agora com limitador de quantidade de tentativas antes de bloquear

senha_correta = "454"


for tentativa in range (3):
    senha= input ("Ensira sua senha: ")
    if senha == senha_correta:
        print("Acesso permitido. Bem vindo!")
        break
    else:
        print("Acesso negado")
        if tentativa == 2:
            print("Limite de tentativas atingido, tente novamente mais tarde.")

        


