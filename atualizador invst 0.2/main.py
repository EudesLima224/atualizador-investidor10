import pyautogui
import dados
from dados import adctxt
import tratarplanilha
import navegador
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service




servico = Service(ChromeDriverManager().install())

nav = webdriver.Chrome(service=servico)
nav.get('https://investidor10.com.br/carteiras/lancamentos/995177/')

navegador.nav_pt1(nav)
adctxt()
navegador.nav_pt2(nav)





