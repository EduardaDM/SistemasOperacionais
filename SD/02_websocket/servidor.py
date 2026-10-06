import asyncio
import websockets


async def calcular(websocket):
    print("Cliente conectado.")

    try:
        mensagem = await websocket.recv()

        print("Recebido:", mensagem)

        numeros = mensagem.split(",")

        numero1 = float(numeros[0])
        numero2 = float(numeros[1])

        resultado = numero1 + numero2

        await websocket.send(str(resultado))

        print("Resultado enviado:", resultado)

    except Exception as erro:
        print("Erro:", erro)


async def main():
    servidor = await websockets.serve(
        calcular,
        "localhost",
        8765
    )

    print("Servidor WebSocket iniciado.")
    print("Porta: 8765")

    await servidor.wait_closed()


asyncio.run(main())