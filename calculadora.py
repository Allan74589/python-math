try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
except ValueError:
    print("Erro: digite apenas números.")
    exit()

operacao = input("Digite a operação desejada: ")

resultado = None

match operacao:
    case "+":
        resultado = num1 + num2
    case "-":
        resultado = num1 - num2
    case "*":
        resultado = num1 * num2
    case "/":
        if num2 != 0:
            resultado = num1 / num2
        else:
            print("Erro: Divisão por zero não é permitido.")
    case _:
        print("Operação inválida.")

if resultado is not None:
    print(f"O resultado da operação {operacao} é: {resultado}")