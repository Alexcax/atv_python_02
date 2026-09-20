algoritmo "sistema_autenticacao"

var
   senha, senha_correta: caractere
   tentativas: inteiro

inicio

   senha_correta <- "54321"
   tentativas <- 0

   enquanto tentativas < 3 faca

      escreva("Digite sua senha: ")
      leia(senha)

      tentativas <- tentativas + 1

      se senha = senha_correta entao
         escreval("Acesso permitido!")
         interrompa
      senao
         escreval("Senha incorreta.")
      fimse

   fimenquanto

   se senha <> senha_correta entao
      escreval("Acesso bloqueado. Voce excedeu o numero de tentativas.")
   fimse

fimalgoritmo