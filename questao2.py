'''Faça um programa em Python contendo subprograma(s), que leia da entrada padrão o nome de um 
arquivo texto contendo linhas de produtos com no formato:
       código#preço#quantidade#dias restantes de validade. 
(1) Mostre seu conteúdo na saída padrão;
(2) Liste os produtos vencendo em menos de uma semana;
(3) Leia o nome do arquivo de um cliente contendo em cada linha um código de um produto que pretende 
comprar. Liste para cada código o preço e a quantidade disponível. Caso algum código não exista, 
escreva mensagem com o código e a string “indisponível”.   '''
#Sub Programas
def lerArquivo(arq):
       saldo=[]
       dados = open(arq, "r", encoding='utf-8')
       for linha in dados:
              entrada = linha.strip("\n").split(sep='#')
              saldo.append(entrada)
       dados.close()
       return saldo
def imprimeArquivo(vals):
       print("Codigo - Preço - Quantidade - Dias restantes da validade")
       for linha in vals:
              print(f"{linha[0]:^{6}s} - {linha[1]} - {linha[2]} - {linha[3]}")

       return None
def verificaVencidos(vals):
       print("Itens a vencer:")
       for linha in vals:
              if int(linha[3])<7:
                     print(f"{linha[0]:^{6}s} - {linha[1]} - {linha[2]} - {linha[3]}")
       return None
def verificaEstoque(valsEstoque, arq):
       dados = open(arq, "r", encoding="utf-8")
       for linha in dados:
              codigo = linha.strip("\n")
              encontrado = 0
              for produto in valsEstoque:
                     if codigo == produto[0] and encontrado == 0:
                            print(f"{produto[0]} - {produto[1]} - {produto[2]}")
                            encontrado = 1
                     
              if encontrado == 0:
                     print(f"{codigo} - indisponível")
              

       dados.close()
       return None
#Programa Principal
nomeArq = input("Digite o nome do arquivo: ")
estoque = lerArquivo(nomeArq)
imprimeArquivo(estoque)
verificaVencidos(estoque)
nomeArqCompra = input("Insira o nome do arquivo de compra: ")
#compra = lerArquivo(nomeArqCompra)
#imprimeArquivo(compra)
verificaEstoque(estoque, nomeArqCompra)