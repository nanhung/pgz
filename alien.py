import pgzrun

alien = Actor('alien')
#alien.pos = 56, 56
alien.topright = 0, 10

WIDTH = 500
HEIGHT = alien.height + 20


def draw():
    screen.clear()
    alien.draw()

def update():
    alien.left += 4
    if alien.left > WIDTH:
        alien.right = 0

def on_mouse_down(pos):
    if alien.collidepoint(pos):
        print("Eek!")
    else:
        print("You missed me!")

pgzrun.go()
