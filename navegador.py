import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import dados
import tratarplanilha
import pyautogui
import os

# Função para abrir o navegador
def iniciar_navegador():
    servico = Service(ChromeDriverManager().install())
    navegador = webdriver.Chrome(service=servico)
    return navegador

# Função para logar
def fazer_login(navegador, email, senha):
    navegador.get('https://investidor10.com.br/carteiras/lancamentos/995177/')
    navegador.find_element('xpath', '//*[@id="section-1"]/div/div/div[1]/div/div/a[2]').click()
    navegador.find_element('xpath', '//*[@id="modal-sign"]/div/div[1]/form/div[1]/input').send_keys(email)
    navegador.find_element('xpath', '//*[@id="modal-sign"]/div/div[1]/form/div[2]/input').send_keys(senha)
    navegador.find_element('xpath', '//*[@id="modal-sign"]/div/div[1]/form/div[3]/input').click()

# Função para fechar o tutorial (iframe)
def fechar_tutorial(navegador):
    try:
        # Aguarda até o botão de fechar ficar clicável
        WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-sign"]/div/button'))
        ).click()
        print("Tutorial fechado com sucesso!")
        
        # Espera até o iframe desaparecer (caso ainda esteja na página)
        WebDriverWait(navegador, 10).until(
            EC.invisibility_of_element_located((By.XPATH, '//*[@id="wallet-tutorial-video-iframe"]'))
        )
        print("Iframe do tutorial removido!")
    except Exception as e:
        print(f"Erro ao tentar fechar o tutorial: {e}")


# Função para selecionar tipo de ativo
def selecionar_tipo_ativo(navegador, tipo):
    # Abre a aba de tipos
    navegador.find_element('xpath', '//*[@id="add_ticker_entry"]/div/div[1]/div[2]/div[2]/form/div[1]/span/span[1]/span/span[2]').click()
    
    if tipo == 'ACOES':
        navegador.find_element('class name', 'select2-results__option').click()
        time.sleep(1)

    elif tipo == 'FIIS' or tipo == 'ETFS':
        for _ in range(12):
            pyautogui.press('up')
            time.sleep(0.2)
        
        if tipo == 'FIIS':
            pyautogui.press('down')
            pyautogui.press('down')
        elif tipo == 'ETFS':
            for _ in range(7):
                pyautogui.press('down')
                time.sleep(0.2)

        pyautogui.press('enter')
        time.sleep(1)

# Função para preencher os campos de lançamento
def preencher_campo(xpath, valor):
    navegador.find_element('xpath', xpath).click()
    pyautogui.hotkey('Ctrl', 'a')
    pyautogui.press('backspace')
    time.sleep(0.5)
    pyautogui.write(valor)

# Função principal para inclusão de lançamentos
def incluir_lancamento(navegador, id, quantiativo):
    for id in range(quantiativo):
        print(f'será avaliado o ativo numero {id}')
        
        compra = dados.tipomov(id)
        tipo = dados.tipoativo(id)
        nome = dados.nomeativo(id)
        data = dados.datadecompra(id)
        quantidade = dados.quantidade(id)
        valor = dados.valorativo(id)


        fechar_tutorial(navegador)
        # Clica para incluir lançamento
        navegador.find_element('xpath', '//*[@id="my-wallets"]/section[1]/div/div[1]/ul/li[6]/a/span').click()

        try:
            navegador.find_element('xpath', '//*[@id="ticker-entries_wrapper"]/div[1]/div[4]/a').click()
        except:
            navegador.find_element('xpath', '//*[@id="no-entries"]/div/button').click()

        if compra == 'Credito':
            print('é compra')
            navegador.find_element('xpath', '//*[@id="add_ticker_entry"]/div/div[1]/div[2]/div[1]/ul/li[1]').click()
        else:
            print('é venda')
            navegador.find_element('xpath', '//*[@id="add_ticker_entry"]/div/div[1]/div[2]/div[1]/ul/li[2]').click()

        # Seleciona o tipo de ativo (Ações, FIIs, ETFs)
        selecionar_tipo_ativo(navegador, tipo)

        # Preenche o código do ativo
        navegador.find_element('xpath', '//*[@id="ticker_entry"]/div[1]/span/span[1]/span/span[2]/b').click()
        time.sleep(1)
        navegador.find_element('xpath', '/html/body/span/span/span[1]/input').send_keys(nome)
        time.sleep(1)
        pyautogui.press('Enter')
        time.sleep(1)

        # Preenche os campos de data, quantidade e valor
        preencher_campo('//*[@id="ticker_entry"]/div[2]/div[1]/div/input', data)
        preencher_campo('//*[@id="ticker_entry"]/div[2]/div[2]/div/input', quantidade)
        preencher_campo('//*[@id="ticker_entry"]/div[3]/div[1]/div/input', valor)

        # Submete o lançamento
        navegador.find_element('xpath', '//*[@id="submit"]').click()
        time.sleep(4)

        # Fecha a mensagem de sucesso
        navegador.find_element('xpath', '//*[@id="add_ticker_entry_message"]/div/div/div[1]/button').click()
        dados.jaadd(id)

        time.sleep(1)

if __name__ == "__main__":
    # Pega o email e senha
    base_dir = os.path.dirname(__file__)
    email_path = os.path.join(base_dir, 'email-e-senha-invst10', 'email.txt')
    senha_path = os.path.join(base_dir, 'email-e-senha-invst10', 'senha.txt')

    with open(email_path, 'r') as e:
        email = e.read()
    with open(senha_path, 'r') as r:
        senha = r.read()

    # Inicializa o navegador e faz login
    navegador = iniciar_navegador()
    fazer_login(navegador, email, senha)

    # Aguarda um tempo para garantir que a página tenha carregado completamente
    time.sleep(1)

    # Faz a inclusão dos lançamentos
    quantiativo = tratarplanilha.quantativos()
    incluir_lancamento(navegador, 0, quantiativo)
