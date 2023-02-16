import pygame as py
import pygame.gfxdraw as pydraw
from enum import Enum
py.init()

size = (1280, 720)
screen = py.display.set_mode(size)
py.display.set_caption("Cool Game")

skyBlue = (89, 247, 255)
oceanBlue = (89, 136, 255)
darkBlue = (0, 51, 204)
sandYellow = (255, 249, 128)
sandOutline = (173, 169, 87)
grassGreen = (102, 255, 102)
darkGreen = (51, 153, 51)
woodBrown = (153, 102, 51)

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
        j = 0
        while introRunning:
            if j < 570:
                j = j + 2.5
            py.draw.rect(screen, skyBlue, skyBG)
            pydraw.box(screen, ((0,400), (1280,500)), grassGreen)

            pydraw.filled_ellipse(screen, 0, 550, 215, 215, darkGreen)
            pydraw.filled_ellipse(screen, 150, 550, 315, 265, darkGreen)
            pydraw.filled_ellipse(screen, 400, 500, 265, 415, darkGreen)
            pydraw.filled_ellipse(screen, 750, 550, 215, 315, darkGreen)
            pydraw.filled_ellipse(screen, 1100, 550, 415, 415, darkGreen)

            pydraw.filled_ellipse(screen, 0, 550, 200, 200, grassGreen)
            pydraw.filled_ellipse(screen, 150, 550, 300, 250, grassGreen)
            pydraw.filled_ellipse(screen, 400, 500, 250, 400, grassGreen)
            pydraw.filled_ellipse(screen, 750, 550, 200, 300, grassGreen)
            pydraw.filled_ellipse(screen, 1100, 550, 400, 400, grassGreen)

            pydraw.filled_ellipse(screen, 640, 680, 1510, 210, sandOutline)
            pydraw.filled_ellipse(screen, 640, 680, 1500, 200, sandYellow)

            for i in range(0,33):
                pydraw.filled_ellipse(screen, i * 40, 720, 60, 110, darkBlue)
            for i in range(0,33):
                pydraw.filled_ellipse(screen, i * 40, 720, 50, 100, oceanBlue)
            
            pydraw.box(screen, ((190, j - 530), (900,520)), (0,0,0))
            pydraw.box(screen, ((200, j - 520), (880,500)), woodBrown)
            
            
            
            

            py.display.flip()
            clock.tick(60)
            for event in py.event.get():
                if event.type == py.QUIT:
                    introRunning = False
                    running = False


    py.display.flip()
    clock.tick(60)

py.quit()