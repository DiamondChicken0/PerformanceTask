import pygame as py
import pygame.gfxdraw as pydraw
import pygame.pixelarray as px
import random as rng
from enum import Enum
import math
import random
py.init()
py.font.init()
random.seed()

size = (1280, 720)
screen = py.display.set_mode(size)
py.display.set_caption("Cool Game")
spriteList = py.sprite.Group()

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
rinserTone = (255,204,153)
rinserHair = (253, 193, 0)
black = (0,0,0)
white = (255,255,255)

class States(Enum):
    mainMenu = 1
    transition = 2
    mainGame = 3

state = States.mainGame
clock = py.time.Clock()
skyBG = py.Rect(0, 0, 1280, 720)
running = True

titleFont = py.font.SysFont("Trebuchet MS", 150)
titleText = titleFont.render("Bot Defense", True, (255,255,0))
titleTextBG = titleFont.render("Bot Defense", True, (200,200,0))

hudFont = py.font.SysFont("Gill Sans MT", 90)

heartHUD = py.Surface((7,7))
heartPixelArray = py.PixelArray(heartHUD)
for i in range(0,49):
    heartPixelArray[int(i/7), i%7] = (255, 43, 43)
heartPixelArray [0,0] = (43, 170, 255)
heartPixelArray [3,0] = (43, 170, 255)
heartPixelArray [6,0] = (43, 170, 255)
heartPixelArray [0,4] = (43, 170, 255)
heartPixelArray [6,4] = (43, 170, 255)
heartPixelArray [0,5] = (43, 170, 255)
heartPixelArray [1,5] = (43, 170, 255)
heartPixelArray [5,5] = (43, 170, 255)
heartPixelArray [6,5] = (43, 170, 255)
heartPixelArray [0,6] = (43, 170, 255)
heartPixelArray [1,6] = (43, 170, 255)
heartPixelArray [2,6] = (43, 170, 255)
heartPixelArray [4,6] = (43, 170, 255)
heartPixelArray [5,6] = (43, 170, 255)
heartPixelArray [6,6] = (43, 170, 255)
heartPixelArray.close()

heartHUD = py.transform.scale(heartHUD, (77, 77))
heartHUD.set_colorkey((43, 170, 255))
heartHUD.unlock()

coinHUD = py.Surface((7,7))
coinPixelArray = py.PixelArray(coinHUD)
for i in range(0,49):
    coinPixelArray[int(i/7), i%7] = (255, 243, 0)
coinPixelArray [3,1] = (161, 154, 0)
coinPixelArray [2,2] = (161, 154, 0)
coinPixelArray [3,2] = (161, 154, 0)
coinPixelArray [4,2] = (161, 154, 0)
coinPixelArray [2,3] = (161, 154, 0)
coinPixelArray [2,4] = (161, 154, 0)
coinPixelArray [3,4] = (161, 154, 0)
coinPixelArray [4,4] = (161, 154, 0)
coinPixelArray [3,5] = (161, 154, 0)
coinPixelArray [0,0] = (43, 170, 255)
coinPixelArray [0,1] = (43, 170, 255)
coinPixelArray [1,0] = (43, 170, 255)
coinPixelArray [5,0] = (43, 170, 255)
coinPixelArray [6,1] = (43, 170, 255)
coinPixelArray [6,0] = (43, 170, 255)
coinPixelArray [0,5] = (43, 170, 255)
coinPixelArray [0,6] = (43, 170, 255)
coinPixelArray [1,6] = (43, 170, 255)
coinPixelArray [5,6] = (43, 170, 255)
coinPixelArray [6,6] = (43, 170, 255)
coinPixelArray [6,5] = (43, 170, 255)
coinPixelArray.close()

coinHUD = py.transform.scale(coinHUD, (77, 77))
coinHUD.set_colorkey((43, 170, 255))
coinHUD.unlock()

waterHUD = py.Surface((7,7))
waterPixelArray = py.PixelArray(waterHUD)
for i in range(0,49):
    waterPixelArray[int(i/7), i%7] = (99,155,255)
waterPixelArray [4,4] = white
waterPixelArray [0,0] = ((43, 170, 255))
waterPixelArray [1,0] = ((43, 170, 255))
waterPixelArray [2,0] = ((43, 170, 255))
waterPixelArray [4,0] = ((43, 170, 255))
waterPixelArray [5,0] = ((43, 170, 255))
waterPixelArray [6,0] = ((43, 170, 255))
waterPixelArray [0,1] = ((43, 170, 255))
waterPixelArray [1,1] = ((43, 170, 255))
waterPixelArray [5,1] = ((43, 170, 255))
waterPixelArray [6,1] = ((43, 170, 255))
waterPixelArray [0,2] = ((43, 170, 255))
waterPixelArray [6,2] = ((43, 170, 255))
waterPixelArray [0,3] = ((43, 170, 255))
waterPixelArray [6,3] = ((43, 170, 255))
waterPixelArray [0,4] = ((43, 170, 255))
waterPixelArray [6,4] = ((43, 170, 255))
waterPixelArray [0,5] = ((43, 170, 255))
waterPixelArray [6,5] = ((43, 170, 255))
waterPixelArray [0,6] = ((43, 170, 255))
waterPixelArray [1,6] = ((43, 170, 255))
waterPixelArray [5,6] = ((43, 170, 255))
waterPixelArray [6,6] = ((43, 170, 255))

waterPixelArray.close()

waterHUD = py.transform.scale(waterHUD, (77, 77))
waterHUD.set_colorkey((43, 170, 255))
waterHUD.unlock()

subTitleFont = py.font.SysFont("Tahoma", 90)
startGameText = subTitleFont.render("Start Game", True, white)

class lives():
    def __init__(self):
        self.gameLives = 100
        self.gameLivesText = hudFont.render(str(self.gameLives), True, white)

    def change(self, amount):
        self.gameLives += amount
        self.gameLivesText = hudFont.render(str(self.gameLives), True, white)

    def get(self):
        return self.gameLives
    
    def getText(self):
        return self.gameLivesText
    
class water():
    def __init__(self):
        self.water = 9999
        self.waterText = hudFont.render(str(self.water), True, white)

    def change(self, amount):
        self.water += amount
        self.waterText = hudFont.render(str(self.water), True, white)

    def get(self):
        return self.water

    def getText(self):
        return self.waterText
    
class money():
    def __init__(self):
        self.money = 99999
        self.moneyText = hudFont.render(str(self.money), True, white)

    def change(self, amount):
        self.money += amount 
        self.moneyText = hudFont.render(str(self.money), True, white)

    def get(self):
        return self.money

    def getText(self):
        return self.moneyText
    
currentLives = lives()
waterSupply = water()
currentMoney = money()

class weather():
    def __init__(self):
        self.freq = 1
        self.sev = 1
        self.weather = [0,0,1,0,0,0,1]

    def generateNext(self):
        self.weather.pop(6)
    
class rinser(py.sprite.Sprite):
    def __init__(self, pos):
        upgrades = black
        super().__init__()
        self.image = py.Surface((100,100))
        self.rect = self.image.get_rect()
        self.range = py.surface
        #self.rect.coll
        
        pydraw.box(self.image, ((-2,-2), (104,104)), black)
        pydraw.filled_circle(self.image, 50, 50, 44, black)
        pydraw.filled_circle(self.image, 30, 40, 14, black)
        pydraw.filled_circle(self.image, 70, 40, 14, black)
        pydraw.filled_circle(self.image, 70, 40, 8, black)
        pydraw.filled_circle(self.image, 30, 40, 8, black)

        pydraw.box(self.image, ((0,0), (100,100)), (107, 112, 0))
        pydraw.filled_circle(self.image, 50, 50, 40, rinserTone)
        pydraw.filled_circle(self.image, 30, 40, 10, white)
        pydraw.filled_circle(self.image, 70, 40, 10, white)
        pydraw.filled_circle(self.image, 70, 40, 4, (0, 169, 223))
        pydraw.filled_circle(self.image, 30, 40, 4, (0, 169, 223))

        for i in range(0,20):
            pydraw.filled_trigon(self.image, random.randint(5,95),random.randint(5,30),random.randint(5,95),random.randint(5,30),random.randint(5,95),random.randint(5,30), rinserHair)
        pydraw.bezier(self.image, [(25,70),(50,85),(75,70)], 100, black)
        pydraw.bezier(self.image, [(25,71),(50,86),(75,71)], 100, black)
        pydraw.bezier(self.image, [(25,72),(50,87),(75,72)], 100, black)
        pydraw.line(self.image, 45,60,55,60, black)
        pydraw.line(self.image, 45,61,55,61, black)
        pydraw.line(self.image, 45,62,55,62, black)
        pydraw.line(self.image, 50,50,55,60, black)
        pydraw.line(self.image, 50,51,55,60, black)
        pydraw.line(self.image, 50,52,55,60, black)
        pydraw.box(self.image,(0,40,10,30), (249, 171, 27))
        pydraw.filled_trigon(self.image,0,70,5,75,10,70,(255, 116, 0))
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.image.set_colorkey((107, 112, 0))
        self.pixArray = py.surfarray.pixels2d(self.image)
        self.pixArray.flatten()
        self.pixArray[0,0] = (0,0,0)
        self.pixArray[0,1] = black
        self.pixArray[1,1] = black
        self.pixArray[2,2] = black
        self.pixArray[2,1] = black
        self.pixArray[1,3] = black

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
        self.storedAngle = 90

    def update(self):
        self.storedAngle = self.storedAngle % 360
        if self.moveNum < self.robotMoves.__len__():
            if self.rect.x < self.robotMoves[self.moveNum][0]:
                self.rect.x += 2 * (self.speed)/100
                if self.storedAngle != 90:
                    self.image = py.transform.rotate(self.image, 90)
                    self.storedAngle += 90
            elif self.rect.x > self.robotMoves[self.moveNum][0]:
                self.rect.x -= 2 * (self.speed)/100
                if self.storedAngle != 270:
                    self.image = py.transform.rotate(self.image, 90)
                    self.storedAngle += 90
            if self.rect.y < self.robotMoves[self.moveNum][1]:
                self.rect.y += 2 * (self.speed)/100
                if self.storedAngle != 0:
                    self.image = py.transform.rotate(self.image, 90)
                    self.storedAngle += 90
            elif self.rect.y > self.robotMoves[self.moveNum][1]:
                self.rect.y -= 2 * (self.speed)/100
                if self.storedAngle != 180:
                    self.image = py.transform.rotate(self.image, 90)
                    self.storedAngle += 90

            if self.rect.x == self.robotMoves[self.moveNum][0] and self.rect.y == self.robotMoves[self.moveNum][1]:
                self.moveNum += 1
                
        else:
            currentLives.change(self.HP * -1)
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
            
            pydraw.box(screen, ((190, j - 530), (900,520)), black)
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
            
            pydraw.box(screen, ((-2000 + j, 0),(2000,2000)), black)
            pydraw.box(screen, ((1280 - j, 0),(2000,2000)), black)
            pydraw.box(screen, ((0, 720 - j),(2000,2000)), black)
            pydraw.box(screen, ((0, -2000 + j),(2000,2000)), black)

            py.display.flip()
            clock.tick(60)

            for event in py.event.get():
                if event.type == py.QUIT:
                    running = False

    if state == States.mainGame:
        gameRunning = True
        j = 0
        test = robot("r", False)
        test2 = robot("g", False)
        spriteList.add(test)
        spriteList.add(test2)
        test3 = rinser((200,200))
        spriteList.add(test3)
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

            pydraw.box(screen, ((0,0),(1280, 95)), black)

            pydraw.box(screen, ((0, 0),(1280, 90)), darkWood)

            for i in range(0,20):
                pydraw.box(screen, ((80 * i, 0),(40, 90)), woodBrown)

            screen.blit(currentLives.getText(),(100,15))
            screen.blit(currentMoney.getText(),(310,15))
            screen.blit(waterSupply.getText(),(570,15))
            screen.blit(heartHUD, (15,10))
            screen.blit(coinHUD, (220,8))
            screen.blit(waterHUD, (495,5))

            pydraw.box(screen, ((-360 - j,-640 - j),(1000,1000)), black)
            pydraw.box(screen, ((640 + j ,-640 - j),(1000,1000)), black)
            pydraw.box(screen, ((-360 - j,360 + j),(1000,1000)), black)
            pydraw.box(screen, ((640 + j,360 + j),(1000,1000)), black)

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