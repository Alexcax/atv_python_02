algoritmo "calculadora"

var
   opcao: inteiro
   numero1, numero2, resultado: real

inicio

   escreval("=== CALCULADORA ===")
   escreval("1 - Soma")
   escreval("2 - Subtracao")
   escreval("3 - Multiplicacao")
   escreval("4 - Divisao")

   escreva("Escolha uma operacao: ")
   leia(opcao)

   escreva("Digite o primeiro numero: ")
   leia(numero1)

   escreva("Digite o segundo numero: ")
   leia(numero2)

   escolha opcao

      caso 1
         resultado <- numero1 + numero2
         escreva("Resultado: ", resultado)

      caso 2
         resultado <- numero1 - numero2
         escreva("Resultado: ", resultado)

      caso 3
         resultado <- numero1 * numero2
         escreva("Resultado: ", resultado)

      caso 4
         se numero1 e numero2 <> 0 entao
            resultado <- numero1 / numero2
            escreva("Resultado: ", resultado)
         senao
            escreva("Nao e possivel dividir por zero.")
         fimse

      outrocaso
         escreva("Opcao invalida.")

   fimescolha

fimalgoritmo