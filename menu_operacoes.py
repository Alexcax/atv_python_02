print("=== CALCULADORA ===")
print("1 - Soma")    
print("2 - Subtração")                       # Exibe as operações disponíveis
print("3 - Multiplicação")
print("4 - Divisão")

opcao = int(input("Escolha uma operação: "))                  # Solicita ao usuário que escolha uma das operações

numero1 = float(input("Digite o primeiro número: "))          # Solicita os dois números que serão utilizados no cálculo
numero2 = float(input("Digite o segundo número: "))

match opcao:                                    # Verifica qual operação foi escolhida pelo usuário, e realiza a operação dessa opção
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
        if numero2 != 0:                     # Verifica se é possível realizar a divisão por zero
            resultado = numero1 / numero2
            print("Resultado:", resultado)
        else:
            print("Não é possível dividir por zero.")

    case _:                                              # Executado caso o usuário escolha uma opção que não existe
        print("Opção inválida.")
