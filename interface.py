import tkinter as tk
#import navegador
import threading
import subprocess


#instala o pyautogui
subprocess.run(["pip", "install", "pyautogui"], check=True)
#instala selenium
subprocess.run(["pip", "install", "selenium"], check=True)



#função para iniciar o navegador
def abrir_navegador_thread():
    thread = threading.Thread(target=abrir_nav())
    thread.daemon = True
    thread.start()

def abrir_nav():
    try:
        subprocess.run(["python", "navegador.py"], check=True)
    except Exception as e:
        print(f"Erro ao abrir o navegador: {e}") 

def fechar_navegador_thread():
    thread = threading.Thread(target=navegador.fechar_nav)
    thread.daemon = True
    thread.start()


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