from random import *
from turtle import *
from freegames import path

car = path('car.gif')
emojiTiles = ["\U0001F600", "\U0001F603", "\U0001F604", "\U0001F601", "\U0001F606", "\U0001F605", "\U0001F923", "\U0001F602", "\U0001F642", "\U0001F643", "\U0001F609", "\U0001F60A", "\U0001F607", "\U0001F970", "\U0001F60D", "\U0001F929", "\U0001F618", "\U0001F617", "\U0001F61A", "\U0001F619", "\U0001F60B", "\U0001F61B", "\U0001F61C", "\U0001F92A", "\U0001F61D", "\U0001F911", "\U0001F917", "\U0001F92D", "\U0001F92B", "\U0001F914", "\U0001F910", "\U0001F928"]
emojiTiles = [val for val in emojiTiles for _ in (0, 1)]

state = {'mark': None}
hide = [True] * 64

def square(x, y):
    "Draw white square with black outline at (x, y)."
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def tap(x, y):
    "Update mark and hidden tiles based on tap."
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or emojiTiles[mark] != emojiTiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None

def draw():
    "Draw image and tiles."
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
        up()
        goto(x + 2, y)
        color('black')
        write(emojiTiles[mark], font=('Arial', 30, 'normal'))

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