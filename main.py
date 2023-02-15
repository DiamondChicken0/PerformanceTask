import pygame as py
import pygame.gfxdraw as pydraw
from enum import Enum
py.init()

size = (1280, 720)
screen = py.display.set_mode(size)
py.display.set_caption("Cool Game")

skyBlue = (89, 247, 255)
oceanBlue = (89, 136, 255)
sandYellow = (255, 249, 128)
sandOutline = (173, 169, 87)

class States(Enum):
    mainMenu = 1

state = States.mainMenu
clock = py.time.Clock()

skyBG = py.Rect(0, 0, 1280, 720)
running = True


while running:
    
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
    
    if state == States.mainMenu:
        introRunning = True
        while introRunning:
            py.draw.rect(screen, skyBlue, skyBG)
            pydraw.filled_ellipse(screen, 640, 620, 1500, 200, sandYellow)
            pydraw.filled_ellipse(screen, )
            py.display.flip()


    py.display.flip()
    clock.tick(60)

py.quit()