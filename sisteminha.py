import os
banco_de_tarefas = []

def limpar_tela():
    os.system ("cls" if os.name == "nt" else "clear")

def mostrar_tarefa():
    contador = 1
    for tarefas in banco_de_tarefas:
        print(f"{contador} - {tarefas}")
        contador += 1

def pausar():
    input("Pressione Enter para continuar...")

def selecionar_menu(opcao):
    if (opcao == '1'):
        tarefa = input("Digite a tarefa nova:")
        banco_de_tarefas.append(tarefa)
    elif (opcao =='2'):
        limpar_tela()
        print ("Listando tarefas...")
        mostrar_tarefa()
        pausar()
    elif (opcao =='3'):
        print ("Editando Tarefas...")
        mostrar_tarefa()
        tarefa_editar = int(input("Qual o número da tarefa que deseja editar? "))
        nova_tarefa = input("Digite a nova tarefa: ")
        banco_de_tarefas[tarefa_editar - 1] = nova_tarefa
    elif (opcao =='4'):
        print ("Excluir Tarefas...")
        mostrar_tarefa()
        tarefa_excluir = int(input("Qual o número da tarefa que deseja excluir? "))
        del banco_de_tarefas[tarefa_excluir-1]
    elif (opcao == '0'):
        print ("Saindo...")
        exit()
    else:
        print("Opção inválida. Tente navegar novamente pelo menu.")
        pausar()


#Exibição do menu e suas opções, além de armazenar a opção selecionada pelo usuário.
def exibir_menu():
    print ("---> Menu <----")
    print ("1 - Adicionar tarefa")
    print ("2 - Listar tarefas")
    print ("3 - Editar tarefas")
    print ("4 - Excluir tarefas")
    print ("0 - Sair")
    opcao = input("Escolha uma Opção: ")
    selecionar_menu(opcao)
    limpar_tela()
    exibir_menu()

exibir_menu()
