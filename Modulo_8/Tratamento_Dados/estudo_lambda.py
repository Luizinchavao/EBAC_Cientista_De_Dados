import pandas as pd

# Função para calcular o cubo de um número
def eleva_cubo(x): # Vai receber o valor de x e elevar ao cubo x**3
    return x ** 3
    
# Expressão de lambda para calcular o cubo de um número 

eleva_cubo_lambda = lambda x: x ** 3 # Essa forma apenas didádita para aprender, porém nao usar assim
# Lambda é a forma de escrever a função em uma linha tbm recebe o valor de x e elevar ao cubo x**3
print(eleva_cubo(2))
print(eleva_cubo_lambda(2))

df = pd.DataFrame({'numeros':[1,2,3,4,5,10]})

df['cubo_funcao'] = df['numeros']. apply(eleva_cubo) # Apply para aplicar uma função um map, um lambda
df['cubo_lambda'] = df['numeros']. apply(lambda x: x ** 3)# Boas Praticas executar o lambda melhor forma
print(df)
 # Utilizar o lambda qdo for operações simples, pequenas operaçãos use o lambda
 # Operações muito complexas utilizar a função pois vai ser mais fácil no futuro as pessoas compreender seu código