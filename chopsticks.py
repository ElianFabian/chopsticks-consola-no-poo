import random as r
import colorama
from colorama import Fore, Style
colorama.init()

# Jerarquía de condiciones: (boceto incompleto):

    # LÓGICA
    # evita atacar si te perjudica
    # evita que se pueda repartir teniendo un 0 y un 1 en cada mano
    # si se puede matar, se matará, excepto si te perjudica
    # evita que si alguien ya ha repartido, la otra no pueda repartir si se vuelve al estado anterior
    # evita que si al matar una mano, la otra te mate, entonces no puedas matar (teniendo una de tus manos a 0) (en proceso)
 
    # SUMA2
    # evita que se pueda atacar con una mano con 0
    # evita que se pueda sumar a una mano con 0
    # ataca para matar si se puede
 
    # REPARTIR2
    # condición para que si una mano es 0, entonces no pueda repartir
    # reparte sólo si no perjudica
    # evita atacar si te perjudica
    # si las manos son diferente de 0, repartirán
         # evita que un jugador se suicide
    # evita que si en una mano tienes 1 y en otra 0, pases a la otra 1
    # evita que al repartir te puedan matar una mano
 
    # REPARTIR
    # si una mano tiene 0, no podrá pasar todo a la otra mano, sólo una parte
    # evita que puedas pasar una cantidad que haría que en la otra mano llegue a n o más
    # reparte una cantidad que no te perjudique siempre que se pueda
    # cuando en una mano hay 1 y con la otra pasas una cantidad que hace que te quedes igual que antes y te puedan matar entonces se cambia al valor de k

# jugador 1 (manos)
a1, a2 = 1, 1
# jugador 2 (manos)
b1, b2 = 1, 1

# jugador (1 o 2)
j = int()
# número máximo en cada mano
n = 5
# cuenta el número de veces que se ha usado repartir
cont1 = 0
# indica la accion que se ha hecho
accion = str()


# Argumentos:
# a, b: mano cualquiera del jugador principal y del secundario, respectivamente
# n1, n2: manos del jugador principal; c1, c2: manos del jugador secundario
# cont1,accion: es necesario que sea un argumento para poder modificarlo dentro de las funciones

# acciones
def sumar(a, b): # suma el número del jugador que ataca al jugador atacado
    return a + b

def sumar2(n1, n2, c1, c2, accion): # se encarga de toda la lógica suma
    accion = 'ataca'
    e = r.randint(0, 3)

    # evita que se pueda atacar con una mano con 0
    if (n1 == 0 and n2 != 0):
        e = r.choice([2, 3])
    elif (n1 != 0 and n2 == 0):
        e = r.choice([0, 1])
    # evita que se pueda sumar a una mano con 0
    if (c1 == 0 and n1 != 0):
        e = 1
    elif (c1 == 0 and n2 != 0):
        e = 3
    elif (c2 == 0 and n1 != 0):
        e = 0
    elif (c2 == 0 and n2 != 0):
        e = 2
    # ataca para matar si se puede
    if (n1 + c1 >= n):
        e = 0
    elif (n1 + c2 >= n):
        e = 1
    elif (n2 + c1 >= n):
        e = 2
    elif (n2 + c2 >= n):
        e = 3

    # ataca con la mano y a la mano que no te perjudique
    if ((2*n1 + c1 >= n or n1 + c1 + n2 >= n) and c1 != 0 and c2 != 0): #P1M1 a P2M1 y luego P2M1 a P1M1
        e = 1
    elif ((2*n1 + c2 >= n or n1 + c2 + n2 >= n) and c1 != 0 and c2 != 0): #P1M1 a P2M2 y luego P2M2 a P1M1
        e = 0
    elif ((2*n2 + c1 >= n or n2 + c1 + n1 >= n) and c1 != 0 and c2 != 0): #P1M2 a P2M1 y luego P2M1 a P1M2
        e = 3
    elif ((2*n2 + c2 >= n or n2 + c2 + n1 >= n) and c1 != 0 and c2 != 0): #P1M2 a P2M2 y luego P2M2 a P1M2
        e = 2
    # elif (n1 + c1 + n2 >= n): #P1M1 a P2M1 y luego P2M1 a P1M2
    #     e =
    # elif (n1 + c2 + n2 >= n): #P1M1 a P2M2 y luego P2M2 a P1M2
    #     e =
    # aquí es donde se hacen las sumas de los ataques
    if (e == 0):
        c1 = sumar(n1, c1)
        ma = 'M1'
        mb = 'M1'
    elif (e == 1):
        c2 = sumar(n1, c2)
        ma = 'M1'
        mb = 'M2'
    elif (e == 2):
        c1 = sumar(n2, c1)
        ma = 'M2'
        mb = 'M1'
    elif (e == 3):
        c2 = sumar(n2, c2)
        ma = 'M2'
        mb = 'M2'
    # cuando una mano llega a n o más se pone a 0
    if (c1 >= n):
        c1 = 0
    elif (c2 >= n):
        c2 = 0
    return c1, c2, ma, mb, accion

def repartir(n1, n2, c1, c2): # reparte de los número de una mano a otra
    cont = 0 # cuenta las veces que se ha tratado de buscar un valor para k que no perjudique al repartir
    k = r.randint(1, n1) #cantidad que se reparte

    # si una mano tiene 0 sólo una parte, no todo
    if (n2 == 0 and k == n1 and n1 > 1):
        k = r.randint(1, k-1)

    # evita que puedas pasar una cantidad que haría que en la otra mano llegue a n o más
    if (k == n1 and k + n2 >= n and n1 > 1):
        k = r.randint(1, k-1)

    # reparte una cantidad que no te perjudique siempre que se pueda
    while ((n2 + k + c1 >= n or n2 + k + c2 >= n) and n1 > 1):
        k = r.randint(1, n1-1)
        cont += 1
        # cuando en una mano hay 1 y con la otra pasas una cantidad que hace que te quedes igual que antes y te puedan matar entonces se cambia al valor de k
        if (n2 + k == n1 and n2 + k >= n and n1 - k == 1):
            k = r.randint(1, k-1)
        if (cont == n1):
            break
    return k

def repartir2(n1, n2, c1, c2, accion): # se encarga de toda la lógica de repartir
    accion = 'reparte'
    mb = ''
    e = r.randint(0, 1)
    k1, k2 = int(), int() # cantidad que se pasa de una mano a otra de la mano 1 y 2, respectivamente
    
    # condición para que si una mano es 0, entonces no pueda repartir
    if (n1 == 0):
        e = 1
        k2 = repartir(n2, n1, c1, c2)
    elif (n2 == 0):
        e = 0
        k1 = repartir(n1, n2, c1, c2)
    # si las manos son diferente de 0, repartirán
    elif (n1 != 0 and n2 != 0):
        k1 = repartir(n1, n2, c1, c2)
        k2 = repartir(n2, n1, c1, c2)
        # evita que un jugador se suicide
        if (n1 == 1 and n1 + n2 >= n):
            e = 1
        elif (n2 == 1 and n1 + n2 >= n):
            e = 0

    # evita atacar si te perjudica
    if ((n1 + c1 >= n and n2 == 0) or (n1 + c2 >= n and n2 == 0) or (n2 + c1 >= n and n1 == 0) or (n2 + c2 >= n and n1 == 0)):
        e = r.randint(0, 1)

    # evita que si en una mano tienes 1 y en otra 0, pases a la otra 1
    if (n1 == 0 and n2 == 1 or n1 == 1 and n2 == 0):
        e = 0

    # evita que al repartir te puedan matar una mano
    if (n2 + k1 + c1 >= n or n2 + k1 + c2 >= n or k2 != 0):
        e = 1
    elif (n1 + k2 + c1 >= n or n1 + k2 + c2 >= n or k1 != 0):
        e = 0
    # reparte sólo si no perjudica
    if ((n2 + k1 + c1 >= n) or (n2 + k1 + c2 >= n) and (n1 + k2 + c1 >= n) or (n1 + k2 + c2 >= n)):
        e = 2
        #print(1)
    elif ((n2 + k1 + c1 >= n) or (n2 + k1 + c2 >= n)):
        e = 1
        #print(2)
    elif ((n1 + k2 + c1 >= n) or (n1 + k2 + c2 >= n)):
        e = 0
        #print(3)
    #print('k1 =',k1)
    #print('k2 =',k2)

    #aquí es donde se ejecuta la accion de repartir
    if (e == 0):
        n1 -= k1
        n2 += k1
        ma = 'M1'
        mb = 'M2'
    elif (e == 1):
        n2 -= k2
        n1 += k2
        ma = 'M2'
        mb = 'M1'
    else:
        c1, c2, ma, mb, accion = sumar2(n1, n2, c1, c2, accion)

    return n1, n2, c1, c2, ma, mb, accion

def logica(n1, n2, c1, c2, cont1, accion): # se encarga de gestionar la lógica general del juego
    e = r.randint(0, 1)

    # evita atacar si te perjudica
    if (
        2*n1 + c1 >= n or
        2*n1 + c2 >= n or
        2*n2 + c1 >= n or
        2*n2 + c2 >= n or
        n1 + n2 + c1 >= n or
        n1 + n2 + c2 >= n or
        (n1 + c1 >= n and n2 == 0) or
        (n1 + c2 >= n and n2 == 0) or
        (n2 + c1 >= n and n1 == 0) or
        (n2 + c2 >= n and n1 == 0)
    ):
        e = 1

    # evita que se pueda repartir teniendo un 0 y un 1 en cada mano
    if ((n1 == 1 and n2 == 0) or (n1 == 0 and n2 == 1)):
        e = 0

    # si se puede matar, se matará, excepto si te perjudica
    if ((n1 + c1 >= n and n1 + c2 < n) or (n1 + c2 >= n and n1 + c1 < n) or (n2 + c1 >= n and n2 + c2 < n) or (n2 + c2 >= n and n2 + c1 < n)):
        e = 0

    # evita que si una vez que alguien haya repartido, la otra no pueda repartir si luego volverán al mismo estado anterior
    if (accion == 'reparte'):
        cont1 += 1

    # sólo se podrá repartir 4 veces seguidas entre ambos jugadores (mejorar esta regla)
    if (cont1 == 4):
        e = 0
        cont1 = 0

    # sumar o repartir
    if (e == 0): # sumar
        c1, c2, ma, mb, accion = sumar2(n1, n2, c1, c2, accion)

    elif(e == 1): # repartir
        n1, n2, c1, c2, ma, mb, accion = repartir2(n1, n2, c1, c2, accion)

    return n1, n2, c1, c2, ma, mb, cont1, accion

def juego(n1, n2, c1, c2, cont1, accion): # se encarga de iniciar la partida
    # contador
    cont = 0

    # indica el turno de cada jugador, True: turno del jugador 1, False: turno del jugador 2
    d = False

    # variable auxiliar para elegir una función aleatoriamente
    e = int()

    # texto final
    text = str()

    # número que se reparte
    k1, k2  = int(), int()

    # manos de jugador 1 y 2
    ma, mb = str(), str()
    while ((n1 != 0 or n2 != 0) and (c1 != 0 or c2 != 0)):
        cont += 1
        d = not(d)
        if (d): # jugador 1
            j = 1
            n1, n2, c1, c2, ma, mb, cont1, accion = logica(n1, n2, c1, c2, cont1, accion)
        else: # jugador 2
            j = 2
            c1, c2, n1, n2, ma, mb, cont1, accion = logica(c1, c2, n1, n2, cont1, accion)

        # es el estado de cada jugador que se va mostrando cada vez por pantalla
        text = Fore.CYAN+'J1'+Style.RESET_ALL+' :[M1: %i, M2: %i]' %(n1, n2) + '\n'
        text += Fore.RED+'J2'+Style.RESET_ALL+' :[M1: %i, M2: %i]' %(c1, c2)
        print(Style.BRIGHT+Fore.GREEN+'Jugada: '+Style.RESET_ALL+Fore.YELLOW+'%i' %(cont)+Style.RESET_ALL)
        print(Style.BRIGHT+Fore.MAGENTA+'Jugador %i '%(j)+Style.BRIGHT+Fore.RED+'%s ' %(accion)+Style.RESET_ALL+'con %s a %s' %(ma, mb))
        print(text, '\n')

    # indica cuál es el jugador que ha ganado
    if (n1 == 0 and n2 == 0):
        j = 2
    else:
        j = 1

    # jugador que gana
    print(Style.BRIGHT+Fore.BLUE+'¡JUGADOR',j, 'GANA!'+Style.RESET_ALL)
    return n1, n2, c1, c2

def modoDeJuego():
    pass
    # persona contra persona
    # persona contra maquina
    # máquina contra máquina #controla los modos de juego

# estado inicial
print(Fore.CYAN+'J1'+Style.RESET_ALL+' :[M1: %i, M2: %i]' %(a1, a2))
print(Fore.RED+'J2'+Style.RESET_ALL+' :[M1: %i, M2: %i]' %(b1, b2) + '\n')

# partida
a1, a2, b1, b2 = juego(a1, a2, b1, b2, cont1, accion)
