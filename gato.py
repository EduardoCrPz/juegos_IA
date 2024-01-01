import random
def ubicacionFichas(ubicacion):

    #es como va estar ubicado la posicion para hacer la seleccion
    print(ubicacion[1]+'|',ubicacion[2]+'|',ubicacion[3])
    print('-+-+-')
    print(ubicacion[4]+'|',ubicacion[5]+'|',ubicacion[6])
    print('-+-+-')
    print(ubicacion[7]+'|',ubicacion[8]+'|',ubicacion[9])

def seleccionLetra():   #escoje el jugador con que quiere jugar
    letra=''
    while not (letra == 'X' or letra == 'O'):
        print ('¿Con que quieres jugar X o O?')
        letra = input ().upper()
        
if letra == 'X':
    return ['X','O']
else:
    return ['O','X']

def primerTurno():  #define quien va a tirar primero
    if random.randint(0,1) ==0:
        return 'Computadora'
    else:
        return 'Humano'
def hazMovimiento(ubicacion,letra,moviemiento):
    ubicacion [movimiento] = letra
    
def ganador (tab,let): #las posibles formas de ganar en el tablero

    return((ubi[1]==let and ubi[2]==let and ubi[3]==let) or
            (ubi[4]==let and ubi[5]==let and ubi[6]==let) or
            (ubi[7]==let and ubi[8]==let and ubi[9]==let) or
            (ubi[1]==let and ubi[4]==let and ubi[7]==let) or
            (ubi[2]==let and ubi[5]==let and ubi[8]==let) or
            (ubi[3]==let and ubi[6]==let and ubi[9]==let) or
            (ubi[1]==let and ubi[5]==let and ubi[9]==let) or
            (ubi[3]==let and ubi[5]==let and ubi[7]==let)) 


def muestraGato(ubicacion): 
    vuelveGato = []
    for i in ubicacion:
        vuelveGato.append(i)
    return vuelveGato

def espaciodemovimento(ubicacion, movimiento): #checa si el movimiento pasado estuvo libre 
    return ubicacion[movimiento] == ' '

def movimientosJugador (ubicacion):#movimiento del jugador  
    movimiento =' '
    while movimiento not in '1,2,3,4,5,6,7,8,9'.split() or not espaciodemoviento(ubicacion, int(movimiento)):
        print('¿Que posicion quieres? De las posciones 1-9')
        movimiento= input()
        return int (movimiento)

def movimientoAleatorio (ubicacion,listmov):
    movimientospob=[]
    for i in listmov:
        if espaciomovimiento(ubicacion,i):
            movimientospob.append(i)
            
    if len (movimientospob) !=0:
        return random.choice(movimientospob)
    else:
        return None

def movimientoComputadora(ubicacion,letraMaquina): #aqui la computadora hara el movimiento dependiendo de la dispoivilidad del espacio
    if letraComputadora =='X':
        letraHumano ='O'
    else:
        letraHumano='X'
        
    for i in range(i,10): #este es el agoritmo de la IA 
        vuelveGato = muestraGato(ubicacion)
        if espaciomovimiento(vuelveGato, i):
            hazMovimiento(vuelveGato,letraComputadora,i)
            if gana(vuelveGato,letraComputadora):
                return i

    for i in range(1,10):  #revisa si el humano pude ganar en el siguiente turno para que bloquee la computadora
        vuelveGato= muestraGato(ubicacion)
        if espaciomovimiento(vuelveGato,i):
            hazMovimiento(vuelveGato,letraHumano,i)
            if gana(vuelveGato,letraHumano):
                return i

    movimientoprim = movimientoEnlista (ubicacion,[1,3,7,9]) #buscara ponerse en una esquina
    if movimientoprim != None:
        return movimientoprim
    if espaciomovimiento(ubicacion,5):      #aqui en el centro
        return 5

    return movimientoEnlista(ubicacion,[2,4,6,8])

def ubicacionllena(ubicacion):
    for i in range(1,10):
        if espaciomovimiento(ubicacion,i):
            return False
    return True    

    print('bienvenido al juego del gato ')
    
while True:   # reinia el tablero
    tablero= [' ']*10
    letraHumano,letraComputadora = seleccionLetra()
    turno = primerTurno()
    print(turno+ 'inicia' )
    iniciojuego= True

    while iniciojuego:
        if turno == 'Humano':   #juega Humano
            tableroJuego(tablero)
            movimiento= movimientosJugador(tablero)
            hazMovimiento(tablero,letraHumano,movimiento)

            if gandor(tablero,letraHumano):
                tableroJuego(tablero)
                print('humano gana el juego')
                inicioJuego= False
            else:
                if ubicacionllena(ubicacion):
                    tableroJuego(tablero)
                    print('empate, nadie gano')
                    break
                else:
                    turno = 'Computadora'

        else:  #juega computadora
            movimiento= movimientoComputadora(tablero,letraComputadora)
            hazMovimiento(tablero,letraComputadora,movimiento)

            if ganador(tablero,letraComputadora):
                tableroJuego(tablero)
                print('computadora gana')
                iniciojuego= False
            else:
                if ubicacionllena(tablero):
                    tableroJuego(tablero)
                    print('empate, nadie gano')
                    break
                else:
                    turno = 'Humano'
    print('¿Quieres volver a jugar? (si o no)' )
    if not input().lower().startswitch('si'):
        break
                
                
                
                
                
                
        
    


    
    
            
                
            
            
            
    
        

        


        





    
