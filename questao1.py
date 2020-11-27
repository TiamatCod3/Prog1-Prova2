'''Faça um programa em Python contendo subprograma(s), que leia da entrada padrão o nome de um arquivo 
texto em português e escreva qual a palavra contida no arquivo que mais ocorre e quantas vezes ocorreu. 
Caso haja empate no número de vezes das que mais ocorrem, escreva todas que mais ocorrem e quantas vezes 
ocorreram. 
Caso o arquivo esteja vazio escreva a mensagem: “VAZIO – Nenhuma!!!”.'''
def contarArquivo(arq):
    contarPalavras = {}
    dados = open(arq, "r", encoding='utf-8')
    for linha in dados:
        palavras = linha.strip("\n").split()
        for palavra in palavras:
            if palavra in contarPalavras:
                contarPalavras[palavra] += 1
            else:
                contarPalavras[palavra] = 1
    
    dados.close
    dados = None
    dados = open(arq+"contado","w", encoding="utf-8")
    for item in contarPalavras:
        dados.write(f"{item} {contarPalavras[item]}\n")
        
    dados.close()
    dados= None
    return None
def verificaFrequentes(arq):
    dados = open(arq, "r", encoding="utf-8")
    frequentes = [0,[]]
    for linha in dados:
        palavra = linha.strip("\n").split()[0]
        contagem = int(linha.strip("\n").split()[1])
        if contagem>frequentes[0]:
            frequentes[0]= contagem
            frequentes[1]= [palavra]
        elif contagem==frequentes[0]:
            frequentes[1].append(palavra)
    
    dados.close()
    dados = None
    dados = open(arq, "w", encoding="utf-8")
    dados.write(str(frequentes[0])+"\n")
    for palavra in frequentes[1]:
        dados.write(palavra+"\n")
    dados.close()
    return None

def imprimeFrequentes(arq):
    dados = open(arq, "r", encoding="utf-8")
    casos = int(dados.readline().strip("\n"))
    texto = "A(s) palavra(s)"
    for linha in dados:
        linha = linha.strip("\n")
        texto += f" '{linha}'"
        
    texto += f" aparece(m) {casos} vez(es)"
    
    print(texto)
    return None

#Programa Principal
import os
nomeArq = input("Digite o nome do arquivo: ")
if os.stat(nomeArq).st_size == 0:
    print("VAZIO – Nenhuma!!!")
else:
    contarArquivo(nomeArq)
    verificaFrequentes(nomeArq+"contado")
    imprimeFrequentes(nomeArq+"contado")
  
    #palavrasFrequentes = verificaFrequentes(frequenciaPalavras)
    #palavrasFrequentes[1].sort()
    #imprimePalavras(palavrasFrequentes)

