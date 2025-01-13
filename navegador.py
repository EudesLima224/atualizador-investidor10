import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import dados
import tratarplanilha
import pyautogui
import subprocess


#instala o pyautogui
subprocess.run(["pip", "install", "pyautogui"], check=True)

#pega o email e senha
with open('C:/Users/Gamer/Documents/MeusProjetos/investidor10/email-e-senha-invst10/email.txt', 'r') as e:
    email = e.read()
with open('C:/Users/Gamer/Documents/MeusProjetos/investidor10/email-e-senha-invst10/senha.txt', 'r') as r:
    senha = r.read()

id = 0

quantiativo = tratarplanilha.quantativos()

#Limpa o arquivo adicionar :)
with open('txts/adicionar.txt', 'w') as tempadd:
    tempadd = ''


servico = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service=servico)
navegador.get('https://investidor10.com.br/carteiras/lancamentos/995177/')

#clica entra
navegador.find_element('xpath', '//*[@id="section-1"]/div/div/div[1]/div/div/a[2]').click()
#senha e mail
navegador.find_element('xpath', '//*[@id="modal-sign"]/div/div[1]/form/div[1]/input').send_keys(email)
navegador.find_element('xpath', '//*[@id="modal-sign"]/div/div[1]/form/div[2]/input').send_keys(senha)
#clica em entrar
navegador.find_element('xpath', '//*[@id="modal-sign"]/div/div[1]/form/div[3]/input').click()


dados.adctxt()
time.sleep(1)

navegador.find_element('xpath', '//*[@id="modal-sign"]/div/button').click()
#escolhe a certeira

time.sleep(4)
navegador.fullscreen_window()
navegador.find_element('xpath', '//*[@id="menu-wallets"]').click()
navegador.fullscreen_window()
navegador.find_element('xpath', '//*[@id="resume"]/div[4]/div/ul/li[3]/a').click()


#incluir lançamento
#navegador.find_element('xpath', '//*[@id="my-wallets"]/section[1]/div/div[1]/ul/li[6]/a/span').click()
#
#try:
#    navegador.find_element('xpath', '//*[@id="fixed-treasury-entries_wrapper"]/div[1]/div[4]/a').click()
#
#except:
#    navegador.find_element('xpath', '//*[@id="ticker-entries_wrapper"]/div[1]/div[4]/a').click()




#escolhe o tipo de acão
for id in range(quantiativo):
    print(f'será avaliado o ativo numero {id}')
    #if dados.jaadc(id) == True:
     #   continue

    compra = dados.tipomov(id)
    
    tipo = dados.tipoativo(id)
    nome = dados.nomeativo(id)
    data = dados.datadecompra(id)
    quantidade = dados.quantidade(id)
    valor = dados.valorativo(id)


    #incluir lancamento
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


    if tipo == 'ACOES':
        #abre abas de tipos
        navegador.find_element('xpath',
                               '//*[@id="add_ticker_entry"]/div/div[1]/div[2]/div[2]/form/div[1]/span/span[1]/span/span[2]').click()

        #seleciona acoes
        navegador.find_element('class name', 'select2-results__option').click()
        time.sleep(1)

    elif tipo == 'FIIS':
        #abre aba de tipos
        navegador.find_element('xpath',
                               '//*[@id="add_ticker_entry"]/div/div[1]/div[2]/div[2]/form/div[1]/span/span[1]/span/span[2]').click()
        #navegador.find_element('css selector', 'Fii').click()
        #seleciona o primeiro item, mas nao clica
        for c in range(12):
            pyautogui.press('up')
            time.sleep(0.2)
        #aperta duas vezes para baixo e clica em FIIs
        pyautogui.press('down')
        time.sleep(0.1)
        pyautogui.press('down')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(1)

    elif tipo == 'ETFS':
        #abre aba de tipos
        navegador.find_element('xpath',
                               '//*[@id="add_ticker_entry"]/div/div[1]/div[2]/div[2]/form/div[1]/span/span[1]/span/span[2]').click()
        #seleciona o primeiro item, mas nao clica
        for c in range(12):
            pyautogui.press('up')
            time.sleep(0.2)
        #aperta o botão de descer 17 vezes para selecionar ETFS
        for c in range(7):
            pyautogui.press('down')
            time.sleep(0.2)
        pyautogui.press('enter')
        time.sleep(1)


    #seleciona codigo
    navegador.find_element('xpath', '//*[@id="ticker_entry"]/div[1]/span/span[1]/span/span[2]/b').click()
    time.sleep(1)


    #escreve o codigo
    navegador.find_element('xpath', '/html/body/span/span/span[1]/input').send_keys(nome)
    time.sleep(1)
    pyautogui.press('Enter')
    time.sleep(1)

    #apaga a data
    #navegador.find_element('xpath', '//*[@id="ticker_entry"]/div[2]/div[1]/div/input').click()
    pyautogui.press('tab')
    pyautogui.hotkey('Ctrl', 'a')
    pyautogui.press('backspace')
    time.sleep(0.5)
    #escreve a data
    pyautogui.write(data)

    #escreve quantidade
    navegador.find_element('xpath', '//*[@id="ticker_entry"]/div[2]/div[2]/div/input').click()
    pyautogui.press('backspace')
    pyautogui.write(quantidade)
    time.sleep(0.5)
    #escreve valor
    navegador.find_element('xpath', '//*[@id="ticker_entry"]/div[3]/div[1]/div/input').click()
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('backspace')
    time.sleep(0.5)
    pyautogui.write(valor)
    navegador.find_element('xpath', '//*[@id="submit"]').click()
    time.sleep(4)
    navegador.find_element('xpath', '//*[@id="add_ticker_entry_message"]/div/div/div[1]/button').click()
    navegador.find_element('xpath', '//*[@id="add_ticker_entry_message"]/div/div/div[1]/button')
    dados.jaadd(id)


    time.sleep(1)







