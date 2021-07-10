# Python - Pygame Zero - Mu-Editor
# https://pygame-zero.readthedocs.io/de/latest/index.html
#
# Neues Spiel mit dem Titel "Der Franzose"

TITLE = "Der Franzose"

WIDTH = 800
HEIGHT = 500

# wir definieren eine neue Variable, womit wir die
# Bewegungsgeschwindigkeit unserer Spielfigur
# schnell ändern können

speed = 4

# Unsere initiale Spielfigur (Akteur) erhält einen neuen Parameter:
# Akteure haben eine "Ankerposition", mit dem wir unsere Akteure
# in unserem Spiel positionieren können.
# Standardmäßig ist die Ankerposition die Mitte,
# daher bezieht sich das Attribut .pos auf die Mitte des Akteurs
# (und damit auch auf die x- und y-Koordinaten).
# Wir setzen ihn ganz unten in die Mitte, also zu den Füßen

franzose = Actor('franzose', (WIDTH / 2, HEIGHT / 2), anchor=('center', 'bottom'))

def draw():

    screen.fill('aliceblue')
    franzose.draw()

def update():

    # Die Steuerung unserer Spielfigur
    # Wir prüfen, ob die Pfleiltaste gedrückt wurden
    # und ob unsere Spielfigur sich innerhalb unserer
    # Spielfläsche befindet.

    if keyboard.right and franzose.right < WIDTH:
        franzose.x += speed
    if keyboard.left and franzose.left > 0:
        franzose.x -= speed
    if keyboard.up and franzose.top > 0:
        franzose.y -= speed
    if keyboard.down and franzose.bottom < HEIGHT:
        franzose.y += speed



