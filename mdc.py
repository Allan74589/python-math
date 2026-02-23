# calcular máximo divisor comum entre dois números (mostrando passos)

def mdc_com_passos(a, b):
    print("\n📋 Passo a passo (Algoritmo de Euclides):")

    while b != 0:
        resto = a % b
        print(f"{a} ÷ {b} → resto {resto}")
        a, b = b, resto

    print("Resto chegou a 0.")
    return a


try:
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
except ValueError:
    print("Erro: digite apenas números.")
    exit()

resultado = mdc_com_passos(abs(num1), abs(num2))

print(f"\n✅ O MDC de {num1} e {num2} é: {resultado}")