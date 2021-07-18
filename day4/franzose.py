# Python - Pygame Zero - Mu-Editor
# https://pygame-zero.readthedocs.io/de/latest/index.html
#
# Neues Spiel mit dem Titel "Der Franzose"

from random import randint

import time

TITLE = "Der Franzose"

WIDTH = 1200
HEIGHT = 800

speed = 4

XposBaecker = 2
YposBaecker = 2

game_over = False

game_end = False

level_up = False

score = 0

game_duration = 10

timer_now_sek = time.time()

print(timer_now_sek)



franzose = Actor('franzose', (WIDTH / 2, HEIGHT / 2), anchor=('center', 'bottom'))

baecker = Actor('baecker')

brote = [0,1,2]

for x in brote:
    brote[x] = Actor('brot', (randint(0, WIDTH), randint(0, HEIGHT)))

def draw():

    if game_over:
        screen.fill('mistyrose')
        screen.draw.text('GAME OVER!!!', (WIDTH/2 - 180, HEIGHT/2), fontsize = 100)
        screen.draw.text('Dein Score: ' + str(score), (0 , 0 ), color='black', fontsize = 100)
    elif game_end:
        screen.fill('greenyellow')
        screen.draw.text('Super!', (WIDTH/2 - 180, HEIGHT/2), fontsize = 100)
        screen.draw.text('Dein Score: ' + str(score), (0 , 0 ), color='black', fontsize = 100)
    else:
        screen.fill('aliceblue')
        baecker.draw()
        franzose.draw()
        brote[0].draw()

        if score > 5:
            brote[1].draw()
        if score > 10:
            brote[2].draw()

        screen.draw.text('Score: ' + str(score) + '   Time: ' + str(int(game_duration - (time.time() - timer_now_sek))), (0 , 0 ), color='black', fontsize = 40)


def update():

    global XposBaecker, YposBaecker, game_over, game_end, score, level_up, timer_now_sek, brote

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

    if time.time() > timer_now_sek + game_duration:
        game_end = True

    for brot in brote:
        if franzose.colliderect(brot):
            brot.x = randint(0, WIDTH)
            brot.y = randint(0, HEIGHT)
            score += 1
            level_up = True

    #print( 'X = ' + str(XposBaecker) + '  Y =' + str(YposBaecker))

    if score in (2, 4, 6, 8, 10, 12, 14, 16) and level_up:
        XposBaecker *= 1.2
        YposBaecker *= 1.2
        level_up = False




