import tkinter as tk
import threading
import subprocess
from dados import adctxt  # Importando a função adctxt para tratar os dados

# Instala o pyautogui
subprocess.run(["pip", "install", "pyautogui"], check=True)
# Instala selenium
subprocess.run(["pip", "install", "selenium"], check=True)

# Variável global para armazenar o processo do navegador
processo_navegador = None
21/11/2024
# Limpa o arquivo adicionar
with open('txts/adicionar.txt', 'w') as file:
    pass  # Isso vai simplesmente abrir e fechar o arquivo, apagando o conteúdo

# Função para processar os dados antes de abrir o navegador
def processar_dados():
    try:
        print("Iniciando processamento dos dados...")
        adctxt()  # Chama a função para processar a planilha
        print("Processamento de dados concluído com sucesso.")
    except Exception as e:
        print(f"Erro ao processar os dados: {e}")

# Função para iniciar o navegador
def abrir_navegador_thread():
    thread = threading.Thread(target=abrir_nav)
    thread.daemon = True
    thread.start()

def abrir_nav():
    global processo_navegador
    try:
        if processo_navegador is None or processo_navegador.poll() is not None:
            # Processa os dados antes de abrir o navegador
            processar_dados()
            # Inicia o processo do navegador
            processo_navegador = subprocess.Popen(["python", "navegador.py"])
            print("Navegador iniciado.")
        else:
            print("O navegador já está aberto.")
    except Exception as e:
        print(f"Erro ao abrir o navegador: {e}")

def fechar_navegador_thread():
    thread = threading.Thread(target=fechar_nav)
    thread.daemon = True
    thread.start()

def fechar_nav():
    global processo_navegador
    try:
        if processo_navegador and processo_navegador.poll() is None:
            processo_navegador.terminate()  # Encerra o processo do navegador
            processo_navegador.wait()  # Aguarda o encerramento completo
            print("Navegador fechado com sucesso.")
        else:
            print("Nenhum navegador está em execução.")
        processo_navegador = None  # Limpa a referência
    except Exception as e:
        print(f"Erro ao fechar o navegador: {e}")

# Configurando a interface gráfica
janela = tk.Tk()
janela.title("Controle do Navegador")
janela.geometry("300x200")

# Rótulo
label = tk.Label(janela, text="Controle o navegador:")
label.pack(pady=10)

# Botão para abrir o navegador
botao_abrir = tk.Button(janela, text="Abrir Navegador", command=abrir_navegador_thread)
botao_abrir.pack(pady=10)

# Botão para fechar o navegador
botao_fechar = tk.Button(janela, text="Fechar Navegador", command=fechar_navegador_thread)
botao_fechar.pack(pady=10)

# Inicia o loop da interface
janela.mainloop()
