import pyautogui

import tratarplanilha as tp
import pandas as pd
import math




caminho_arquivo = "C:/Users/Gamer/Documents/MeusProjetos/investidor10/atualizador-investidor10\movimentacoes.xlsx"



def jaadc(id):
    linha_para_verificar = ''

    # Lê todas as linhas do arquivo 'adicionar.txt'
    with open('txts/adicionar.txt', 'r') as f:
        ativos = f.readlines()

    # Verifica se o índice é válido
    if len(ativos) >= id + 1:
        linha_para_verificar = ativos[id].strip()  # Remove quebras de linha e espaços extras
        # Lê o conteúdo de 'adicionados.txt' para verificar se a
        # linha já foi adicionada
        with open('txts/adicionados.txt', 'r') as add_file:
            adicionados = [linha.strip() for linha in add_file.readlines()]

        # Verifica se a linha já está no arquivo
        if linha_para_verificar in adicionados:
            print(f"A linha '{linha_para_verificar}' já está presente em 'adicionados.txt'.")
        else:
            print(f"A linha '{linha_para_verificar}' ainda não está presente. Será adicionada.")
            return False
    else:
        print(f"O arquivo 'adicionar.txt' não contém a linha de índice {id}.")
    return True


def adctxt():
    dados = pd.read_excel(caminho_arquivo)
    quant = int(dados['Data'].count())
    texto = ''

    # excluir colunas inuteis
    dados = tp.droparcoluna(dados, 'Movimentação')
    dados = tp.droparcoluna(dados, 'Instituição')

    # tratar os ticket
    dados = tp.separartick(dados, 'Produto', quant)

    for id in range(quant):
        for titulo in dados:
            # with open('adicionar.txt', 'a') as arquivo:
            # print(dados.loc[id, titulo])
            texto += '|' + str(dados.loc[id, titulo])

        texto += '\n'

        with open('txts/adicionados.txt', 'r') as adicionados:
            adc = adicionados.readlines()

        if str(texto) in adc:
            print("ja foi adicionado", texto)

        else:
            with open('txts/adicionar.txt', 'a') as add:
                print('será adicionado', texto)
                add.write(texto)
        texto = ''
    with open('txts/adicionar.txt', 'r') as adicionar:
        adicionar = adicionar.readlines()
    quant = len(adicionar)
    print('serão adicionados: ', quant, adicionar)
    return


def tipomov(numativo):
    with open('txts/adicionar.txt', 'r') as add:
        add = add.readlines()
        ativo = add[numativo].split('|')
        tipo_de_ativo = ativo[1]
        print(f'tipo: {tipo_de_ativo}')
        return tipo_de_ativo


def nomeativo(ativo):
    with open('txts/adicionar.txt', 'r') as add:
        add = add.readlines()
        ativo = add[ativo].split('|')
        nomeativo = ativo[3]
        return nomeativo


def datadecompra(ativo):
    with open('txts/adicionar.txt', 'r') as add:
        add = add.readlines()
        ativo = add[ativo].split('|')
        data = ativo[2]
        print(f'data de compra: {data}')
        return data


def quantidade(ativo):
    with open('txts/adicionar.txt', 'r') as add:
        add = add.readlines()
        ativo = add[ativo].split('|')
        quant = ativo[4]
        print(f'quantidade: {quant}')
        return quant



def arredondado_para_cima(valor):
    # Multiplica por 100, arredonda para cima e divide por 100
    num = math.ceil(valor * 100) / 100
    # Formata o número para ter duas casas decimais
    return f"{num:.2f}"


def valorativo(ativo):
    with open('txts/adicionar.txt', 'r') as add:
        add = add.readlines()
        ativo = add[ativo].split('|')
        valor = arredondado_para_cima(float(ativo[5]))
        print(f'valor: {valor}')
        return valor


def tipoativo(ativo):
    # Lê o arquivo 'adicionar.txt' e obtém o nome do ativo
    with open('txts/adicionar.txt', 'r') as f:
        nome = nomeativo(ativo)  # Obtém o nome do ativo
        print(f"Nome: {nome}")
    # Verifica se o nome do ativo está presente no arquivo 'tipos.txt' e imprime o tipo
    with open('txts/tipos.txt', 'r') as f:
        encontrado = False
        for linha in f:
            partes = linha.strip().split('|')  # Divide a linha em nome e tipo
            if len(partes) == 2 and partes[0] == nome:  # Verifica se a linha tem o nome e o tipo esperados
                print(f"O ativo {nome} está adicionado como tipo: {partes[1]}")
                encontrado = True
                break

        if not encontrado:
            print("Não encontrei seu ativo no seu banco de dados")
            tipo = input(print('escolha o tipo manualmente:\n'
                  '1 - ACOES\n'
                  '2 - FIIS\n'
                  '3 - ETFS'))

            if tipo == '1':
                pyautogui.click(490, 35)
                txt = (f'{nome}|ACOES\n')
                with open('txts/tipos.txt', 'a') as add:
                    print('será adicionado', txt)
                    add.write(txt)
                return 'ACOES'

            elif tipo == '2':
                pyautogui.click(490, 35)
                txt = (f'{nome}|FIIS\n')
                with open('txts/tipos.txt', 'a') as add:
                    print('será adicionado', txt)
                    add.write(txt)
                return 'FIIS'

            elif tipo == '3':
                pyautogui.click(490, 35)
                txt = (f'{nome}|ETFS\n')
                with open('txts/tipos.txt', 'a') as add:
                    print('será adicionado', txt)
                    add.write(txt)
                return 'ETFS'

    return partes[1]


def finalizar(id):
    achou = False
    while achou == False:
        try:
            imglocal = pyautogui.locateOnScreen('fechar.PNG')
            achou = True
            print('O ativo foi adicionado com sucesso')

        except:
            print('o ativo ainda nn foi adicionado')
            achou = False




def jaadd(id):
    with open('txts/adicionar.txt', 'r') as f:
        linhas = f.readlines()
        ativocompleto = linhas[id]  # Obtém o ativo

    # adiciona no arquivo adicionados.txt
    with open('txts/adicionados.txt', 'a') as add:
        print('será adicionado', ativocompleto)
        add.write(ativocompleto)


