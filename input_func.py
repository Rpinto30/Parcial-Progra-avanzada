def input_number(message): #INGRESAR UN NUMERO Y VERIFICAR QUE SU ENTRADA SEA VALIDA
    while True:
        try:
            value = float(input(message))
            break
        except ValueError: print('-'*50+'\n'+"❌"*5+"   Lo siento valor no valido, intenta nuevamente   "+"❌"*5)

    if value == int(value): return int(value)
    else: return value


def del_tildes(texto):
    reemplazos = (
        ("á", "a"), ("é", "e"), ("í", "i"), ("ó", "o"), ("ú", "u"),)
    for vocal_con_tilde, vocal_sin_tilde in reemplazos: texto = texto.replace(vocal_con_tilde, vocal_sin_tilde)
    return texto

def input_str(message): #INGRESA UN DATO CADENA Y VERIFICA QUE NO ESTÉ VACÍO
    while True:
        try:
            value = del_tildes(input(message).lower().strip())
        except ValueError:print('-' * 50 + '\n' + "❌" * 5 + "   Lo siento valor no valido, intenta nuevamente   " + "❌" * 5)
        else:
            if value.isspace(): print('-' * 50 + '\n' + "❌" * 5 + "   Lo siento valor no valido, la entrada no puede quedar vacia!   " + "❌" * 5)
            else: break

    return value

def clear_screen(): print("\n"*100)
