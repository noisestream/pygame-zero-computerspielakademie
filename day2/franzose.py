# Python - Pygame Zero - Mu-Editor
# https://pygame-zero.readthedocs.io/de/latest/index.html
#
# Neues Spiel mit dem Titel "Der Franzose"

TITLE = "Der Franzose"

WIDTH = 800
HEIGHT = 500

speed = 4

franzose = Actor('franzose', (WIDTH / 2, HEIGHT / 2), anchor=('left', 'bottom'))

def draw():

    screen.fill('aliceblue')
    franzose.draw()

def update():
    if keyboard.right and franzose.right < WIDTH:
        franzose.x += speed
    if keyboard.left and franzose.left > 0:
        franzose.x -= speed
    if keyboard.up and franzose.top > 0:
        franzose.y -= speed
    if keyboard.down and franzose.bottom < HEIGHT:
        franzose.y += speed



