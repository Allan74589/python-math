#calcular o Mínimo Múltiplo Comum entre dois números (mostrando o passo a passo)
def mmc_com_passos(a, b):
    print("\n📋 Passo a passo (Cálculo do MMC):")
    mdc = 0
    if a == 0 or b == 0:
        return 0
    if a > b:
        maior = a
        menor = b
    else:
        maior = b
        menor = a

    print(f"Calculando MMC de {a} e {b}")
    print(f"Comparando os valores: maior = {maior}, menor = {menor}")

    i = 1
    while True:
        mmc = maior * i
        if mmc % menor == 0:
            print(f"MMC encontrado: {mmc}")
            break
        i += 1

    return mmc

try:
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
except ValueError:
    print("Erro: digite apenas números.")
    exit()

resultado = mmc_com_passos(num1, num2)
print(f"\n✅ O MMC de {num1} e {num2} é: {resultado}")