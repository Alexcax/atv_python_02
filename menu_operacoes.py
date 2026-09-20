print("=== CALCULADORA ===")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

opcao = int(input("Escolha uma operação: "))

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

match opcao:
    case 1:
        resultado = numero1 + numero2
        print("Resultado:", resultado)

    case 2:
        resultado = numero1 - numero2
        print("Resultado:", resultado)

    case 3:
        resultado = numero1 * numero2
        print("Resultado:", resultado)

    case 4:
        if numero1 and numero2 != 0:
            resultado = numero1 / numero2
            print("Resultado:", resultado)
        else:
            print("Não é possível dividir por zero.")

    case _:
        print("Opção inválida.")