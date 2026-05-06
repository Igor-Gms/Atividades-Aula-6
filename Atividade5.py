def saudacao(horario):
    hora, minuto = horario.split(":")
    hora = int(hora)
    minuto = int (minuto)
    if hora < 0 or hora > 23 or minuto < 0 or minuto > 59:
        return "Horario Invalido"

    if hora >= 5 and hora <= 11:
        return "Bom Dia"
    elif hora >= 12 and hora <= 17:
        return "Boa Tarde"
    else:
        return "Boa Noite"
    
print (saudacao("14:30"))
print (saudacao("20:10"))
print (saudacao("03:40"))
