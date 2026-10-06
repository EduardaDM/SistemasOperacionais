import socket

HOST = '127.0.0.1'
PORT = 5000

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

cliente.connect((HOST, PORT))

print("Conectado ao servidor.")

while True:

    mensagem = input("Cliente: ")

    cliente.send(mensagem.encode())

    if mensagem.lower() == "sair":
        break

    resposta = cliente.recv(1024).decode()

    print("Servidor:", resposta)

    if resposta.lower() == "sair":
        break

cliente.close()

print("Conexão encerrada.")