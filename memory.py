# Juego de memoria basado en la colección de FreeGames
# donde se hicieron modificaciones para una mejor experiencia
# de juego.
# Autores: Regina Luna, A01655821
#          Diego Samperio, A01662935
#          Abigail Curiel, A01655892
# Fecha: 23/03/2023

# Se importan las librerías que se utilizarán.
from random import *
from turtle import *
from freegames import path
import time

car = path('car.gif')

# Se crea una lista con emojis para asignar a cada casilla.
emojiTiles = [
    "\U0001F600",
     "\U0001F603",
     "\U0001F604", 
     "\U0001F601",
     "\U0001F606",
     "\U0001F605",
     "\U0001F923",
     "\U0001F602",
     "\U0001F642",
     "\U0001F643",
     "\U0001F609",
     "\U0001F60A",
     "\U0001F607",
     "\U0001F970",
     "\U0001F60D",
     "\U0001F929",
     "\U0001F618",
     "\U0001F617",
     "\U0001F61A",
     "\U0001F619",
     "\U0001F60B",
     "\U0001F61B",
     "\U0001F61C",
     "\U0001F92A",
     "\U0001F61D",
     "\U0001F911",
     "\U0001F917",
     "\U0001F92D",
     "\U0001F92B",
     "\U0001F914",
     "\U0001F910",
     "\U0001F928"]

# Se duplica cada elemento de la lista de emojis.
emojiTiles = [val for val in emojiTiles for _ in (0, 1)]

state = {'mark': None}
hide = [True] * 64
# Se crea una variable para guardar el número de taps
# que el jugador hace.
numero_taps = 0

# Función para dibujar un cuadrado blanco con márgenes
# negros en la posición (x,y).
# Toma como parámetros las coordenadas donde se 
# dibujará el cuadrado.
# No hay valor de retorno.
def square(x, y):
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

# Función que convierte coordenadas de tipo (x, y) a
# índices de la lista de emojis.
# Toma como parámetros las coordenadas con las que se
# escogerá un índice de la lista.
# Se regresa el índice para seleccionar un emoji particular.
def index(x, y):
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

# Función que convierte la cuenta de casillas a coordenadas
# de tipo (x,y)
# Toma como parámetro la cuenta de casillas.
# Regresa las coordenadas x y y de una casilla.
def xy(count):
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

# Función que actualiza las casillas marcadas y escondidas
# basándose en sus taps. 
# Toma como parámetro las coordenadas de un tap particular.
# No hay valor de retorno.
def tap(x, y):
    spot = index(x, y)
    mark = state['mark']

    # Se actualiza el número total de taps.
    global numero_taps
    numero_taps += 1

    if mark is None or mark == spot or emojiTiles[mark] != emojiTiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
# Función para revisar si todas las casillas ya han sido reveladas
# No tiene parámetros.
# Regresa True si todas las casillas ya han sido reveladas, False en otro caso.
def allTilesRevealed():
    for tile in hide:
        if tile:
            return False
    return True
# Función que dibuja la imagen, las casillas y taps.
# No tiene parámetros.
# No hay valor de retorno.
def draw():
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)

        # Se centra el emoji en la casilla.
        up()
        goto(x + 5, y + 5)
        write(emojiTiles[mark], font=('Arial', 30, 'normal'))

    # Se despliega en pantalla el número de taps.
    up()
    goto(x=-197, y=183)
    write(numero_taps, False, font=('Arial', 10, 'normal'))
    if allTilesRevealed():
        goto(-110,-30)
        color('white')
        write("GANASTE",False, font=('Arial',35,'normal'))
    update()

        
    ontimer(draw, 100)
shuffle(emojiTiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()