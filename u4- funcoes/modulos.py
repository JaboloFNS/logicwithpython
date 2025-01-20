#Módulos funcionam como arquivos prontos com blocos de códigos que têm a intenção de serem importados quando necessários para outros arquivos de código.
#É possível renomear o arquivo adicionando a palavra chave "as"
# import funcoes as exemplo

#A função "import" busca o módulo por inteiro, todos os seus blocos de códigos, é possível puxar um bloco específico utilizando "from" antes
from funcoes import somar

print (somar(1,2,3,4))