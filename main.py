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
redCharge = (201, 0, 0)
orangeCharge = (255, 72, 0)
blueCharge = (0, 117, 227)
greenCharge = (0, 227, 45)
robotGray = (200,200,200)

class States(Enum):
    mainMenu = 1
    transition = 2
    mainGame = 3

state = States.mainMenu
clock = py.time.Clock()
gameLives = 100

skyBG = py.Rect(0, 0, 1280, 720)
running = True

titleFont = py.font.SysFont("Trebuchet MS", 150)
titleText = titleFont.render("Bot Defense", True, (255,255,0))
titleTextBG = titleFont.render("Bot Defense", True, (200,200,0))

subTitleFont = py.font.SysFont("Tahoma", 90)
startGameText = subTitleFont.render("Start Game", True, (255,255,255))

class robot(py.sprite.Sprite):
    def __init__(self, color, BFR):
        super().__init__()
        self.robotMoves = ((-100, 102), (290, 102), (290, 400), (790, 400), (790, 102), (1160, 102), (1160, 600), (90, 600), (90, 900))
        self.image = py.Surface((76,76))
        self.charge = color

        self.moveNum = 1

        if self.charge == "r":
            if BFR:
                self.HP = 20
            else:
                self.HP = 2
            self.outline = redCharge
            self.speed = 50
        elif self.charge == "o":
            if BFR:
                self.HP = 40
            else:
                self.HP = 5
            self.outline = orangeCharge
            self.speed = 65
        elif self.charge == "b":
            if BFR:
                self.HP = 60
            else:
                self.HP = 10
            self.outline = blueCharge
            self.speed = 80
        elif self.charge == "g":
            if BFR:
                self.HP = 80
            else:
                self.HP = 15
            self.outline = greenCharge
            self.speed = 100

        pydraw.box(self.image, ((0,0), (76,76)), grayRoad)
        pydraw.filled_circle(self.image, 38, 38, 30, robotGray)
        pydraw.filled_circle(self.image, 30, 21, 4, self.outline)
        pydraw.filled_circle(self.image, 30, 55, 4, self.outline)
        pydraw.box(self.image, ((46,18),(4,40)), self.outline)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.robotMoves[0][0]
        self.rect.y = self.robotMoves[0][1]

    def update(self):
        if self.moveNum < self.robotMoves.__len__():
            if self.rect.x < self.robotMoves[self.moveNum][0]:
                self.rect.x += 2 * (self.speed)/100
            elif self.rect.x > self.robotMoves[self.moveNum][0]:
                self.rect.x -= 2 * (self.speed)/100
            
            if self.rect.y < self.robotMoves[self.moveNum][1]:
                self.rect.y += 2 * (self.speed)/100
            elif self.rect.y > self.robotMoves[self.moveNum][1]:
                self.rect.y -= 2 * (self.speed)/100

            if self.rect.x == self.robotMoves[self.moveNum][0] and self.rect.y == self.robotMoves[self.moveNum][1]:
                self.moveNum += 1
                
            for event in py.event.get():
                if event.type == py.QUIT:
                    py.quit()
        else:
            self.kill()



    
        

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
        spriteList = py.sprite.Group()
        test = robot("r", False)
        test2 = robot("g", False)
        spriteList.add(test)
        spriteList.add(test2)
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

            spriteList.update()
            spriteList.draw(screen)

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