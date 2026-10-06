import socket

HOST = '127.0.0.1'
PORT = 5000

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

servidor.bind((HOST, PORT))
servidor.listen(1)

print("Servidor aguardando conexão...")

conexao, endereco = servidor.accept()

print("Cliente conectado:", endereco)

while True:

    mensagem = conexao.recv(1024).decode()

    if not mensagem:
        break

    print("Cliente:", mensagem)

    if mensagem.lower() == "sair":
        break

    resposta = input("Servidor: ")

    conexao.send(resposta.encode())

    if resposta.lower() == "sair":
        break

conexao.close()
servidor.close()

print("Conexão encerrada.")