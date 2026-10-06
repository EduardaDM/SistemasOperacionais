import socket


HOST = '127.0.0.1'
PORT = 6001

ARQUIVO_RECEBIDO = 'FT_arquivo_recebido.xlsx'


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


def enviar_arquivo(conn, nome_arquivo):

    import os

    tamanho = os.path.getsize(nome_arquivo)

    conn.sendall(
        tamanho.to_bytes(8, 'big')
    )

    with open(nome_arquivo, 'rb') as arquivo:

        while True:

            dados = arquivo.read(4096)

            if not dados:
                break

            conn.sendall(dados)


cliente = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

cliente.connect((HOST, PORT))

print("Conectado ao servidor.")


# 1 - Receber arquivo

print("Recebendo arquivo...")

receber_arquivo(
    cliente,
    ARQUIVO_RECEBIDO
)

print("Arquivo recebido com sucesso.")

print()
print("Abra o arquivo:")
print(ARQUIVO_RECEBIDO)
print()
print("Edite e salve o arquivo.")
print()


input(
    "Quando terminar de editar, pressione ENTER..."
)


# 2 - Avisar servidor

cliente.sendall(
    b"PRONTO"
)


# 3 - Enviar arquivo de volta

print("Enviando arquivo de volta...")

enviar_arquivo(
    cliente,
    ARQUIVO_RECEBIDO
)

print("Arquivo enviado com sucesso.")

cliente.close()

print("Conexão encerrada.")