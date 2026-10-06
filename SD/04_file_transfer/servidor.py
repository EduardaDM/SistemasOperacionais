import socket
import os

HOST = '127.0.0.1'
PORT = 6001

ARQUIVO_ENVIO = 'FT_arquivo_recebido.xlsx'
ARQUIVO_RECEBIDO = 'FT_teste.xlsx'


def enviar_arquivo(conn, nome_arquivo):

    tamanho = os.path.getsize(nome_arquivo)

    conn.sendall(tamanho.to_bytes(8, 'big'))

    with open(nome_arquivo, 'rb') as arquivo:

        while True:

            dados = arquivo.read(4096)

            if not dados:
                break

            conn.sendall(dados)


def receber_arquivo(conn, nome_arquivo):

    dados_tamanho = conn.recv(8)

    tamanho = int.from_bytes(dados_tamanho, 'big')

    recebido = 0

    with open(nome_arquivo, 'wb') as arquivo:

        while recebido < tamanho:

            dados = conn.recv(
                min(4096, tamanho - recebido)
            )

            if not dados:
                break

            arquivo.write(dados)

            recebido += len(dados)


servidor = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

servidor.bind((HOST, PORT))

servidor.listen(1)

print("Servidor aguardando conexão...")

conn, endereco = servidor.accept()

print("Cliente conectado:", endereco)


# 1 - Enviar arquivo para o cliente

print("Enviando arquivo...")

enviar_arquivo(conn, ARQUIVO_ENVIO)

print("Arquivo enviado.")


# 2 - Esperar cliente terminar edição

mensagem = conn.recv(1024).decode()

if mensagem == "PRONTO":

    print("Cliente terminou a edição.")

    # 3 - Receber arquivo de volta

    print("Recebendo arquivo...")

    receber_arquivo(
        conn,
        ARQUIVO_RECEBIDO
    )

    print("Arquivo atualizado com sucesso.")

conn.close()

servidor.close()

print("Conexão encerrada.")