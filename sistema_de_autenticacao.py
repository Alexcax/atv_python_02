senha_correta = "54321"
tentativas = 0

while tentativas < 3:                                # Repete enquanto o usuário tiver menos de 3 tentativas
    senha = input("Digite sua senha: ")
    tentativas += 1                         # Adiciona 1 ao número de tentativas

    if senha == senha_correta:
        print("Acesso permitido!")               # Verifica se a senha digitada é igual à senha correta
        break                   # Encerra o laço caso a senha esteja correta
    else:
        print("Senha incorreta.")           # Caso a senha esteja incorreta

if tentativas == 3 and senha != senha_correta:           # Verifica se as 3 tentativas foram utilizadas e a senha continua incorreta
    print("Acesso bloqueado. Você excedeu o número de tentativas.")
