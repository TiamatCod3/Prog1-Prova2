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
    print(contarPalavras)
    print(type(contarPalavras))
    dados.close
    return contarPalavras
def verificaFrequentes(vals):
    frequentes = [0,[]]
    for palavra in vals:
        if vals[palavra]>frequentes[0]:
            frequentes[0]= vals[palavra]
            frequentes[1]=[palavra]
        elif vals[palavra]==frequentes[0]:
            frequentes[1].append(palavra)
    print(frequentes)
    return frequentes
def imprimePalavras(vals):
    texto = "A(s) palavra(s)"
    for palavras in vals[1]:
        texto += f" '{palavras}'"
    texto += f" ocorre(m) {vals[0]} vez(es)"
    print(texto)
    return None
#Programa Principal
import os
nomeArq = input("Digite o nome do arquivo: ")
if os.stat(nomeArq).st_size == 0:
    print("VAZIO – Nenhuma!!!")
else:
    frequenciaPalavras = contarArquivo(nomeArq)
    palavrasFrequentes = verificaFrequentes(frequenciaPalavras)
    palavrasFrequentes[1].sort()
    imprimePalavras(palavrasFrequentes)