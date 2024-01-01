import random 
import time
import os

#Cruz Perez Eduardo
#De la Cruz Guerra Carlos Ivan
#Quevedo Hernández Alejandro 

#El juego se ejecutara en una pantalla de simbolos del sistema por lo que importamos la funcion os 
#Dividiremos el juego en diferentes pantallas que se iran limpiando con ayuda de cls
#La primer pantalla que se prsentara sera la sig en la cual se dfinira con numeros enteros en un rango indeterminado la cantidad de 
#objetos que van a retirar y con otra entrada de tipo entero la cantidad de objetos maxima que puede retirarse en unrango entre 2 y 10:

def eleccion_cantidades():
        #    while objeto == range(1, 100):
        #        objeto = input("Elige numero de objeto: ")
        #    while retirar == range(1, 5):
        #        retirar = input("Elige cuantos objeto quitar: ")
    print()
    print()
    print()
    print("                       *      *   * * * *   *       *")
    print("                       * *    *      *      * *   * *")
    print("                       *   *  *      *      *   *   *")
    print("                       *    * *      *      *       *")
    print("                       *      *   * * * *   *       *")
    print()
    print()
    objeto = int(input("                          Numero de objetos: ")) #range(5,100) #
    retirar = int(input("           Numero maximo de objetos para retirar entre 2 y 10: "))#range(2,10) 
    return objeto, retirar

#La siguiente pantalla nos muestra los niveles de dificultad que podemos elegir, los cuales estan definidos mas abajo pero que cuentan 
#con una dificultad bastabte reducida y que por un error que no pudimos solucionar usualmente pierde, de igual manera nos da una breve 
#explicacion de como se debe de jugar

def pantalla_Bienvenida():

    print()
    print("              *******************************P01*******************************")
    print()
    print("                                *      *   * * * *   *       *")
    print("                                * *    *      *      * *   * *")
    print("                                *   *  *      *      *   *   *")
    print("                                *    * *      *      *       *")
    print("                                *      *   * * * *   *       *")
    print()
    print()
    print("               Cada jugador debera ir retirando objetos en el rango entr 1 y {}".format(retirar))
    print("                             Pierde quien tiene el ultimo objeto")
    print()
    print()
    print("                                    Niveles de dificultad:")
    print("                                  Facil(1)         Dificil(2) ")
    print()
    print()
    print("              ******************************************************************")
    print()
    nivel = ""
    while nivel != "1" and nivel != "2":
        nivel = input("ELige el nivel de dificultad (1/2): ")
    return nivel 

#La siguiente pantalla nos indica en base a las cantidades que elegimos previamente el numero de objetos que habra en el tablero y la 
#cantidad de estos que podemos retirar en un rango de 1 y la cantidad seleccionada y a partir de una entrada(input) se dara inicio al 
#juego cuando se presione enter 

def pantalla_Inicio(objeto, retirar):

    print()
    print("                             *      *   * * * *   *       *")
    print("                             * *    *      *      * *   * *")
    print("                             *   *  *      *      *   *   *")
    print("                             *    * *      *      *       *")
    print("                             *      *   * * * *   *       *")
    print()
    print()
    print("                                Habra {} objetos en total".format(objeto))
    print()
    print("                          Se pueden quitar entre 1 y {} objeto".format(retirar))
    print()
    print()
    print("                                 Comienzas tu el juego ")
    print()
    print()
#    objeto = input("Seleccione numero de objeto: ")
#    retirar = input("objeto a quitar: ") 
    input ("                             Pulsa enter para empezar ...")
    
#En la siguiente pantalla veremos como se orgaiza un tablero con los objetos definidos por una letra I simulando palillos coo en el juego
#clasico y separando cada monton entre si por 1 espacio, 
#esto en el primer for 
#Por otro lado el segundo for nos indicara cuantos objetos I debe de haber por cada monton tomando en cuenta los que se vallan retirando
#y los que van quedando en el tablero , es decir quitara de froma grafica la cantidad que indique el jugador o la maquina 

def tablero(objeto, retirar):
    
    print()
    print("                             *      *   * * * *   *       *")
    print("                             * *    *      *      * *   * *")
    print("                             *   *  *      *      *   *   *")
    print("                             *    * *      *      *       *")
    print("                             *      *   * * * *   *       *")
    print()
    print()

    for fila in range(1):
        print(end=" ")
        for p in range(1, objeto+1):
            print("I", end="   ")
            if p % retirar == 0:
                print(end=" ")
        print

    print()
    print()
    print()

#Esta parte define la forma de jugar que tendra el humano, indicando la operacion que se debe realizar segun e valor de input(q) que se 
#reciba de igual forma, nos indica los posibles errores ya sea que q sea mayor al numero asignado como maximo y pida algo menor o que
#si recibe una entrada vacia vuelva a solicitar que se ingrese una cantidad, de igual manera si el numero ingresa es mayor a la cantidad 
#de objetos restantes indicara esto y solicitara un numero menor, esta misma parte del codigo nos deculve la variavle objeto_quitar a 
#partir de la entrada que de el jugador 

def movimiento_jugador(objeto, retirar):

    if retirar == 1:
        retirar = ("1")
    elif retirar == 2:
        retirar = ("1","2")
    elif retirar == 3:
        retirar = ("1","2","3")
    elif retirar == 4:
        retirar = ("1","2","3","4")
    elif retirar == 5:
        retirar = ("1","2","3","4","5")
    elif retirar == 6:
        retirar = ("1","2","3","4","5","6")
    elif retirar == 7:
        retirar = ("1","2","3","4","5","6","7")
    elif retirar == 8:
        retirar = ("1","2","3","4","5","6","7","8")
    elif retirar == 9:
        retirar = ("1","2","3","4","5","6","7","8","9")
    elif retirar == 10:
        retirar = ("1","2","3","4","5","6","7","8","9","10")
    
    q = input("         Objetos a retirar:")
    while q not in retirar or int(q) > objeto:
        if q not in retirar:
            q = input(" Elige entre 1 y {}:  ".format(len(retirar)))
        elif int(q) > objeto:
            q = input(" Solo quedan {} objetos:  ".format(objeto))
    else:
        objeto_quitar = int(q)

    return objeto_quitar 

#Aqui se definen las operaciones que realiza cada nivel siendo:
# -  para el nivel facil unicamente numeros aleatorios que se encentran dentro del rango establecido pero que busca ser lo mas grande 
# posible para poder ganarle al usuario en caso de que este calcule erroneamente y quede un numero que sea menor al que se definio como 
# limite maximo, dejando un unico objeto para que el jugadro pierda 
            

def nivel_facil(objeto, retirar):

    if objeto <= retirar:
        objeto_quitar = (objeto-1)
    else:
        objeto_quitar = random.randint(1,retirar)

        while objeto_quitar > objeto:
            objeto_quitar = random.randint(1,retirar)

    return objeto_quitar
#-  y para el nivel dificil buscara calcular la mejor opcion para realozar el retiro de objetos basandose en la cantidad de objetos 
#sobrantes y buscando nuevamente dejar al final un unico objeto para que el jugador pierda

def nivel_dificil(objeto, retirar):

    objeto_quitar = None

    while objeto_quitar is None or objeto_quitar > objeto:
        if objeto <= retirar:
            objeto_quitar = (objeto-1)
        elif objeto % (retirar-1) == 10:
            objeto_quitar = 10
        elif objeto % (retirar-1) == 9:
            objeto_quitar = 9
        elif objeto % (retirar-1) == 8:
            objeto_quitar = 8
        elif objeto % (retirar-1) == 7:
            objeto_quitar = 7
        elif objeto % (retirar-1) == 6:
            objeto_quitar = 6
        elif objeto % (retirar-1) == 5:
            objeto_quitar = 5
        elif objeto % (retirar-1) == 4:
            objeto_quitar = 4
        elif objeto % (retirar-1) == 3:
            objeto_quitar = 3
        elif objeto % (retirar-1) == 2:
            objeto_quitar = 2
        elif objeto % (retirar-1) == 1:
            objeto_quitar = 1
        elif objeto % (retirar-1) == 0:
            objeto_quitar = random.randint(1,retirar)
        #print(objeto_quitar, objeto)

    return objeto_quitar


#Por ultimo aqui definimos quien es el ganador del juego de una manera simple ayudandonos de conocer quien es el jugador en turno que 
#recogio el ultimo objeto t mostrando un mensaje al mismo 

def mostrar_ganador(turno):

    if turno == 2:
        mensaje1 = "                            Tienes el ultimo objeto"
        mensaje2 = "                                  has perdido "
    elif turno == 1:
        mensaje1 = "                          La IA tiene el ultimo objeto "
        mensaje2 = "                                   has ganado"

    print()
    print("                             *      *   * * * *   *       *")
    print("                             * *    *      *      * *   * *")
    print("                             *   *  *      *      *   *   *")
    print("                             *    * *      *      *       *")
    print("                             *      *   * * * *   *       *")
    print()
    print()
    print("    {}".format(mensaje1))
    print()
    print()
    print("    {}".format(mensaje2))
    print()
    print()
    print()


#En esta parte definimos como se realiza el ciclo del juego, los turnos y el elemento que se debe llamar para jugar, la sea el jugador o
#uno de los dos niveles de dificultad disponibles y se definira la accion a realizar en cuanto a cuantos objetos se retiran 

turno = 1

objeto, retirar = eleccion_cantidades()

os.system("cls")
nivel = pantalla_Bienvenida()

os.system("cls")
pantalla_Inicio(objeto, retirar)

jugando = True

while jugando:

    os.system("cls")
    tablero(objeto, retirar)

    if turno == 1:
        jugada = movimiento_jugador(objeto, retirar)
        turno = 2
    elif turno == 2:
        print(" IA en proceso")
        time.sleep(2)
        if nivel == "1":
            jugada = nivel_facil(objeto, retirar)
        elif nivel == "2":
            jugada = nivel_dificil(objeto, retirar)
        turno = 1

    objeto -= jugada
#En esta ultima parte al llegar a 0 los objetos en el tablero nos indica quien fue el ganador y posteriormente se cierra
    if objeto == 0:
        os.system(" ")
        mostrar_ganador(turno)
        time.sleep(20)
        jugando(False)