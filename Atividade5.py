import time

def saudacao(n):
    if n < 11 and n > 5:
        return "Bom Dia"
    elif n >= 12 and n < 17:
        return "Boa Tarde"
    else:
        return "Boa Noite"
    
print (saudacao(14.30))   
