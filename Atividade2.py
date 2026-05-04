def cont_vogais(n):
    vogais = 0
    for letra in n:
        if letra.lower() in "aeiou":
            vogais += 1
    return(vogais)

print (cont_vogais("programacao"))