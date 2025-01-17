def droparcoluna(dados, coluna):
    dados = dados.drop(labels=str(coluna), axis=1)
    return dados

def separartick(dados, coluna, quant):
    for id in range(quant):

        linha = dados.loc[id, str(coluna)]
        ticker = linha.split()[0]
        dados.loc[id, coluna] = ticker

    return dados


def quantativos():
    with open('txts/adicionar.txt', 'r') as adicionar:
        adicionar = adicionar.readlines()
    quant = len(adicionar)
    print(f"serão adicionados {quant} ativos")
    return quant



