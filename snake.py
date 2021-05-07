"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to arrow keys.

"""

from turtle import *
from random import randrange
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

colores = ["green", "blue", "magenta", "yellow", "black"]

colorSnake = colores[randrange(0,5)]
colorFood = colores[randrange(0,5)]

while colorFood == colorSnake:
    colorFood = colores[randrange(0,5)]


def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

#Función para mover la comida, se le pasa una opción aleatoria
#Si el movimiento hecho saca a la comida de las barreras, se 
#regresa la comida a su lugar y se llama recursivamente a la función
#con otra opción al azar
def moveFood(option):
    if option == 1: #Mover a la derecha
        food.x = food.x+10
        if not inside(food):
            food.x = food.x-10
            moveFood(randrange(1,5))
    elif option == 2: #Mover a la izquierda
        food.x = food.x-10
        if not inside(food):
            food.x = food.x+10
            moveFood(randrange(1,5))
    elif option == 3: #Mover arriba
        food.y = food.y+10
        if not inside(food):
            food.y = food.y-10
            moveFood(randrange(1,5))
    else: #Mover abajo
        food.y = food.y-10
        if not inside(food):
            food.y = food.y+10
            moveFood(randrange(1,5))

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        moveFood(randrange(1,5)) #Si no se come la comida, moverla
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, colorSnake)

    square(food.x, food.y, 9, colorFood)
    update()
    ontimer(move, 100)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
