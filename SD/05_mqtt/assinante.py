import paho.mqtt.client as mqtt
import json


BROKER = "broker.hivemq.com"

PORT = 1883

TOPIC = "/SMART_CP5"


def conectar(client, userdata, flags, rc):

    if rc == 0:

        print("Conectado com sucesso ao broker MQTT!")

        client.subscribe(
            TOPIC,
            qos=2
        )

        print("Inscrito no tópico:", TOPIC)

    else:

        print("Erro na conexão. Código:", rc)


def receber_mensagem(client, userdata, msg):

    try:

        dados = json.loads(
            msg.payload.decode()
        )

        print()
        print("Mensagem recebida:")
        print("-------------------")

        print(
            f"Temperatura: {dados.get('Temp')} °C"
        )

        print(
            f"Umidade: {dados.get('Umid')} %"
        )

        print(
            f"Pressão: {dados.get('Pressao')} hPa"
        )

        print(
            f"RPM: {dados.get('Rpm')}"
        )

        print("-------------------")

    except Exception as erro:

        print(
            "Erro ao processar mensagem:",
            erro
        )


cliente = mqtt.Client()

cliente.on_connect = conectar

cliente.on_message = receber_mensagem


print("Conectando ao broker...")

cliente.connect(
    BROKER,
    PORT,
    60
)


print("Aguardando mensagens...")

cliente.loop_forever()