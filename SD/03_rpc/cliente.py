import xmlrpc.client


servidor = xmlrpc.client.ServerProxy(
    'http://localhost:8005'
)

numero1 = float(input("Digite o primeiro número: "))

numero2 = float(input("Digite o segundo número: "))


resultado = servidor.calcular(numero1, numero2)


print()
print("RESULTADOS")
print("----------")

print("Soma:", resultado["soma"])

print("Subtração:", resultado["subtracao"])

print("Multiplicação:", resultado["multiplicacao"])

print("Divisão:", resultado["divisao"])

print("Potência:", resultado["potencia"])