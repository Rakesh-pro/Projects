from turtle import *
from random import randrange
from freegames import square, vector



w=Screen()

w.title('ShowBot-Snake_Game')

w.bgpic("outputs.gif")                                  

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

def change(x, y):
    "Change snake direction."
    aim.x = x                                            #x-axis
    aim.y = y                                            #y-axis

def inside(head):                                        #Boundary
    "Return True if head inside boundaries."
    return -400 < head.x < 390 and -200 < head.y < 200   # Fixing wall or  boundaries

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:                #  The first cond is 'is snake is in boundary?'
        square(head.x, head.y, 9, 'red')                 #  The second cond is 'is snake touched its own body'
        update()                                         #  if any one is True The snake head will becomes Red'
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-35, 35) * 10                 # if snake eaten the existing food
        food.y = randrange(-19, 19) * 10                 # below stmts will helps to show another food
    else: snake.pop(0)

    clear()

    for body in snake: square(body.x, body.y, 9, 'red')

    square(food.x, food.y, 9, 'cyan')
    update()
    ontimer(move, 100)


hideturtle()                                             #hiding turtle till execution or compiling of whole code
tracer(False)
listen()

onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')

move()

bgcolor("black")                                         #background color

done()
'''
I added a gif image to turtle window
Ensuring that i have installed ''freegames'' module prior to run
  comands in cmd    'pip install freegames'
  
->first,save gif image and the python file in same folder

->and by running the python file in interpretor i got a pic on snake game

-> in the above case the picture is ''outputs.gif''
'''
