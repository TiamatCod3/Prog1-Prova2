def localiza(x, listaOcs):
    for i in range(len(listaOcs)):
        if x == listaOcs[i][0]:
            return 1
    return -1

def produz(nm):
    listaOcs = []
    dados = open(nm, 'r')
    for linha in dados:
        valor = int(linha)
        onde = localiza(valor, listaOcs)
        if onde == -1:
            listaOcs.append([valor, 1])
        else:
            for i in range(len(listaOcs)):
                if listaOcs[i][0] == valor:
                    listaOcs[i][1] += 1
    dados.close()
    return listaOcs

def mostrar(listaOcs):
    print('Lista de ocorrencias:')
    for valor, vezes in listaOcs:
        print('%5d'%valor, 'ocorre', '%3d'%vezes, 'vez(es)')
    print()
    return None

def qualMaisOcorre(listaOcs):
    if listaOcs == []:
        print('Não existe nehum valor na lista')
    else:
        maisOcorre= listaOcs[0][0]
        vezesMaisOcorre = listaOcs[0][1]
        for valor, vezes in listaOcs:
            if vezes > vezesMaisOcorre:
                maisOcorre = valor
                vezesMaisOcorre = vezes
        print('Mais frequente:', maisOcorre, vezesMaisOcorre, 'vezes')
    return None

nomeArq = input()
listaOcorrencias = produz(nomeArq)
mostrar(listaOcorrencias)
qualMaisOcorre(listaOcorrencias)


