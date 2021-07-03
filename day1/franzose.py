# Python - Pygame Zero - Mu-Editor
# https://pygame-zero.readthedocs.io/de/latest/index.html
#
# Neues Spiel mit dem Titel "Der Franzose"

TITLE = "Der Franzose"

# Größe unseres Spielfeldes (Fenstergröße)

WIDTH = 800
HEIGHT = 500

# Wir initialisieren unsere Spielfigur
# und setzen gleich die initiale Position
# geht auch: franzose.pos = WIDTH / 2, HEIGHT / 2

franzose = Actor('franzose', (WIDTH / 2, HEIGHT / 2))

# draw()-Funktion - zeichnet unsere Spielfläsche
# Pygame Zero ruft diese Funktion immer dann auf,
# wenn der Bildschirm neu gezeichnet werden muss.

def draw():
    # Setzt den Hintergrund blau
    # Alle möglich Farbe-Codes findest du unter
    # https://pygame-zero.readthedocs.io/en/latest/colors_ref.html

    screen.fill('aliceblue')

    # Zeichnet unsere Spielfigur

    franzose.draw()

# Pygame Zero ruft die Funktion update() automatisch
# in jedem Frame auf. Indem wir das Alien in jedem Frame
# etwas verschieben, sieht es so aus, als ob sich das Alien bewegt.

def update():
    franzose.x = franzose.x + 1

