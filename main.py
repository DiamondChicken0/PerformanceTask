import pygame as py
import pygame.gfxdraw as pydraw
import pygame.pixelarray
import random
from enum import Enum
import math
import random
import threading
import numpy
py.init()
py.font.init()
random.seed()

size = (1280, 720)
screen = py.display.set_mode(size)
py.display.set_caption("Bot Defense")
spriteList = py.sprite.Group()
towerList = py.sprite.Group()
robotList = py.sprite.Group()
tempList = py.sprite.Group()
unplaceableScreen = py.Surface((1280,720))
unplaceableScreen.fill((0,0,0))
waterScreen = py.Surface((1280,720))
waterScreen.fill((0,0,0))

#colors
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
rinserHair = (150,74,2)
black = (0,0,0)
white = (255,255,255)

class States(Enum):
    mainMenu = 1
    transition = 2
    mainGame = 3
    victory = 4

state = States.mainGame
clock = py.time.Clock()
skyBG = py.Rect(0, 0, 1280, 720)
running = True

titleFont = py.font.SysFont("Trebuchet MS", 150)
titleText = titleFont.render("Bot Defense", True, (255,255,0))
titleTextBG = titleFont.render("Bot Defense", True, (200,200,0))

hudFont = py.font.SysFont("Gill Sans MT", 90)

#Creating hud elements
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

towerFont = py.font.SysFont("Bahnschrift", 30)

rinserText = towerFont.render("Rinser", True, black)
fountainText = towerFont.render("Fountain", True, black)
shipText = towerFont.render("SS Soaker", True, black)
snorklerText = towerFont.render("Snorkler", True, black)
wellText = towerFont.render("Well", True, black)
waterCollectorText1 = towerFont.render("Rain", True, black)
waterCollectorText2 = towerFont.render("Barrel", True, black)
waterPumpText1 = towerFont.render("Water", True, black)
waterPumpText2 = towerFont.render("Pump", True, black)

selectedTower = None

def makeRadiusMask(pos, r):
    rMaskScreen = py.Surface((1280,720))
    rMaskScreen.fill((0,0,0))
    pydraw.filled_circle(rMaskScreen, pos[0], pos[1], r, (255,255,255))
    rMaskScreen.set_colorkey((0,0,0))
    rMask = py.mask.from_surface(rMaskScreen)

    return rMask
#Keeps track of lives
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
    
#Outlines surfaces using a key(background color)
def outline(surf, key, size):
    pixArray = py.surfarray.array3d(surf)
    #loop through everything
    for y in range(surf.get_width()):
        for x in range(surf.get_height()):
            #check if pixel is background or foreground
            if pixArray[x,y,0] != key[0] and pixArray[x,y,1] != key[1] and pixArray[x,y,2] != key[2]:
                for j in range(size):
                    if x - j >= 0:
                        if pixArray[x-j,y,0] == key[0] and pixArray[x-j,y,1] == key[1] and pixArray[x-j,y,2] == key[2]:
                            pixArray[x-j,y,0] = 0
                            pixArray[x-j,y,1] = 0
                            pixArray[x-j,y,2] = 0
                    if x + j < surf.get_width():
                        if pixArray[x+j,y,0] == key[0] and pixArray[x+j,y,1] == key[1] and pixArray[x+j,y,2] == key[2]:
                            pixArray[x+j,y,0] = 0
                            pixArray[x+j,y,1] = 0
                            pixArray[x+j,y,2] = 0
                    if y - j >= 0:
                        if pixArray[x,y-j,0] == key[0] and pixArray[x,y-j,1] == key[1] and pixArray[x,y-j,2] == key[2]:
                            pixArray[x,y-j,0] = 0
                            pixArray[x,y-j,1] = 0
                            pixArray[x,y-j,2] = 0 
                    if y + j < surf.get_height():
                        if pixArray[x,y+j,0] == key[0] and pixArray[x,y+j,1] == key[1] and pixArray[x,y+j,2] == key[2]:
                            pixArray[x,y+j,0] = 0
                            pixArray[x,y+j,1] = 0
                            pixArray[x,y+j,2] = 0

    surf = py.surfarray.make_surface(pixArray)
    return surf

#keeps track of water
class water():
    def __init__(self):
        self.water = 500
        self.waterText = hudFont.render(str(self.water), True, white)

    def change(self, amount):
        if self.water + amount >= 0:
            self.water += amount
            self.waterText = hudFont.render(str(self.water), True, white)
            return True
        return False

    def get(self):
        return self.water

    def getText(self):
        return self.waterText
    
#keeps track of money 
class money():
    def __init__(self):
        self.money = 1000
        self.moneyText = hudFont.render(str(self.money), True, white)

    def change(self, amount):
        if self.money + amount >= 0:
            self.money += amount 
            self.moneyText = hudFont.render(str(self.money), True, white)
            return True
        return False
        

    def get(self):
        return self.money

    def getText(self):
        return self.moneyText
    
currentLives = lives()
waterSupply = water()
currentMoney = money()

#The robot increases its speed and HP with energy
#indicated by the color of the robot: Green > Blue > Orange > Red
class robot(py.sprite.Sprite):
    def __init__(self, color):
        super().__init__()
        self.robotMoves = ((-100, 102), (290, 102), (290, 400), (790, 400), (790, 102), (1160, 102), (1160, 490), (90, 490), (90, 700))
        self.image = py.Surface((76,76))
        self.charge = color

        self.moveNum = 1

        if self.charge == "r":
                self.HP = 2
                self.outline = redCharge
                self.speed = 1
        elif self.charge == "o":
                self.HP = 5
                self.outline = orangeCharge
                self.speed = 2
        elif self.charge == "b":
                self.HP = 10
                self.outline = blueCharge
                self.speed = 3
        elif self.charge == "g":
                self.HP = 15
                self.outline = greenCharge
                self.speed = 4

        pydraw.box(self.image, ((0,0), (76,76)), grayRoad)
        pydraw.filled_circle(self.image, 38, 38, 34, black)
        pydraw.filled_circle(self.image, 38, 38, 30, robotGray)
        pydraw.filled_circle(self.image, 30, 21, 4, self.outline)
        pydraw.filled_circle(self.image, 30, 55, 4, self.outline)
        pydraw.box(self.image, ((46,18),(4,40)), self.outline)
        self.image.set_colorkey(grayRoad)
        self.rect = self.image.get_rect()
        self.rect.x = self.robotMoves[0][0]
        self.rect.y = self.robotMoves[0][1]
        self.storedAngle = 90

    def update(self):

        self.storedAngle = self.storedAngle % 360
        if self.moveNum < self.robotMoves.__len__():
            if self.rect.x < self.robotMoves[self.moveNum][0]:
                self.rect.x += self.speed
                if self.storedAngle != 90:
                    self.image = py.transform.rotate(self.image, 90)
                    self.storedAngle = 90
            elif self.rect.x > self.robotMoves[self.moveNum][0]:
                self.rect.x -= self.speed
                if self.storedAngle != 270:
                    self.image = py.transform.rotate(self.image, 90)
                    self.storedAngle = 270
            if self.rect.y < self.robotMoves[self.moveNum][1]:
                self.rect.y += self.speed
                if self.storedAngle != 0:
                    self.image = py.transform.rotate(self.image, 90)
                    self.storedAngle = 0
            elif self.rect.y > self.robotMoves[self.moveNum][1]:
                self.rect.y -= self.speed
                if self.storedAngle != 180:
                    self.image = py.transform.rotate(self.image, 90)
                    self.storedAngle = 180
            
            #I cant be bothered making this airtight, its close enough
            if abs(self.rect.x - self.robotMoves[self.moveNum][0]  + self.rect.y - self.robotMoves[self.moveNum][1]) < 5:
                self.rect.x = self.robotMoves[self.moveNum][0]
                self.rect.y = self.robotMoves[self.moveNum][1]
                self.moveNum += 1
                
        else:
            currentLives.change(self.HP * -1)
            self.kill()
    
    def getPos(self):
        return (self.rect.x, self.rect.y)
    
    def damage(self, dmg):
        self.HP -= dmg
        if self.HP <= 0:
            self.kill()
        elif self.HP <= 2:
            self.charge = "r"
            self.outline = redCharge
            self.speed = 1
        elif self.HP <= 5:
            self.charge = "o"
            self.outline = orangeCharge
            self.speed = 2
        elif self.HP <= 10:
            self.charge = "b"
            self.outline = blueCharge
            self.speed = 3
        
        pydraw.box(self.image, ((0,0), (76,76)), grayRoad)
        pydraw.filled_circle(self.image, 38, 38, 34, black)
        pydraw.filled_circle(self.image, 38, 38, 30, robotGray)
        pydraw.filled_circle(self.image, 30, 21, 4, self.outline)
        pydraw.filled_circle(self.image, 30, 55, 4, self.outline)
        pydraw.box(self.image, ((46,18),(4,40)), self.outline)

        self.image = py.transform.rotate(self.image, self.storedAngle - 90)

        


def towerTarget(mask, offset):
    index = -1
    for x in robotList:
        index += 1
        try:
            if mask.get_at((x.getPos()[0] - offset, (x.getPos()[1]) - offset)) == 1:
                return((x.getPos()), index)
        except:
            pass
    return None

def makeDottedLine(startx, starty, endx, endy):
    tempScreen = py.Surface((1280,720))
    tempScreen.fill((255,255,255))
    pydraw.line(tempScreen, startx, starty, endx, endy, oceanBlue)
    pydraw.line(tempScreen, startx, starty+1, endx-1, endy, oceanBlue)
    pydraw.line(tempScreen, startx+1, starty, endx, endy-1, oceanBlue)
    pydraw.line(tempScreen, startx+2, starty, endx, endy-2, oceanBlue)
    pydraw.line(tempScreen, startx, starty+2, endx-2, endy, oceanBlue)
    tempPix = py.PixelArray(tempScreen)
    for x in range(0,endx,30):
        for y in range(0,endy):
            if tempPix[x][y] == oceanBlue:
                tempPix[x-1:x][y-1:y-2] == (255,255,255)
                tempPix[x+1:x][y-3:y-2] == (255,255,255)
    tempPix.close()
    tempScreen.set_colorkey((255,255,255))
    tempScreen.unlock()
    screen.unlock()
    screen.blit(tempScreen, (0,0))
    return tempScreen


#This is the starting tower of the game
class rinser(py.sprite.Sprite):
    def __init__(self, pos, selected):

        #Declaration stuff
        super().__init__()
        self.image = py.Surface((100,100))
        self.rect = self.image.get_rect()
        self.selected = selected
        self.placedDown = False
        self.storedAngle = 0 #Looking Down
        self.lowTime = py.time.get_ticks()
        
        #Body
        pydraw.box(self.image, ((-2,-2), (104,104)), black)
        pydraw.filled_circle(self.image, 50, 50, 44, black)
        pydraw.filled_circle(self.image, 30, 40, 14, black)
        pydraw.filled_circle(self.image, 70, 40, 14, black)
        pydraw.filled_circle(self.image, 70, 40, 8, black)
        pydraw.filled_circle(self.image, 30, 40, 8, black)
        pydraw.box(self.image, ((0,0), (100,100)), (107, 112, 0))
        pydraw.filled_circle(self.image, 50, 50, 40, rinserTone)

        pydraw.box(self.image,(5,40,10,30), (249, 171, 27))
        pydraw.filled_trigon(self.image,5,70,10,75,15,70,(255, 116, 67))
        pydraw.filled_polygon(self.image,[(6,70),(7,85),(25,85),(40,87),(54,79),(67,86),(80,78),(98,85),(90,78),(97,57),(90,36),(96,6),(80,20),(57,6),(40,10),(19,7),(6,30),(14,40),(5,49),(14,61)], rinserHair)
        
        self.rect.x = pos[0]
        self.rect.y = pos[1]

        self.image = outline(self.image, (107, 112, 0), 6)
        self.image.set_colorkey((107,112,0))

        self.original = self.image.copy()
        self.image.set_alpha(75)

    def update(self):
        if not self.placedDown:
            if self.selected: 
                self.rect.x = py.mouse.get_pos()[0]
                self.rect.y = py.mouse.get_pos()[1]
            else:
                try:
                    if (unplaceableMask.get_at((self.rect.x, self.rect.y)) == 0 and unplaceableMask.get_at((self.rect.x + 100, self.rect.y)) == 0 and unplaceableMask.get_at((self.rect.x, self.rect.y + 100)) == 0 and unplaceableMask.get_at((self.rect.x + 100, self.rect.y + 100)) == 0 and unplaceableMask.get_at((self.rect.x + 50, self.rect.y + 50)) == 0) and (waterMask.get_at((self.rect.x, self.rect.y)) == 0 and waterMask.get_at((self.rect.x + 100, self.rect.y)) == 0 and waterMask.get_at((self.rect.x, self.rect.y + 100)) == 0 and waterMask.get_at((self.rect.x + 100, self.rect.y + 100)) == 0 and waterMask.get_at((self.rect.x + 50, self.rect.y + 50)) == 0):
                        if currentMoney.change(-500) == True:
                            self.placedDown = True
                            self.image.set_alpha(255)
                        else:
                            self.kill()
                    else:
                        self.kill()
                except:
                    pass
        else:
            self.mask = makeRadiusMask((self.rect.x, self.rect.y), 200)
            if self.lowTime <= py.time.get_ticks() - 1000:
                if towerTarget(self.mask,50) != None and waterSupply.change(-1):
                    self.lowTime = py.time.get_ticks()
                    self.targetPoint = towerTarget(self.mask,50)
                    self.newAngle = math.degrees(math.atan2((self.targetPoint[0][0] - self.rect.x) * -1, self.targetPoint[0][1] - self.rect.y) % (2 * math.pi))
                    robotList.sprites()[self.targetPoint[1]].damage(2)
                    waterLine = makeDottedLine(self.rect.x + 50, self.rect.y + 50, self.targetPoint[0][0]+38, self.targetPoint[0][1]+38)
                    screen.blit(waterLine,(0,0))
                    if abs(self.newAngle - self.storedAngle) > 1:
                        self.image = py.transform.rotate(self.original, int((self.newAngle - self.storedAngle) * -1))
    def unselect(self):
        self.selected = False


class fountain(py.sprite.Sprite):
    def __init__(self, pos, selected):

        #Declaration stuff
        super().__init__()
        self.image = py.Surface((100,100))
        self.rect = self.image.get_rect()
        self.image.fill((107,112,0))
        self.lowTime = py.time.get_ticks()
        self.selected = selected
        self.placedDown = False
        pydraw.filled_ellipse(self.image, 50, 25, 40, 15, (102,178, 255))
        pydraw.filled_ellipse(self.image, 50, 75, 40, 15, (102,178, 255))
        pydraw.box(self.image, ((9,25), (82,50)), (102,178, 255))
        pydraw.ellipse(self.image, 50, 24, 40, 15, black)
        pydraw.ellipse(self.image, 50, 25, 40, 15, black)
        pydraw.ellipse(self.image, 50, 26, 40, 15, black)
        pydraw.filled_ellipse(self.image, 50, 25, 30, 10, black)
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.image = outline(self.image, (107,112,0), 6)
        self.image.set_colorkey((107,112,0))
        self.image.set_alpha(75)

    def update(self):
        print(self.selected)
        if not self.placedDown:
            if self.selected: 
                self.rect.x = py.mouse.get_pos()[0]
                self.rect.y = py.mouse.get_pos()[1]
            else:
                try:
                    print("trying")
                    if (unplaceableMask.get_at((self.rect.x, self.rect.y)) == 0 and unplaceableMask.get_at((self.rect.x + 100, self.rect.y)) == 0 and unplaceableMask.get_at((self.rect.x, self.rect.y + 100)) == 0 and unplaceableMask.get_at((self.rect.x + 100, self.rect.y + 100)) == 0 and unplaceableMask.get_at((self.rect.x + 50, self.rect.y + 50)) == 0) and (waterMask.get_at((self.rect.x, self.rect.y)) == 0 and waterMask.get_at((self.rect.x + 100, self.rect.y)) == 0 and waterMask.get_at((self.rect.x, self.rect.y + 100)) == 0 and waterMask.get_at((self.rect.x + 100, self.rect.y + 100)) == 0 and waterMask.get_at((self.rect.x + 50, self.rect.y + 50)) == 0):
                        print("really")
                        if currentMoney.change(-300) == True:
                            self.placedDown = True
                            self.image.set_alpha(255)
                            print("it got placed")
                        else:
                            print("killed 1")
                            self.kill()
                    else:
                        print("killed 2")
                        self.kill()
                except:
                    print("excepted")
        else:
            if gamelogic.isSending() == True and self.lowTime <= py.time.get_ticks() - 10000:
                waterSupply.change(20)
                self.lowTime = py.time.get_ticks()
                
    def unselect(self):
        self.selected = False


class ship(py.sprite.Sprite):
    def __init__(self, pos, selected):

        #Declaration stuff
        super().__init__()
        self.image = py.Surface((100,100))
        self.rect = self.image.get_rect()
        self.selected = selected
        self.placedDown = False
        self.storedAngle = 0 #Looking Down
        self.lowTime = py.time.get_ticks()
        self.image.fill((107,112,0))
        
        pydraw.box(self.image, ((25,25), (50,50)), (175,122,0))
        pydraw.filled_trigon(self.image,25,25,75,25,50,10, (175,122,0))
        pydraw.box(self.image, ((10,60),(15,5)), (255,193,7))
        pydraw.box(self.image, ((75,60),(15,5)), (255,193,7))


        self.rect.x = pos[0]
        self.rect.y = pos[1]

        self.image = outline(self.image, (107, 112, 0), 6)
        self.image.set_colorkey((107,112,0))

        self.original = self.image.copy()
        self.image.set_alpha(75)

    def update(self):
        if not self.placedDown:
            if self.selected: 
                self.rect.x = py.mouse.get_pos()[0]
                self.rect.y = py.mouse.get_pos()[1]
            else:
                try:
                    if (unplaceableMask.get_at((self.rect.x, self.rect.y)) == 0 and unplaceableMask.get_at((self.rect.x + 100, self.rect.y)) == 0 and unplaceableMask.get_at((self.rect.x, self.rect.y + 100)) == 0 and unplaceableMask.get_at((self.rect.x + 100, self.rect.y + 100)) == 0 and unplaceableMask.get_at((self.rect.x + 50, self.rect.y + 50)) == 0) and (waterMask.get_at((self.rect.x, self.rect.y)) == 0 and waterMask.get_at((self.rect.x + 100, self.rect.y)) == 0 and waterMask.get_at((self.rect.x, self.rect.y + 100)) == 0 and waterMask.get_at((self.rect.x + 100, self.rect.y + 100)) == 0 and waterMask.get_at((self.rect.x + 50, self.rect.y + 50)) == 0):
                        if currentMoney.change(-1200) == True:
                            self.placedDown = True
                            self.image.set_alpha(255)
                        else:
                            self.kill()
                    else:
                        self.kill()
                except:
                    pass
        else:
            self.mask = makeRadiusMask((self.rect.x, self.rect.y), 500)
            if self.lowTime <= py.time.get_ticks() - 1000:
                if towerTarget(self.mask,50) != None and waterSupply.change(-1):
                    self.lowTime = py.time.get_ticks()
                    self.targetPoint = towerTarget(self.mask,50)
                    self.newAngle = math.degrees(math.atan2((self.targetPoint[0][0] - self.rect.x) * -1, self.targetPoint[0][1] - self.rect.y) % (2 * math.pi))
                    robotList.sprites()[self.targetPoint[1]].damage(5)
                    waterLine = makeDottedLine(self.rect.x + 50, self.rect.y + 50, self.targetPoint[0][0]+38, self.targetPoint[0][1]+38)
                    screen.blit(waterLine,(0,0))
                    if abs(self.newAngle - self.storedAngle) > 1:
                        self.image = py.transform.rotate(self.original, int((self.newAngle - self.storedAngle) * -1))
    def unselect(self):
        self.selected = False

class snorkler(py.sprite.Sprite):
    def __init__(self, pos):

        #Declaration stuff
        super().__init__()
        self.image = py.Surface((100,100))
        self.rect = self.image.get_rect()

class well(py.sprite.Sprite):
    def __init__(self, pos):

        #Declaration stuff
        super().__init__()
        self.image = py.Surface((100,100))
        self.rect = self.image.get_rect()

class collector(py.sprite.Sprite):
    def __init__(self, pos):

        #Declaration stuff
        super().__init__()
        self.image = py.Surface((100,100))
        self.rect = self.image.get_rect()

class pump(py.sprite.Sprite):
    def __init__(self, pos):

        #Declaration stuff
        super().__init__()
        self.image = py.Surface((100,100))
        self.rect = self.image.get_rect()


class roundManager():
    def __init__(self):
        self.round = 1
        self.waves = ((5,0,0,0,.5), (10,0,0,0,1))
        self.sending = False
    
    def startNextRound(self):
        self.lowTime = py.time.get_ticks()
        if round == 30:
            return States.victory
        else:
            self.sending = True
            self.robotR = self.waves[(self.round-1)][0]
            self.robotO = self.waves[(self.round-1)][1]
            self.robotB = self.waves[(self.round-1)][2]
            self.robotG = self.waves[(self.round-1)][3]
            self.timePerBot = self.waves[self.round-1][4] * 1000
            while self.sending:
                if self.lowTime <= py.time.get_ticks() - self.timePerBot:
                    if self.robotR > 0:
                        self.sentBot = robot("r")
                        self.robotR -= 1
                    elif self.robotO > 0:
                        self.sentBot = robot("o")
                        self.robotO -= 1
                    elif self.robotB > 0:
                        self.sentBot = robot("b")
                        self.robotB -= 1
                    elif self.robotG > 0:
                        self.sentBot = robot("g")
                        self.robotG -= 1
                    else:
                        self.sending = False
                    
                    if self.sending:
                        robotList.add(self.sentBot)
                        self.lowTime = py.time.get_ticks()
                        
                clock.tick(60)
            self.round += 1

    def isSending(self):
        return self.sending
    
    def getRound(self):
        return self.round

    def Reset(self):
        self.round = 1


while running:
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
    
    #Main Menu animation
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

    #This only exists to create a black transistion between game states
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

    #This is the main game stuff
    if state == States.mainGame:
        gamelogic = roundManager()
        gameRunning = True
        j = 0
        
        while gameRunning:
            if j < 2000:
                j = j + 2.5
            pydraw.box(screen, ((0,0),(1280,720)), grassGreen)

            pydraw.box(screen, ((-10, 100), (300, 80)), grayRoad)
            pydraw.box(screen, ((290, 100), (80, 300)), grayRoad)
            pydraw.box(screen, ((290, 400), (500, 80)), grayRoad)
            pydraw.box(screen, ((790, 100), (80, 380)), grayRoad)
            pydraw.box(screen, ((790, 100), (450, 80)), grayRoad)
            pydraw.box(screen, ((1160, 100), (80, 400)), grayRoad)
            pydraw.box(screen, ((90, 490), (1150, 80)), grayRoad)
            pydraw.box(screen, ((90, 490), (80, 300)), grayRoad)

            pydraw.box(unplaceableScreen, ((-10, 100), (300, 80)), grayRoad)
            pydraw.box(unplaceableScreen, ((290, 100), (80, 300)), grayRoad)
            pydraw.box(unplaceableScreen, ((290, 400), (500, 80)), grayRoad)
            pydraw.box(unplaceableScreen, ((790, 100), (80, 380)), grayRoad)
            pydraw.box(unplaceableScreen, ((790, 100), (450, 80)), grayRoad)
            pydraw.box(unplaceableScreen, ((1160, 100), (80, 400)), grayRoad)
            pydraw.box(unplaceableScreen, ((90, 490), (1150, 80)), grayRoad)
            pydraw.box(unplaceableScreen, ((90, 490), (80, 300)), grayRoad)

            pydraw.box(screen, ((880, 190), (270, 290)), oceanBlue)
            pydraw.box(waterScreen, ((880, 190), (270, 290)), oceanBlue)
            pydraw.box(screen, ((0,0),(1280, 95)), black)

            unplaceableScreen.set_colorkey((0,0,0))
            waterScreen.set_colorkey((0,0,0))
            unplaceableMask = py.mask.from_surface(unplaceableScreen)
            waterMask = py.mask.from_surface(waterScreen)
            tempList.update()
            tempList.draw(screen)
            robotList.update()
            robotList.draw(screen)
            towerList.update()
            towerList.draw(screen)
            spriteList.update()
            spriteList.draw(screen)
            
            pydraw.box(screen, ((0, 0),(1280, 90)), darkWood)
            pydraw.box(unplaceableScreen, ((0, 0),(1280, 90)), darkWood)

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

            pydraw.box(screen, ((0, 630),(1280, 110)), darkWood)
            pydraw.box(unplaceableScreen, ((0, 630),(1280, 110)), darkWood)


            for i in range(0,20):
                pydraw.box(screen, ((80 * i, 630),(40, 110)), woodBrown)
            
            for i in range(0,7):
                pydraw.box(screen, ((65 + (i*150),640),(140,80)), (255,255,255))
                    
            pydraw.box(screen, ((1175,635),(100, 80)), (51,255,51))
            pydraw.filled_trigon(screen,1200,645,1200,705,1260,675,(white))
                 
            screen.blit(rinserText, (90,660))
            screen.blit(fountainText, (225,660))
            screen.blit(shipText, (365,660))
            screen.blit(snorklerText, (525,660))
            screen.blit(wellText, (705,660))
            screen.blit(waterCollectorText1, (850,645))
            screen.blit(waterCollectorText2, (840,675))
            screen.blit(waterPumpText1, (995,645))
            screen.blit(waterPumpText2, (995,675))
            py.display.flip()
            clock.tick(60)

            #checks whats being pressed and click
            for event in py.event.get():
                mouse = py.mouse.get_pos()
                if event.type == py.QUIT:
                    running = False
                    gameRunning = False
                if event.type == py.MOUSEBUTTONDOWN:
                    if ((mouse[0] > 1174 and mouse[0] < 1276) and (mouse[1] > 635 and mouse[1] < 716)) and gamelogic.isSending() == False:
                        logicThread = threading.Thread(target=gamelogic.startNextRound)
                        logicThread.start()
                    if ((mouse[0] > 65 and mouse[0] < 205) and (mouse[1] > 640 and mouse[1] < 720)):
                        selectedTower = rinser((mouse[0], mouse[1]), True)
                        tempList.add(selectedTower)
                    if ((mouse[0] > 215 and mouse[0] < 355) and (mouse[1] > 640 and mouse[1 < 720])):
                        selectedTower = fountain((mouse[0], mouse[1]), True)
                        tempList.add(selectedTower)
                    if ((mouse[0] > 365 and mouse[0] < 505) and (mouse[1] > 640 and mouse[1 < 720])):
                        selectedTower = ship((mouse[0], mouse[1]), True)
                        tempList.add(selectedTower)
                if event.type == py.MOUSEBUTTONUP:
                    print("why")
                    tempList.empty()
                    try:
                        selectedTower.unselect()
                        towerList.add(selectedTower)
                        print(towerList)
                    except:
                        pass

    for event in py.event.get():
        if event.type == py.QUIT:
            running = False

    #keep this
    py.display.flip()
    clock.tick(60)

py.quit()