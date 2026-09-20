
cliente_idade = 30              #armazenando a idade e renda do cliente
cliente_renda = 2600

if cliente_idade >= 18 and cliente_renda <= 1600:
    print("Cliente nivel Bronze.")
elif cliente_idade >= 18 and cliente_renda <= 2700:                #faz um funil com a idade e renda do cliente para classificar o mesmo
    print("Cliente nivel Prata.")
elif cliente_idade >= 18 and cliente_renda <= 5999:
    print("Cliente nivel Ouro.")
elif cliente_idade >= 18 and cliente_renda >= 6000:
    print("Cliente nivel Diamante.")
else:
    print("Cliente não qualificado para classificação.")