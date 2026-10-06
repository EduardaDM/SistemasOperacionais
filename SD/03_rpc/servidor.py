from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler


class RequestHandler(SimpleXMLRPCRequestHandler):

    rpc_paths = ('/RPC2',)


servidor = SimpleXMLRPCServer(
    ('localhost', 8005),
    requestHandler=RequestHandler
)


def calcular(numero1, numero2):

    resultados = {}

    resultados["soma"] = numero1 + numero2

    resultados["subtracao"] = numero1 - numero2

    resultados["multiplicacao"] = numero1 * numero2

    if numero2 != 0:
        resultados["divisao"] = numero1 / numero2
    else:
        resultados["divisao"] = "Não é possível dividir por zero"

    resultados["potencia"] = numero1 ** numero2

    return resultados


servidor.register_function(calcular, "calcular")

print("Servidor RPC iniciado na porta 8005.")

servidor.serve_forever()