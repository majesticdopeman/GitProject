from House import *
from Bomb import *
from Graphics import *
import math
import random
import vlc

INTRO = 1
letterList1 = []
letterList2 = []
introList1 = ["T","H","I","S", " ","G","A","M","E"," ","I","S", " ", "R","E", "A", "L","L", "Y", " " ,"D","U","M","B", ".", ".", ".", ".", "."]
introList2 = ["C","L","I","C","K", " ","A","N","Y","W","H","E","R", "E "," ", "T","O", " ", "D","R", "O", "P" ," ","A"," ","B", "O", "M", "B", "."]
introList3 = ["T","R","Y"," ","T","O"," ","G","E","T"," ","T","H", "E "," ", "M","O", "S", "T"," ", "R", "E" ,"C","T","A","N", "G", "L", "E", "S", "."]

def startScreen():
    box = Rectangle(Point(0,0), Point(900, 600))
    box.setFill("black")
    box.draw(win)
    image = Image(Point(450, 200), "light.ppm")
    image.draw(win)
    update()
    for i in range(29):
        time.sleep(0.1)
        letter = Text(Point(200 + i*20, 275), introList1[i])
        letterList1.append(letter)
        letter.setSize(16)
        letter.setStyle("bold")
        letter.setTextColor("white")
        letter.setFace("helvetica")
        letter.draw(win)
        update()

    time.sleep(2.42)

    for i in range(29):
        letterList1[i].undraw()
    update()

    for i in range(30):
        time.sleep(0.1)
        letter = Text(Point(200 + i * 20, 275), introList2[i])
        letterList2.append(letter)
        letter.setSize(16)
        letter.setStyle("bold")
        letter.setTextColor("white")
        letter.setFace("helvetica")
        letter.draw(win)
        update()

    time.sleep(1.8)

    for i in range(30):
        letterList2[i].undraw()
    update()

    for i in range(31):
        time.sleep(0.1)
        letter = Text(Point(200 + i * 20, 275), introList3[i])
        letter.setSize(16)
        letter.setStyle("bold")
        letter.setTextColor("white")
        letter.setFace("helvetica")
        letter.draw(win)
        update()

    return image, box, letter

def northernWallDetection(home:House):
    """Detect if house is at the top wall - if it is, it will be moved down"""
    p1y = home.house.getP1().getY()
    if p1y <= 0:
        transport = random.randrange(0, 650, 2)
        home.house.move(0, transport)
        home.centerY += transport

def southernWallDetection(home:House):
    """Detect if ball is at the bottom wall - if it is, it will be moved up"""
    p2y = home.house.getP2().getY()
    if p2y >= 649:
        transport = random.randrange(0, 650, 2)
        home.house.move(0, -1*transport)
        home.centerY -= transport

def easternWallDetection(home:House):
    """Detect if ball is at the bottom wall - if it is, it will be moved up"""
    p2x = home.house.getP2().getX()
    if p2x >= 999:
        transport = random.randrange(0, 1000, 2)
        home.house.move(-1*transport,0)
        home.centerX -= transport

def westernWallDetection(home:House):
    """Detect if ball is at the bottom wall - if it is, it will be moved up"""
    p1x = home.house.getP1().getX()
    if p1x <= 0:
        transport = random.randrange(0, 1000, 2)
        home.house.move(transport, 0)
        home.centerX += transport

def yForCircleTop(xVal, bomb:Bomb):
    """Given the x-value of a circle, return the proper y-value on the circle"""
    value = ((bomb.radius)**2 - (xVal - bomb.center.getX())**2)
    yVal = math.sqrt(value) + bomb.center.getY()
    return yVal

def yForCircleBottom(xVal, bomb:Bomb):
    """Given the x-value of a circle, return the proper y-value on the circle"""
    value = ((bomb.radius)**2 - (xVal - bomb.center.getX())**2)
    yVal = -1*math.sqrt(value) + bomb.center.getY()
    return yVal

def showScore(bomb:Bomb):
    """Prints out score at the end on the screen"""
    score = Text(bomb.center, "Score: " + str(House.destroyed))
    score.setSize(36)
    score.setStyle("bold")
    score.setTextColor("blue")
    score.draw(win)
    update()
    time.sleep(1)
    jump = bomb.radius // 20
    for i in range(20):             ##Moves score left in 20 quick steps (left side of circle)
        score.move(-1*jump, 0)
        update()
        time.sleep(.05)


    stepsAround = 2*bomb.radius
    normalSpeed = int(stepsAround//2*0.96)
    slowerSpeed = (stepsAround//2 - normalSpeed)//2

    for j in range(5):
        choose = random.randint(0,1)
        color = random.choice(["blue", "green", "red", "purple", "yellow", "orange"])
        if choose == 0:
            bomb.blast.setOutline(color)
            score.setTextColor(color)
            bomb.blast.undraw()
            score.undraw()
            update()
            score.draw(win)
            bomb.blast.draw(win)
            update()
            rotateClockwise(slowerSpeed, score, bomb, normalSpeed)
            rotateClockwise2(slowerSpeed, score, bomb, normalSpeed)
        else:
            bomb.blast.setOutline(color)
            score.setTextColor(color)
            bomb.blast.undraw()
            score.undraw()
            update()
            score.draw(win)
            bomb.blast.draw(win)
            update()
            rotateCounterClockwise(slowerSpeed, score, bomb, normalSpeed)
            rotateCounterClockwise2(slowerSpeed, score, bomb, normalSpeed)

def rotateClockwise(slowerSpeed, score, bomb, normalSpeed):
    for i in range(slowerSpeed):
        newY = yForCircleBottom(score.getAnchor().getX() + 2, bomb)
        dy = newY - score.getAnchor().getY()
        score.move(2, dy)
        update()
        time.sleep(.02)

    for i in range(normalSpeed):
        newY = yForCircleBottom(score.getAnchor().getX() + 2, bomb)
        dy = newY - score.getAnchor().getY()
        score.move(2, dy)
        update()
        time.sleep(.0025)

    for i in range(slowerSpeed):
        newY = yForCircleBottom(score.getAnchor().getX() + 2, bomb)
        dy = newY - score.getAnchor().getY()
        score.move(2, dy)
        update()
        time.sleep(.02)

def rotateClockwise2(slowerSpeed, score, bomb, normalSpeed):
    for i in range(slowerSpeed):
        newY = yForCircleTop(score.getAnchor().getX() - 2, bomb)
        dy = newY - score.getAnchor().getY()
        score.move(-2, dy)
        update()
        time.sleep(.02)

    for i in range(normalSpeed):
        newY = yForCircleTop(score.getAnchor().getX() - 2, bomb)
        dy = newY - score.getAnchor().getY()
        score.move(-2, dy)
        update()
        time.sleep(.0025)

    for i in range(slowerSpeed):
        newY = yForCircleTop(score.getAnchor().getX() - 2, bomb)
        dy = newY - score.getAnchor().getY()
        score.move(-2, dy)
        update()
        time.sleep(.02)

def rotateCounterClockwise(slowerSpeed, score, bomb, normalSpeed):
    for i in range(slowerSpeed):
        newY = yForCircleTop(score.getAnchor().getX() + 2, bomb)
        dy = newY - score.getAnchor().getY()
        score.move(2, dy)
        update()
        time.sleep(.02)

    for i in range(normalSpeed):
        newY = yForCircleTop(score.getAnchor().getX() + 2, bomb)
        dy = newY - score.getAnchor().getY()
        score.move(2, dy)
        update()
        time.sleep(.0025)

    for i in range(slowerSpeed):
        newY = yForCircleTop(score.getAnchor().getX() + 2, bomb)
        dy = newY - score.getAnchor().getY()
        score.move(2, dy)
        update()
        time.sleep(.02)

def rotateCounterClockwise2(slowerSpeed, score, bomb, normalSpeed):
    for i in range(slowerSpeed):
        newY = yForCircleBottom(score.getAnchor().getX() - 2, bomb)
        dy = newY - score.getAnchor().getY()
        score.move(-2, dy)
        update()
        time.sleep(.02)

    for i in range(normalSpeed):
        newY = yForCircleBottom(score.getAnchor().getX() - 2, bomb)
        dy = newY - score.getAnchor().getY()
        score.move(-2, dy)
        update()
        time.sleep(.0025)

    for i in range(slowerSpeed):
        newY = yForCircleBottom(score.getAnchor().getX() - 2, bomb)
        dy = newY - score.getAnchor().getY()
        score.move(-2, dy)
        update()
        time.sleep(.02)

def gameOverExit(houseList:list):
    """When bomb is dropped, houses not hit fly off the screen one by one!"""
    for j in range(10):
        for i in houseList:
            if i.isDestroyed == False:
                if i.centerX >= 500 and i.centerY >= 325:
                    i.house.setFill("Blue")
                    i.house.move(40, 40)
                elif i.centerX >= 500 and i.centerY <325:
                    i.house.setFill("Blue")
                    i.house.move(40, -40)
                elif i.centerX < 500 and i.centerY >= 325:
                    i.house.setFill("Blue")
                    i.house.move(-40, 40)
                else:
                    i.house.setFill("Blue")
                    i.house.move(-40, -40)
        update()

def redHousesExit(houseList:list):
    """Red houses exit to center of circle"""



win = GraphWin("House Test", 1000, 650, autoflush = False)
win.setBackground("white")


def main():
    if INTRO == 1:
        audio = vlc.MediaPlayer("Resources/Deathless.mp3")
        audio.play()
        image, box, letter = startScreen()
        time.sleep(1.25)
        image.undraw()
        box.undraw()
        letter.undraw()
        update()

    houses = []

    if INTRO == 1:
        for i in range(7):
            #house = House(random.randrange(15, 984), random.randrange(15, 634))
            house = House(200 + i*40, 400)
            house.drawHouse(win)
            houses.append(house)
            update()
            time.sleep(0.1)

        time.sleep(3)

        for i in range(7):
            house = House(random.randrange(15, 984), random.randrange(15, 634))
            house.drawHouse(win)
            houses.append(house)
            update()
            time.sleep(0.1)

    else:
        for i in range(100):
            house = House(random.randrange(15, 984), random.randrange(15, 634))
            house.drawHouse(win)
            houses.append(house)

    while True:                                 ##Animation loop
        for i in houses:
            dx = random.randrange(-20,21,5)
            dy = random.randrange(-20,21,5)
            i.house.move(dx, dy)
            northernWallDetection(i)
            southernWallDetection(i)
            easternWallDetection(i)
            westernWallDetection(i)
            i.centerX += dx
            i.centerY += dy

        update()
        time.sleep(0.01)
        click = win.checkMouse()
        #click = Point(500, 325)
        if click != None:
            break



    bomb = Bomb(click)
    bomb.drawBomb(win)
    update()
    bombAudio = vlc.MediaPlayer("Resources/Explosion.mp3")
    bombAudio.play()

    for i in houses:
        i.isItHit(bomb, click)

    update()

    gameOverExit(houses)

    showScore(bomb)

    audio.stop()

    win.getMouse()
    win.close()

main()