# Python - Pygame Zero - Mu-Editor
# https://pygame-zero.readthedocs.io/de/latest/index.html
#
# Soo, dass war der letzt Tag! Es hat uns sehr viel Spaß gemacht!

from random import randint

from time import time

# Neues Spiel mit dem Titel "Der Franzose"
TITLE = "Der Franzose"

# Größe unseres Spielfeldes (Fenstergröße)
WIDTH = 1200
HEIGHT = 800

# wie schnell lässt sich unsere Spielfigur bewegen (in Pixel)
speed = 4

# wie schnell bewegt sich unser Gegener bei Spielbeginn (in Pixel)
XposBaecker = 2
YposBaecker = 2

# Hiermit steuern wir das Spiel, wenn der Gegener uns berühert
game_over = False

# Hiermit steuern wir das Spiel, wenn die Zeit abgelaufen ist
game_end = False

# Hiermit steuern wir die Schwirgkeit im Spiel
level_up = False

# Unsere Punktezahl
score = 0

# Für unseren Counter benötigen wir den Timestamp beim Spielstart
timestamp_start = time()

# und wie lang unser Spiel dauern soll (in Sekunden)
game_duration = 60

# Wir initialisieren unsere Spielfiguren
franzose = Actor('franzose', (WIDTH / 2, HEIGHT / 2), anchor=('center', 'bottom'))

baecker = Actor('baecker')

# Je nach Punktezahl lassen wir bis zu drei Brote erscheinen
# Jedes Brot muss einzeln als eigenes Objekt initialisiert werden
# Das machen wir mit einer Liste - brote[0 bis 2]
brote = [0, 1, 2]

# in einer for-Schleife initialisieren wir die einzelnen Spielfiguren
# und setzen einen Merker für seine Sichtbarkeit
for x in brote:
    brote[x] = Actor('brot', (randint(0, WIDTH), randint(0, HEIGHT)))
    brote[x].isDraw = False

# draw()-Funktion - zeichnet unsere Spielfläsche
# Pygame Zero ruft diese Funktion immer dann auf,
# wenn der Bildschirm neu gezeichnet werden muss.
def draw():

    if game_over:  # Wenn wir das Spiel verlieren, dann mache
        screen.fill('mistyrose')  # farbischer Hintergrund. Alle möglich Farbe-Codes findest du unter
        # https://pygame-zero.readthedocs.io/en/latest/colors_ref.html
        screen.draw.text('GAME OVER!!!', (WIDTH/2 - 180, HEIGHT/2), fontsize=100)
        screen.draw.text('Dein Score: ' + str(score), (0 , 0), color='black', fontsize=100)
        franzose.draw()
    elif game_end:  # oder wenn das Spiel zu ende ist, dann mache:
        screen.fill('greenyellow')
        screen.draw.text('Super!', (WIDTH/2 - 180, HEIGHT/2), fontsize=100)
        screen.draw.text('Dein Score: ' + str(score), (0 , 0), color='black', fontsize=100)
    else:  # ansonst mache das...
        # Setzt das Hintergrundbild backscreen.png. Wenn möglich, sollte es so groß sein
        # wie das Spielfeld
        screen.blit("backscreen", (0, 0))

        # Hier geben wir jetzt noch die Sekunden aus, die nach untern zählen:
        # gewünschte Spieldauer - (akueller Timestamp - Timestamp vom Spielbeginn)
        screen.draw.text('Score: ' + str(score) + '   Time: ' + str(int(game_duration - (time() - timestamp_start))), (0 , 0), color='black', fontsize=40)

    # Zeichnet unsere Spielfigur
    baecker.draw()
    franzose.draw()

    # Ein Brot wird immer angezeigt
    brote[0].isDraw = True
    brote[0].draw()

    if score > 5:  # ab 5 Punke kommt das zweite Brot dazu
        brote[1].isDraw = True
        brote[1].draw()
    if score > 10:  # ab 10 Punkte das dritte...
        brote[2].isDraw = True
        brote[2].draw()
# Pygame Zero ruft die Funktion update() automatisch
# in jedem Frame auf. Indem wir die Positionen unserer Speilfiguren für jedem Frame
# verändern, sieht es so aus, als ob sie sich bewegen.
def update():

    global XposBaecker, YposBaecker, game_over, game_end, score, level_up, timestamp_start, brote

    if not game_end and not game_over:
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
    if time() > timestamp_start + game_duration:
        game_end = True

    # Hier durchlaufen wir unsere Brote-Liste und prüfen jedes einzelnen
    # Brot, ob es den Franzosen berühert.
    # Aber nur, wenn isDraw true ist!
    for brot in brote:
        if franzose.colliderect(brot) and brot.isDraw:
            brot.x = randint(0, WIDTH)
            brot.y = randint(0, HEIGHT)
            score += 1
            level_up = True

    if score in (2, 4, 6, 8, 10, 12, 14, 16) and level_up:
        XposBaecker *= 1.2
        YposBaecker *= 1.2
        level_up = False

