#Dicionário é uma estrutura de dados que armazena pares de chave:valor, cada chave é única e mapeia diretamente um valor.
#Os dicionários são definidos usando chaves {} e pares de chave:valor são separados por :. Cada par é separado por vírgulas.

aluno = {
    "nome": "Carlos",
    "idade":20,
    "curso":"Engenharia"
}

#mutabilidade, acesso direto, chaves únicas

#acessando de forma simples através da chave associada
print(aluno["nome"])

#acessando através do método get(), configurando uma mensagem de erro caso nenhuma chave seja encontrada.
print(aluno.get("nome", "Nenhum cadastro encontrado"))
print(aluno.get("nota", "Nenhum registro encontrado"))

#alterar o valor de uma chave existente é possível simplesmente atribuindo um novo valor à ela.
print(aluno["curso"])
aluno["curso"] = "Ciência da Computação"
print(aluno["curso"])

#Para adicionar um novo par chave-valor a um dicionário, basta atribuir um valor a uma nova chave.
aluno["nota"] = 9.5
print(aluno)

#Existem dois métodos para remoção de itens:
#pop() remove um item específico com base na chave e retorna o valor removido
aluno.pop("idade")
print(aluno)

#popitem() remove e retorna o último par chave:valor adicionado.
aluno.popitem()
print(aluno)

for valor in aluno.values():
    print(valor)