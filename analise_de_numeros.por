algoritmo "analise_numeros"

var
   numero, soma, media, maior, menor: real
   i: inteiro

inicio

   soma <- 0

   para i de 1 ate 5 faca

      escreva("Digite o ", i, "º numero: ")
      leia(numero)

      soma <- soma + numero

      se i = 1 entao
         maior <- numero
         menor <- numero
      senao
         se numero > maior entao
            maior <- numero
         fimse

         se numero < menor entao
            menor <- numero
         fimse
      fimse

   fimpara

   media <- soma / 5

   escreval("Soma: ", soma)
   escreval("Media: ", media)
   escreval("Maior valor: ", maior)
   escreval("Menor valor: ", menor)

fimalgoritmo