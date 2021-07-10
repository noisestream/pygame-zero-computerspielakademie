# Python - Pygame Zero - Mu-Editor
# https://pygame-zero.readthedocs.io/de/latest/index.html
#
# Neues Spiel mit dem Titel "Der Franzose"

from random import randint

TITLE = "Der Franzose"

WIDTH = 1600
HEIGHT = 1000

speed = 4
XposBaecker = 2
YposBaecker = 2
game_over = False
score = 0

franzose = Actor('franzose', (WIDTH / 2, HEIGHT / 2), anchor=('center', 'bottom'))

baecker = Actor('baecker')

brot = Actor('brot', (randint(0, WIDTH), randint(0, HEIGHT)))

def draw():

    if game_over:
        screen.fill('red')
        screen.draw.text('GAME OVER!!!', (WIDTH/2 - 180, HEIGHT/2), fontsize = 100)
    else:
        screen.fill('aliceblue')
        baecker.draw()
        franzose.draw()
        brot.draw()
        screen.draw.text('Score: ' + str(score), (0 , 0 ), color='black', fontsize = 40)


def update():

    global XposBaecker, YposBaecker, game_over, score

    if keyboard.right and franzose.right < WIDTH:
        franzose.x += speed
    if keyboard.left and franzose.left > 0:
        franzose.x -= speed
    if keyboard.up and franzose.top > 0:
        franzose.y -= speed
    if keyboard.down and franzose.bottom < HEIGHT:
        franzose.y += speed

    baecker.x += XposBaecker
    baecker.y += YposBaecker

    if baecker.right > WIDTH or baecker.left < 0:
        XposBaecker = -XposBaecker
    if baecker.top < 0 or baecker.bottom > HEIGHT:
        YposBaecker = -YposBaecker

    if franzose.colliderect(baecker):
        game_over = True

    if franzose.colliderect(brot):
        brot.x = randint(0, WIDTH)
        brot.y = randint(0, HEIGHT)
        score += 1


