# Python - Pygame Zero - Mu-Editor
# https://pygame-zero.readthedocs.io/de/latest/index.html
#
# Neues Spiel mit dem Titel "Der Franzose"

from random import randint

# Wir importieren die Funktion time() aus dem Modul time
# Die nutzen wir, um unseren Counter zu programmieren:
# Ein Spiel soll nur eine bestimmte Zeit lang gehen
from time import time

TITLE = "Der Franzose"

WIDTH = 1200
HEIGHT = 800

speed = 4

XposBaecker = 2
YposBaecker = 2

game_over = False

level_up = False

score = 0

# Wir speichern uns die aktuell Zahl aus der Funktion time()
# Sie gibt dabei die Anzahl der Sekunden an, die seit dem 01.01.1970 vergangen sind
# Mit dieser Zahl lässt es sich gut rechnen.
# Diese Zahl wird auch Timestamp genannt.
timer_now_sek = time()

# Hier können wir festlegen, wie lang unser Spiel dauern soll (in Sekunden)
game_duration = 60

# Hiermit steuern wir das Spiel, wenn die Zeit abgelaufen ist
game_end = False

# Wir initialisieren unsere Spielfiguren
franzose = Actor('franzose', (WIDTH / 2, HEIGHT / 2), anchor=('center', 'bottom'))

baecker = Actor('baecker')

print(inspect.getdoc(baecker))

# Je nach Punktezahl lassen wir bis zu drei Brote erscheinen
# Jedes Brot muss einzeln als eigenes Objekt initialisiert werden
# Das machen wir mit einer Liste - brote[0 bis 2]
brote = [0,1,2]

# in einer for-Schleife initialisieren wir die einzelnen Spielfiguren
# und setzen einen Merker für seine Sichtbarkeit
for x in brote:
    brote[x] = Actor('brot', (randint(0, WIDTH), randint(0, HEIGHT)))
    brote[x].isDraw = False

def draw():

    if game_over: # Wenn wir das Spiel verlieren, dann mache
        screen.fill('mistyrose')
        screen.draw.text('GAME OVER!!!', (WIDTH/2 - 180, HEIGHT/2), fontsize = 100)
        screen.draw.text('Dein Score: ' + str(score), (0 , 0 ), color='black', fontsize = 100)
    elif game_end: # oder wenn das Spiel zu ende ist, dann mache:
        screen.fill('greenyellow')
        screen.draw.text('Super!', (WIDTH/2 - 180, HEIGHT/2), fontsize = 100)
        screen.draw.text('Dein Score: ' + str(score), (0 , 0 ), color='black', fontsize = 100)
    else: # ansonst mache das...
        screen.fill('aliceblue')
        baecker.draw()
        franzose.draw()

        # Ein Brot wird immer angezeigt
        brote[0].isDraw = True
        brote[0].draw()

        if score > 5: # ab 5 Punke kommt das zweite Brot dazu
            brote[1].isDraw = True
            brote[1].draw()
        if score > 10: # ab 10 Punkte das dritte...
            brote[2].isDraw = True
            brote[2].draw()

        # Hier geben wir jetzt noch die Sekunden aus, die nach untern zählen:
        # gewünschte Spieldauer - (akueller Timestamp - Timestamp vom Spielbeginn)
        screen.draw.text('Score: ' + str(score) + '   Time: ' + str(int(game_duration - (time() - timer_now_sek))), (0 , 0 ), color='black', fontsize = 40)


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

    # Hier prüfen wir, wann die gewünscht Spieldauer vorbei ist
    if time() > timer_now_sek + game_duration:
        game_end = True

    for brot in brote:
        if franzose.colliderect(brot) and brot.isDraw == True:
            brot.x = randint(0, WIDTH)
            brot.y = randint(0, HEIGHT)
            score += 1
            level_up = True

    if score in (2, 4, 6, 8, 10, 12, 14, 16) and level_up:
        XposBaecker *= 1.2
        YposBaecker *= 1.2
        level_up = False

