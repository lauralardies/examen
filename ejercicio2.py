from random import randint

def encerrada(FILA, COLUMNA):
    if FILA == 0 and tableroajedrez[FILA + 1][COLUMNA] != ' ':
        fallo = True
    elif FILA == 1:
        if tableroajedrez[FILA + 1][COLUMNA] != ' ' and tableroajedrez[FILA - 1][COLUMNA] != ' ':
            fallo = True
        else:
            fallo = False
    elif FILA == 2 and tableroajedrez[FILA - 1][COLUMNA] != ' ':
            fallo = True
    else:
        fallo = False
    return fallo

def printeartablero(tableroajedrez):
    contador_indice = 0
    for tableroajedrez[contador_indice] in tableroajedrez:
        print(tableroajedrez[contador_indice])
        contador_indice += 1
    print("\n")

def movimiento(FILA, COLUMNA):
    if FILA == 0:
            tableroajedrez[FILA+1][COLUMNA] = tableroajedrez[FILA][COLUMNA]
            tableroajedrez[FILA][COLUMNA] = ' '
    elif FILA == 1:
        if tableroajedrez[FILA+1][COLUMNA] != ' ':
            tableroajedrez[FILA-1][COLUMNA] = tableroajedrez[FILA][COLUMNA]
            tableroajedrez[FILA][COLUMNA] = ' '
        else:
            tableroajedrez[FILA+1][COLUMNA] = tableroajedrez[FILA][COLUMNA]
            tableroajedrez[FILA][COLUMNA] = ' '
    elif FILA == 2:
        tableroajedrez[FILA-1][COLUMNA] = tableroajedrez[FILA][COLUMNA]
        tableroajedrez[FILA][COLUMNA] = ' '

def cambio(FILA, COLUMNA):
    if FILA == 0:
        FILA = FILA + 1
    elif FILA == 1:
        if tableroajedrez[FILA+1][COLUMNA] != ' ':
            FILA = FILA - 1
        else:
            FILA = FILA + 1
    elif FILA == 2:
        FILA = FILA - 1
    return FILA

while True:
    tableroajedrez =  [
    [' ', ' ', ' '], 
    [' ', ' ', ' '],
    [' ', ' ', ' '], 
    ]

    x = randint(0,2)
    y = randint(0,2)
    z = randint(0,2)
    a = randint(0,2)
    b = randint(0,2)
    c = randint(0,2)

    while x == a:
        a = randint(0,2)
    while y == b:
        b = randint(0,2)
    while z == c:
        c = randint(0,2)

    #posicionpiezas
    (tableroajedrez[x])[0] = chr(0x2656)
    (tableroajedrez[y])[1] = chr(0x2656)
    (tableroajedrez[z])[2] = chr(0x2656)
    (tableroajedrez[a])[0] = chr(0x265C)
    (tableroajedrez[b])[1] = chr(0x265C)
    (tableroajedrez[c])[2] = chr(0x265C)

    printeartablero(tableroajedrez)

    errorx = encerrada(x, 0)
    errory = encerrada(y, 1)
    errorz = encerrada(z, 2)
    errora = encerrada(a, 0)
    errorb = encerrada(b, 1)
    errorc = encerrada(c, 2)

    if errorx == True and errory == True and errorz == True:
        print("El jugador blanco no se puede mover, volvemos a crear el tablero")
        pass
    elif errora == True and errorb == True and errorc == True:
        print("El jugador negro no se puede mover, volvemos a crear el tablero")
        pass
    else:
        break

turno = randint(0, 1)
while True:
    if turno == 1:
        if errorx == False and errora == False:
            movimiento(x, 0)
            x = cambio(x, 0)
            errora = encerrada(a, 0)
        elif errory == False and errorb == False:
            movimiento(y, 1)
            y = cambio(y, 1)
            errorb = encerrada(b, 1)
        elif errorz == False and errorc == False:
            movimiento(z, 2)
            z = cambio(z, 2)
            errorc = encerrada(c, 2)
        elif errorx == False:
            movimiento(x, 0)
            x = cambio(x, 0)
            errora = encerrada(a, 0)
        elif errory == False:
            movimiento(y, 1)
            y = cambio(y, 1)
            errorb = encerrada(b, 1)
        elif errorz == False:
            movimiento(z, 2)
            z = cambio(z, 2)
            errorc = encerrada(c, 2)
        else:
            break
        turno = 0
    elif turno == 0:
        if errora == False and errorx == False:
            movimiento(a, 0)
            a = cambio(a, 0)
            errorx = encerrada(x, 0)
        elif errorb == False and errory == False:
            movimiento(b, 1)
            b = cambio(b, 1)
            errory = encerrada(y, 1)
        elif errorc == False and errorz == False:
            movimiento(c, 2)
            c = cambio(c, 2)
            errorz = encerrada(z, 2)
        elif errora == False:
            movimiento(a, 0)
            a = cambio(a, 0)
            errorx = encerrada(x, 0)
        elif errorb == False:
            movimiento(b, 1)
            b = cambio(b, 1)
            errory = encerrada(y, 1)
        elif errorc == False:
            movimiento(c, 2)
            c = cambio(c, 2)
            errorc = encerrada(z, 2)
        else:
            break
        turno = 1
    printeartablero(tableroajedrez)
if errorx == True and errory == True and errorz == True:
    print("El jugador blanco no se puede mover, ha ganado el jugador negro")
elif errora == True and errorb == True and errorc == True:
    print("El jugador negro no se puede mover, ha ganado el jugador blanco")