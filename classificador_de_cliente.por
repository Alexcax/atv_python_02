algoritmo "classificacao_cliente"

var
   cliente_idade: inteiro
   cliente_renda: real

inicio

   cliente_idade <- 30
   cliente_renda <- 2600

   se (cliente_idade >= 18) e (cliente_renda <= 1600) entao
      escreva("Cliente nivel Bronze.")

   senao se (cliente_idade >= 18) e (cliente_renda <= 2700) entao
      escreva("Cliente nivel Prata.")

   senao se (cliente_idade >= 18) e (cliente_renda <= 5999) entao
      escreva("Cliente nivel Ouro.")

   senao se (cliente_idade >= 18) e (cliente_renda >= 6000) entao
      escreva("Cliente nivel Diamante.")

   senao
      escreva("Cliente nao qualificado para classificacao.")

   fimse

fimalgoritmo