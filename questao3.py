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

def substituiPrimos(arq):
    dados = open(arq, "r", encoding="utf-8")
    arquivo =[]
    for linha in dados:
        lin = linha.strip("/n").split()
        novaLinha=""
        for i in range(len(lin)):
            if verificaPrimo(int(lin[i])):
                lin[i]=0
            novaLinha += f" {lin[i]}"
        arquivo.append(novaLinha[1:])
    dados.close()
    dados = None
    dados = open(arq, "w", encoding="utf-8")
    for linha in arquivo:
        dados.write(f"{linha}\n")
    dados.close()
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