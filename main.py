import pygame as py
import pygame.gfxdraw as pydraw
from enum import Enum
py.init()
py.font.init()

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
lightGray = (163, 163, 163)
gray = (64, 64, 64)
grayRoad = (85,85,85)
darkWood = (56, 46, 17)
lightWood = (135, 112, 45)

class States(Enum):
    mainMenu = 1
    transition = 2
    mainGame = 3

state = States.mainMenu
clock = py.time.Clock()

skyBG = py.Rect(0, 0, 1280, 720)
running = True

titleFont = py.font.SysFont("Trebuchet MS", 150)
titleText = titleFont.render("Bot Defense", True, (255,255,0))
titleTextBG = titleFont.render("Bot Defense", True, (200,200,0))

subTitleFont = py.font.SysFont("Tahoma", 90)
startGameText = subTitleFont.render("Start Game", True, (255,255,255))

while running:
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
    
    if state == States.mainMenu:
        introRunning = True
        introDone = False
        j = 0
        while introRunning:
            if j < 570:
                j = j + 2.5
            else:
                introDone = True
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

            screen.blit(titleTextBG, (235 + 3, j - 490 - 3))
            screen.blit(titleTextBG, (235 + 3, j - 490 + 3))
            screen.blit(titleTextBG, (235 - 3, j - 490 - 3))
            screen.blit(titleTextBG, (235 - 3, j - 490 + 3))
            screen.blit(titleTextBG, (235 + 3, j - 490))
            screen.blit(titleTextBG, (235 - 3, j - 490))
            screen.blit(titleTextBG, (235, j - 490 - 3))
            screen.blit(titleTextBG, (235, j - 490 + 3))
            screen.blit(titleText, (235, j - 490))
            
            if introDone:
                pydraw.box(screen, ((385,295),(510,210)), gray)
                pydraw.box(screen, ((390,300),(500,200)), lightGray)
                screen.blit(startGameText, (415,330))
                

            py.display.flip()
            clock.tick(60)
            for event in py.event.get():
                mouse = py.mouse.get_pos()
                if event.type == py.QUIT:
                    introRunning = False
                    running = False
                if event.type == py.MOUSEBUTTONDOWN:
                    if ((mouse[0] >= 385 and mouse[0] <= 895) and (mouse[1] >= 295 and mouse[1] <= 505)):
                        introRunning = False
                        state = States.transition

    if state == States.transition:
        transitioning = True
        j = 0
        while transitioning:
            for event in py.event.get():
                if event.type == py.QUIT:
                    running  = False
                    transitioning = False

            if j < 1500:
                j = j + 5
            else:
                transitioning = False
                state = States.mainGame
            
            pydraw.box(screen, ((-2000 + j, 0),(2000,2000)), (0,0,0))
            pydraw.box(screen, ((1280 - j, 0),(2000,2000)), (0,0,0))
            pydraw.box(screen, ((0, 720 - j),(2000,2000)), (0,0,0))
            pydraw.box(screen, ((0, -2000 + j),(2000,2000)), (0,0,0))

            py.display.flip()
            clock.tick(60)

            for event in py.event.get():
                if event.type == py.QUIT:
                    running = False

    if state == States.mainGame:
        gameRunning = True
        j = 0
        while gameRunning:
            j = j + 2.5
            pydraw.box(screen, ((0,0),(1280,720)), grassGreen)

            pydraw.box(screen, ((-10, 100), (300, 80)), grayRoad)
            pydraw.box(screen, ((290, 100), (80, 300)), grayRoad)
            pydraw.box(screen, ((290, 400), (500, 80)), grayRoad)
            pydraw.box(screen, ((790, 100), (80, 380)), grayRoad)
            pydraw.box(screen, ((790, 100), (450, 80)), grayRoad)
            pydraw.box(screen, ((1160, 100), (80, 500)), grayRoad)
            pydraw.box(screen, ((90, 600), (1150, 80)), grayRoad)
            pydraw.box(screen, ((90, 600), (80, 300)), grayRoad)

            pydraw.box(screen, ((880, 190), (270, 400)), oceanBlue)

            pydraw.box(screen, ((0,0),(1280, 95)), (0,0,0))

            pydraw.box(screen, ((0, 0),(1280, 90)), darkWood)

            for i in range(0,20):
                pydraw.box(screen, ((80 * i, 0),(40, 90)), woodBrown)

            pydraw.box(screen, ((-360 - j,-640 - j),(1000,1000)), (0,0,0))
            pydraw.box(screen, ((640 + j ,-640 - j),(1000,1000)), (0,0,0))
            pydraw.box(screen, ((-360 - j,360 + j),(1000,1000)), (0,0,0))
            pydraw.box(screen, ((640 + j,360 + j),(1000,1000)), (0,0,0))

            py.display.flip()
            clock.tick(60)
            
            for event in py.event.get():
                if event.type == py.QUIT:
                    running = False
                    gameRunning = False

    for event in py.event.get():
        if event.type == py.QUIT:
            running = False

    py.display.flip()
    clock.tick(60)

py.quit()