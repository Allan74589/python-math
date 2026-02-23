# calculando o IMC de uma pessoa (mostrando o passo a passo)

def calcular_imc_com_passos(peso, altura):
    print("\n📋 Passo a passo (Cálculo do IMC):")

    if altura <= 0:
        print("Erro: a altura deve ser maior que zero.")
        return None

    print(f"Fórmula: IMC = peso ÷ (altura²)")
    print(f"Substituindo: IMC = {peso} ÷ ({altura}²)")

    imc = peso / (altura ** 2)

    print(f"Cálculo: {peso} ÷ {altura**2:.4f} = {imc:.2f}")

    return imc


def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    elif imc < 35:
        return "Obesidade grau I"
    elif imc < 40:
        return "Obesidade grau II"
    else:
        return "Obesidade grau III"


# 🔹 entrada segura
try:
    peso = float(input("Digite o peso (kg): "))
    altura = float(input("Digite a altura (m): "))
except ValueError:
    print("Erro: digite apenas números.")
    exit()

resultado = calcular_imc_com_passos(peso, altura)

if resultado is not None:
    classificacao = classificar_imc(resultado)
    print(f"\n✅ Seu IMC é: {resultado:.2f}")
    print(f"📊 Classificação: {classificacao}")
