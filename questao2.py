'''Faça um programa em Python contendo subprograma(s), que leia da entrada padrão o nome de um 
arquivo texto contendo linhas de produtos com no formato:
       código#preço#quantidade#dias restantes de validade. 
(1) Mostre seu conteúdo na saída padrão;
(2) Liste os produtos vencendo em menos de uma semana;
(3) Leia o nome do arquivo de um cliente contendo em cada linha um código de um produto que pretende 
comprar. Liste para cada código o preço e a quantidade disponível. Caso algum código não exista, 
escreva mensagem com o código e a string “indisponível”.   '''
#Sub Programas
def verificaArquivo(arq):
    import os
    if os.path.isfile(arq):
        os.remove(arq)
    return open(arq,"a", encoding="utf-8")
      
def imprimeArquivo(arq):
       dados = open(arq, "r", encoding='utf-8')
       print("Saída do arquivo:")
       for linha in dados:
              for i in linha.strip("\n").split("#"):
                     print(f"{i} ", end="")
              print()
              #print(linha.strip("\n"))
       dados.close()
       return None

def verificaVencido(arq):
       dados = open(arq, "r", encoding="utf-8")
       print("Produtos a vencer:")
       for linha in dados:
              if int(linha.strip("\n").split("#")[3])<7:
                     for i in linha.strip("\n").split("#"):
                         print(f"{i} ", end="")
                     print()
                     #print(linha.strip("\n"))
       dados.close()
       return None
def verificaEstoque(arqEstoque, arqCompra):
       def verificaSaldo(arq, lin):
              estoque = open(arqEstoque, "r", encoding="utf-8")
              for linha in estoque:
                     if lin==linha.strip("\n").split("#")[0]:
                            preco = linha.strip("\n").split("#")[1]
                            saldo = linha.strip("\n").split("#")[2]
                            print(lin,preco,saldo)
                            estoque.close()
                            return None
                     
              print(lin, "indisponível")
              estoque.close()
              return None
       compra = open(arqCompra, "r", encoding="utf-8")
       print("Saldos:")
       for linha in compra:
              verificaSaldo(arqEstoque,linha.strip("\n"))
                    
       
       compra.close()
       return None
#Programa Principal
nomeArq = input("Digite o nome do arquivo: ")
imprimeArquivo(nomeArq)
verificaVencido(nomeArq)
nomeArqCompra = input("Insira o nome do arquivo de compra: ")
verificaEstoque(nomeArq, nomeArqCompra)
