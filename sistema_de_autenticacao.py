senha_correta = "54321"
tentativas = 0

while tentativas < 3:
    senha = input("Digite sua senha: ")
    tentativas += 1

    if senha == senha_correta:
        print("Acesso permitido!")
        break
    else:
        print("Senha incorreta.")

if tentativas == 3 and senha != senha_correta:
    print("Acesso bloqueado. Você excedeu o número de tentativas.")
