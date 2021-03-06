'''Faça um programa em Python contendo subprograma(s), que leia um arquivo texto contendo um ou mais 
números inteiro por linha, mostre seu conteúdo. Substitua todos os números primos do arquivo, 
pelo número zero. Mostre o arquivo após a substituição.

Definição: Um número inteiro é primo se e somente se ele é maior que um e apenas divisível por um e 
por ele mesmo.'''
#Sub Programas
def verificaPrimo(numero):
    if numero<=1:
        return False
    for i in range(2,int(numero**0.5)+1):
        
        if numero%i==0:
            return False
    return True

def lerArquivo(arq):
    dados = open(arq,"r", encoding="utf-8")
    for linha in dados:
        linha = linha.strip("\n")
        print(linha)
    dados.close()
    return None

def verificaArquivo(arq):
    import os
    if os.path.isfile(arq):
        os.remove(arq)
    return open(arq,"a", encoding="utf-8")

def substituiPrimos(arq):
    dados = open(arq, "r", encoding="utf-8")
    arquivo = verificaArquivo("temp")
    for linha in dados:
        lin = linha.strip("/n").split()
        novaLinha=""
        for i in range(len(lin)):
            if verificaPrimo(int(lin[i])):
                lin[i]=0
            novaLinha += f" {lin[i]}"
        arquivo.write(novaLinha[1:]+"\n")
    dados.close()
    arquivo.close()
    dados=arquivo=None
    trocaTemp(arq,"temp")
    return None
def trocaTemp(arq1,arq2):
    dados = open(arq1, "w", encoding="utf-8")
    temp = open(arq2,"r",encoding="utf-8")
    for linha in temp:
        dados.write(linha)
    return None
#Programa Principal
nomeArq = input("Digite o nome do arquivo: ")
#nomeArq = "Q3-arquivo1"
print(20*"-")
print("Arquivo Original:")
lerArquivo(nomeArq)
substituiPrimos(nomeArq)
print(20*"-")
print("Arquivo Substituído:")
lerArquivo(nomeArq)