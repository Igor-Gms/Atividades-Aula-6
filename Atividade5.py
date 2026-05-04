import time

def saudacao(n):
    if n > 5 and n < 12:
        return "Bom Dia"
    elif n >= 12 and n < 18:
        return "Boa Tarde"
    else:
        return "Boa Noite"
    
print (saudacao(14.30))   
