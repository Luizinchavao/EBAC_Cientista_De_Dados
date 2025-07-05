programa {
  funcao inicio() {
    inteiro nota, totalnotas = 0
    para (inteiro cont = 1; cont<=5; cont ++ ){
      escreva("Digite a ", cont, " nota ")
      leia(nota)
      totalnotas = totalnotas + nota
    }
    escreva(totalnotas / 5)
    
  }
}
