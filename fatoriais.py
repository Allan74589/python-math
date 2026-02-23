#calcular os Fatoriais de um número (mostrando o passo a passo)

def calcular_fatorial_com_passos(n):
    print(f"\n📋 Passo a passo (Cálculo do Fatorial de {n}):")
    if n == 0:
        print("Fatorial de 0 é 1.")
        return 1
    fatorial = 1
    for i in range(1, n + 1):
        fatorial *= i
        print(f"Multiplicando por {i}: {fatorial}")
    return fatorial

try:
    num = int(input("Digite um número para calcular o fatorial: "))
except ValueError:
    print("Erro: digite apenas números inteiros.")
    exit()

resultado = calcular_fatorial_com_passos(num)
print(f"\n✅ O fatorial de {num} é: {resultado}")