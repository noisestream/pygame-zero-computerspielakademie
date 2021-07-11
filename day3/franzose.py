# Python - Pygame Zero - Mu-Editor
# https://pygame-zero.readthedocs.io/de/latest/index.html
#
# Neues Spiel mit dem Titel "Der Franzose"

from random import randint

TITLE = "Der Franzose"

WIDTH = 1600
HEIGHT = 1000

speed = 4

# wir haben neue Variabeln gesetzt:

# unsere Bäcker ändert seine Richtung anhand dieser Werte
# jeweils für die x- und y-Position
XposBaecker = 2
YposBaecker = 2

# mit game_over steueren wir, wann unser Spiel zu ende ist
game_over = False

# Unser Punktestand
score = 0

# Wir haben nun drei Akteure in unserem Spiel, die wir hier
# als Opjekte initialisieren

franzose = Actor('franzose', (WIDTH / 2, HEIGHT / 2), anchor=('center', 'bottom'))

baecker = Actor('baecker')

brot = Actor('brot', (randint(0, WIDTH), randint(0, HEIGHT)))

def draw():

    if game_over: # wenn game_over wahr ist, dann ...
        screen.fill('red') # zeichne einen roten Hintergund und
        # Gebe 'GAME OVER' in der Mitte des Bildschirms aus
        screen.draw.text('GAME OVER!!!', (WIDTH/2 - 180, HEIGHT/2), fontsize = 100)
    else: # wenn game_over falsch ist, dann zeichne unsere Spielfiguren
        screen.fill('aliceblue')
        baecker.draw()
        franzose.draw()
        brot.draw()
        screen.draw.text('Score: ' + str(score), (0 , 0 ), color='black', fontsize = 40)


def update():

    # wichtig: Variabel aus dem Hauptteil des Programmes können in
    # Funktionen nur geändert werden, wenn sie der Funktionen
    # bekannt sind:

    global XposBaecker, YposBaecker, game_over, score

    if keyboard.right and franzose.right < WIDTH:
        franzose.x += speed
    if keyboard.left and franzose.left > 0:
        franzose.x -= speed
    if keyboard.up and franzose.top > 0:
        franzose.y -= speed
    if keyboard.down and franzose.bottom < HEIGHT:
        franzose.y += speed

    # hier ändern wir die Position des Bäckers...
    baecker.x += XposBaecker
    baecker.y += YposBaecker

    # und prüfen, ob er einen Rand berühert. Wenn ja,
    # änderen wir die Werte in die jeweiligen Gegenzahl um
    # also positiv in negativ und umgedreht
    if baecker.right > WIDTH or baecker.left < 0:
        XposBaecker = -XposBaecker
    if baecker.top < 0 or baecker.bottom > HEIGHT:
        YposBaecker = -YposBaecker

    # Mit der Funktion colliderect() der Klasse Actor
    # können wir prüfen, ob sich zwei Objekte berühren
    # Hier der Franzose und der Bäcker: Game Over!
    if franzose.colliderect(baecker):
        game_over = True

    # und hier Sammel wir das Brot ein und zählen
    # jedesmal den Score hoch
    if franzose.colliderect(brot):
        brot.x = randint(0, WIDTH)
        brot.y = randint(0, HEIGHT)
        score += 1


