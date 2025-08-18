def input_number(message): #INGRESAR UN NUMERO Y VERIFICAR QUE SU ENTRADA SEA VALIDA
    while True:
        try:
            value = float(input(message))
            break
        except ValueError: print('-'*50+'\n'+"❌"*5+"   Lo siento valor no valido, intenta nuevamente   "+"❌"*5)

    if value == int(value): return int(value)
    else: return value

def input_str(message): #INGRESA UN DATO CADENA Y VERIFICA QUE NO ESTÉ VACÍO
    while True:
        try:
            value = input(message)
        except ValueError:print('-' * 50 + '\n' + "❌" * 5 + "   Lo siento valor no valido, intenta nuevamente   " + "❌" * 5)
        else:
            if value != '': break
            else:print('-' * 50 + '\n' + "❌" * 5 + "   Lo siento valor no valido, la entrada no puede quedar vacia!   " + "❌" * 5)

    return value