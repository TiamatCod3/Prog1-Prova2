'''Faça um programa em Python contendo subprograma(s), que leia da entrada padrão o nome de um arquivo 
texto em português e escreva qual a palavra contida no arquivo que mais ocorre e quantas vezes ocorreu. 
Caso haja empate no número de vezes das que mais ocorrem, escreva todas que mais ocorrem e quantas vezes 
ocorreram. 
Caso o arquivo esteja vazio escreva a mensagem: “VAZIO – Nenhuma!!!”.'''
#Sub Programas
def criarArquivo(arq):
    dados = open(arq,"r", encoding="utf-8")
    lista = open("lista", "w", encoding="utf-8")
    for linha in dados:
        palavras = linha.strip("\n").split()
        for palavra in palavras:
            lista.write(palavra+"\n")
            
    dados.close()
    lista.close()
    lista = None
    dados = None
    return None
def verificaArquivo(arq):
   def verificaArquivo(arq):
        import os
    if os.path.isfile(arq):
        os.remove(arq)
    return open(arq,"r", encoding="utf-8")
def contarPalavraMaior(arq):
    dados = open(arq, "r", encoding="utf-8")
    palavraContada = verificaArquivo("contagem")
    contador = 0
    for linha in dados:
        palavra = linha.strip("\n")
        




    return None
#Programa Principal
nomeArq = input("Digite o nome do arquivo a ser lido:")
criarArquivo(nomeArq)
contarPalavraMaior("lista")