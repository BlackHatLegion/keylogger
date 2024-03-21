# Keylogger Educacional

Este é um projeto de keylogger educacional desenvolvido para fins de aprendizado e demonstração. Ele captura as teclas pressionadas no teclado e envia os registros para um servidor remoto. Este keylogger foi desenvolvido apenas para fins educacionais e deve ser usado de maneira legal.

## Aviso Legal

O keylogger educacional é fornecido exclusivamente para fins educacionais e de demonstração. Qualquer uso deste software sem o consentimento explícito e legal da parte afetada pode violar as leis de privacidade e segurança cibernética em vigor em sua jurisdição.

O autor deste software não assume qualquer responsabilidade por qualquer uso indevido ou ilegal do mesmo. O usuário é inteiramente responsável por garantir que o uso deste software esteja em conformidade com todas as leis, regulamentos e diretrizes éticas aplicáveis.

Ao utilizar este software, você concorda em empregá-lo estritamente para fins educacionais legítimos e éticos, e isenta o autor de qualquer responsabilidade por quaisquer consequências decorrentes do uso inadequado ou ilegal deste software.

## Funcionalidades

- Captura de teclas pressionadas no teclado.
- Envio dos registros para um servidor remoto.
- Execução em segundo plano sem exibir um console.

## Pré-requisitos (DEV)

- Python 3.x instalado no sistema.
- Bibliotecas Python necessárias listadas no arquivo `requirements.txt`.
- Um servidor remoto para receber os registros do keylogger.

## Como Usar

1. Clone este repositório em sua máquina local:

```bash
git clone https://github.com/seu_usuario/keylogger-educacional.git
```

2. Navegue até o diretório do projeto:

```bash
cd keylogger-educacional
```

- 2.1. Crie uma venv utilizando:
```bash
python -m venv env
```

3. Instale as dependências do Python:

```bash
pip install -r requirements.txt
```
4. inicie o servidor utilizando:
```bash
python keyloggerServer.py
```
5. Modifique o arquivo `keyloggerClient.py` conforme necessário para configurar o URL do servidor remoto.

6. Para testar execute o keylogger usando Python:

```bash
python keyloggerClient.py
```

7. Para criar um executável, use o PyInstaller:

- 7.1 para criar um executavel onde não exibe nenhum console crie um arquivo `keyloggerClient.spec`, exemplo:
```
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(['keyloggerClient.py'],
             pathex=['.env\\Scripts'],
             binaries=[('.env\\Scripts\\pythonw.exe', '.'),],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='keyloggerClient',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False)
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='keyloggerClient')

```

- 7.2 após isso  abra o terminal e digite os seguintes comandos:

```bash
pyinstaller keyloggerClient.spec
```

7. Após a conclusão do processo, você encontrará o executável na pasta `dist` do diretório do projeto.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue para relatar bugs, sugerir novos recursos ou enviar um pull request com melhorias.
