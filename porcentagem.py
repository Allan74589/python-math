# calcular a porcentagem de um número em relação a outro (mostrando o passo a passo)

def calcular_porcentagem_com_passos(parte, total):
    print("\n📋 Passo a passo (Cálculo da Porcentagem):")

    if total == 0:
        print("Erro: o total não pode ser zero.")
        return None

    porcentagem = (parte / total) * 100

    print(f"Calculando {parte} como porcentagem de {total}")
    print(f"Divisão: {parte} ÷ {total} = {parte / total}")
    print(f"Multiplicação: {parte / total} × 100 = {porcentagem}%")

    return porcentagem


try:
    parte = float(input("Quanto você tem/obteve? "))
    total = float(input("Qual é o valor total? "))
except ValueError:
    print("Erro: digite apenas números.")
    exit()

resultado = calcular_porcentagem_com_passos(parte, total)

if resultado is not None:
    print(f"\n✅ Resultado final: {resultado:.2f}%")