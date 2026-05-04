def calculo(numeros):
    soma = sum(numeros)
    media = soma / len(numeros)
    return(soma, media)
    

print(calculo([2, 3, 4, 5]))