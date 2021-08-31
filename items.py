from graphics import *
from random import *
import pygame
import sys
from time import *
import time
from pygame.locals import *
Window_Width, Window_Height = 800, 600
win = GraphWin('UJ Simulator', Window_Width, Window_Height)
win.setCoords(0, 0, 3, 8)
pygame.mixer.init()
New_Page = Rectangle(Point(0, 0), Point(3, 8))
New_Page.setOutline('white')
New_Page.setFill('white')

# --------------------------------------------------------------------------------------------variables used for calc()
Running = True
total1 = ""
total2 = ""
total_number = 0
change_given = 0
total_change_given = 0
Plus = False
Minus = False
Multiply = False
# -----------------------------------------------------------------------------------------

alignment = 0                           #variable used for deciding the ending

counter_image = Image(Point(1.5, 4), 'images/UJ Background.gif')
counter_image.draw(win)



# -------------------------------------------------------------------------------------------------------- item array
#               0    1     2     3    4     5     6     7     8     9     10    11    12   13   14   15    16    17    18    19
item_price = [1.87, 0.5, 0.44, 0.98, 0.6, 0.64, 0.46, 3.67, 2.12, 2.77, 1.77, 1.51, 0.14, 0.9, 0.95, 1, 0.58, 1.39, 0.58, 0.89]
item_name = ['images/Chips.gif', 'images/Dr.Pepper.gif', 'images/Gatorade.gif', 'images/Slim_Monster.gif',
             'images/Pepsi.gif', 'images/Sprite.gif', 'images/Toreta.gif', 'images/Haribo.gif',
             "images/hershey's.gif", "images/Lay's_monster.gif", "images/Lay's_Pepper.gif",
             'images/Lays_Lemon.gif', 'images/Lolipop.gif', 'images/Noodle.gif', 'images/Noodle_2P.gif',
             'images/Noodle_3P.gif', 'images/twix.gif', 'images/Cookie.gif', 'images/Cracker.gif',
             'images/Snickers.gif']

customers = ['images/Man.gif', 'images/Woman.gif','images/OG.gif','images/SUNY.gif','images/Utah.gif',
             'images/G.Mason.gif','images/Ghent.gif']



talkbox = Rectangle(Point(0, 0), Point(3, 1.8))
talkbox.setWidth(5)
talkbox.setFill('white')

def bgm():
    pygame.mixer.music.load('audios/TheFatRat - Unity.wav')
    pygame.mixer.music.play()
bgm()


def scenechange():
    r = 255
    g = 255
    b = 255

    Window_for_Tutorial = Rectangle(Point(0, 0), Point(3, 8))
    Window_for_Tutorial.draw(win)

    for i in range(100):
        Window_for_Tutorial.setOutline(color_rgb(r, g, b))
        Window_for_Tutorial.setFill(color_rgb(r, g, b))
        r -= 20
        g -= 20
        b -= 20

        if r < 0 and g < 0 and b < 0:
            break

    sleep(0.5)

    color_change = 'black'
    Window_for_Tutorial = Rectangle(Point(0, 0), Point(3, 8))
    Window_for_Tutorial.setOutline(color_change)
    Window_for_Tutorial.setFill(color_change)
    Window_for_Tutorial.draw(win)

    r = 0
    g = 0
    b = 0
    x = 0
    y = -5

    for i in range(100):
        Window_for_Tutorial.setOutline(color_rgb(r, g, b))
        Window_for_Tutorial.setFill(color_rgb(r, g, b))
        r += 20
        g += 20
        b += 20

        if r > 255 and g > 255 and b > 255:
            color_change = 'white'
            break

Day = Image(Point(2.55, 6.8), 'images/One.gif')
def statistics():
    scenechange()
    statistics = Image(Point(1.5, 4), 'images/statistics.gif')
    statistics.draw(win)

    sleep(0.5)
    Day.draw(win)

    Satisfied_s = Text(Point(2.3, 4.75), Satisfied)
    Satisfied_s.setSize(36)
    Satisfied_s.setStyle('bold')
    sleep(0.7)
    Satisfied_s.draw(win)

    Unsatisfied_s = Text(Point(2.3, 2.7), Unsatisfied)
    Unsatisfied_s.setSize(36)
    Unsatisfied_s.setStyle('bold')
    sleep(0.7)
    Unsatisfied_s.draw(win)

    Total_s = Text(Point(2.3, 0.8), Satisfied + Unsatisfied)
    Total_s.setSize(36)
    Total_s.setStyle('bold')
    sleep(1.2)
    Total_s.draw(win)

    sleep(1.5)
    scenechange()

#--------------------------------------------------------------------------animation for transition between days

def Day3():
    global Day1

    x = 0
    y = -5

    Day1 = Text(Point(x, 4.5), 'Day 3')
    Day1.setSize(36)
    Day1.setStyle('bold')
    Day1.setFace('courier')
    Day1.draw(win)

    pygame.mixer.music.load('audios/Flying.wav')
    pygame.mixer.music.play()
    while x < 1.5:
        Day1.move(0.02, 0)
        x += 0.02

    sleep(0.5)

    pygame.mixer.music.load('audios/Alarm Clock.wav')
    pygame.mixer.music.play()
    for i in range(5):          #moves the text back and forth
        Day1.move(-0.02, 0)
        Day1.move(0.02, 0)
        Day1.move(-0.02, 0.02)
        Day1.move(0.02, -0.02)
        Day1.move(0.02, 0)
        Day1.move(-0.02, 0)
        Day1.move(0.02, -0.02)
        Day1.move(-0.02, 0.02)

    sleep(0.5)

    pygame.mixer.music.load('audios/Flying.wav')
    pygame.mixer.music.play()
    while x < 4:
        Day1.move(0.02, 0)
        x += 0.02


    UJ_Background = Image(Point(1.5, 4), 'images/UJ Background.gif')
    UJ_Background.draw(win)

    #while y < 4:
     #   UJ_Background.move(0, 0.04)
      #  y += 0.04

    x = -2

    boss_walking = Image(Point(x, 4.8), 'images/boss walk.gif')
    boss_walking.draw(win)
    pygame.mixer.music.load('audios/footstep.wav')
    pygame.mixer.music.play()

    for i in range(275):
        boss_walking.move(0.01, 0)

    boss_walking.undraw()
    boss = Image(Point(0.75, 4.8), 'images/Boss counter version.gif')
    boss.draw(win)
    pygame.mixer.music.stop()


    talkbox.draw(win)
    talk21 = Text(Point(1.5,1),"I heard that it's your last day today")
    talk21.setSize(25)
    talk21.draw(win)

    if win.getMouse():
        talk21.undraw()

    talk22 = Text(Point(1.5,1), 'I think it will the busiest day!!')
    talk22.setSize(25)
    talk22.draw(win)

    if win.getMouse():
        talk22.undraw()

    talk23 = Text(Point(1.5,1), 'Good luck.')
    talk23.setSize(25)
    talk23.draw(win)

    if win.getMouse():
        talk23.undraw()
        talkbox.undraw()


    if win.getMouse():
        boss.undraw()

    Smiling_Boss = Image(Point(0.75, 4.8), 'images/Smiling_Boss.gif')
    Smiling_Boss.draw(win)
    sleep(1)

    Walking_Boss_2 = Image(Point(0.75, 4.8), 'images/Walking_Boss_2.gif')
    Walking_Boss_2.draw(win)
    Smiling_Boss.undraw()
    pygame.mixer.music.load('audios/footstep.wav')
    pygame.mixer.music.play()

    for i in range(275):
        Walking_Boss_2.move(-0.01, 0)

    pygame.mixer.music.stop()


# The choice made here affects the ending of game.
# This is one of the marking point of the story of this game.
def Boss_event():
    global Day1
    x = 0
    y = -5
    New_Page.draw(win)
    Day1 = Text(Point(x, 4.5), 'Day 2')
    Day1.setSize(36)
    Day1.setStyle('bold')
    Day1.setFace('courier')
    Day1.draw(win)

    pygame.mixer.music.load('audios/Flying.wav')
    pygame.mixer.music.play()
    while x < 1.5:
        Day1.move(0.02, 0)
        x += 0.02

    sleep(0.5)

    pygame.mixer.music.load('audios/Alarm Clock.wav')
    pygame.mixer.music.play()
    for i in range(5):  # moves the text back and forth
        Day1.move(-0.02, 0)
        Day1.move(0.02, 0)
        Day1.move(-0.02, 0.02)
        Day1.move(0.02, -0.02)
        Day1.move(0.02, 0)
        Day1.move(-0.02, 0)
        Day1.move(0.02, -0.02)
        Day1.move(-0.02, 0.02)

    sleep(0.5)

    pygame.mixer.music.load('audios/Flying.wav')
    pygame.mixer.music.play()
    while x < 4:
        Day1.move(0.02, 0)
        x += 0.02

    UJ_Background = Image(Point(1.5, 4), 'images/UJ Background.gif')
    UJ_Background.draw(win)

    # while y < 4:
    #   UJ_Background.move(0, 0.04)
    #  y += 0.04

    x = -2

    boss_walking = Image(Point(x, 4.8), 'images/boss walk.gif')
    boss_walking.draw(win)
    pygame.mixer.music.load('audios/footstep.wav')
    pygame.mixer.music.play()

    for i in range(275):
        boss_walking.move(0.01, 0)

    boss_walking.undraw()
    boss = Image(Point(0.75, 4.8), 'images/Boss counter version.gif')
    boss.draw(win)
    pygame.mixer.music.stop()

    talkbox.draw(win)
    talk21 = Text(Point(1.5, 1), "Well... You've done quite good job yesterday.")
    talk21.setSize(25)
    talk21.draw(win)

    if win.getMouse():
        talk21.undraw()

    talk22 = Text(Point(1.5, 1), 'I expect you to do the same job today!')
    talk22.setSize(25)
    talk22.draw(win)

    if win.getMouse():
        talk22.undraw()

    talk23 = Text(Point(1.5, 1), 'Good luck again!')
    talk23.setSize(25)
    talk23.draw(win)

    if win.getMouse():
        talk23.undraw()
        talkbox.undraw()
        boss.undraw()

    Walking_Boss_2 = Image(Point(0.75, 4.8), 'images/Walking_Boss_2.gif')
    Walking_Boss_2.draw(win)
    pygame.mixer.music.load('audios/footstep.wav')
    pygame.mixer.music.play()

    for i in range(275):
        Walking_Boss_2.move(-0.01, 0)

    pygame.mixer.music.stop()

    sleep(0.5)

    talk24 = Text(Point(1.5, 1), '...')
    talk24.setSize(25)
    talkbox.draw(win)
    talk24.draw(win)

    sleep(1)

    talk24.undraw()
    talkbox.undraw()

    x = -2
    boss_walking = Image(Point(x, 4.8), 'images/boss walk.gif')
    boss_walking.draw(win)
    pygame.mixer.music.load('audios/footstep.wav')
    pygame.mixer.music.play()

    for i in range(137):
        boss_walking.move(0.02, 0)

    boss_walking.undraw()
    boss = Image(Point(0.75, 4.8), 'images/Boss counter version.gif')
    boss.draw(win)
    pygame.mixer.music.stop()

    talk25 = Text(Point(1.5, 1), 'Oh... I almost forgot something.')
    talk25.setSize(25)
    talkbox.draw(win)
    talk25.draw(win)

    if win.getMouse():
        talk25.undraw()

    talk26 = Text(Point(1.5, 1), 'This is for you!')
    talk26.setSize(25)
    talk26.draw(win)

    if win.getMouse():
        talk26.undraw()
        talkbox.undraw()

    present = Image(Point(0.8, 2.6), 'images/Coke.gif')
    present.draw(win)

    sleep(0.5)

    talkbox.draw(win)
    talk27 = Text(Point(1.5, 1), 'Please feel free to drink this!')
    talk27.setSize(25)
    talk27.draw(win)

    if win.getMouse():
        talk27.undraw()
        talkbox.undraw()

    decision_box1 = Rectangle(Point(0.6, 6), Point(0.90, 6.5))
    decision_box1.setFill('white')
    decision_box1.draw(win)
    choice1 = Text(Point(.75, 6.25), "Drink!")
    choice1.draw(win)
    decision_box2 = Rectangle(Point(2, 6), Point(2.5, 6.5))
    decision_box2.setFill('white')
    decision_box2.draw(win)
    choice2 = Text(Point(2.25, 6.25), "Don't drink!")
    choice2.draw(win)

    while True:
        point = win.getMouse()
        x_pos = point.getX()
        y_pos = point.getY()
        if 2 < x_pos < 2.5 and 6 < y_pos < 6.5:
            global alignment
            alignment -= 1
            decision_box1.undraw()
            choice1.undraw()
            decision_box2.undraw()
            choice2.undraw()
            dialogue = Text(Point(1.5, 1), "Oh...")
            dialogue.setSize(25)
            talkbox.draw(win)
            dialogue.draw(win)
            if win.getMouse():
                dialogue.undraw()
            dialogue = Text(Point(1.5, 1), "So... you don't want it?")
            dialogue.setSize(25)
            dialogue.draw(win)
            if win.getMouse():
                dialogue.undraw()
            dialogue = Text(Point(1.5, 1), "...Ok! I'm good with that!")
            dialogue.setSize(25)
            dialogue.draw(win)
            if win.getMouse():
                dialogue.undraw()

            dialogue = Text(Point(1.5, 1), 'Good luck today!')
            dialogue.setSize(25)
            dialogue.draw(win)

            if win.getMouse():
                dialogue.undraw()
                talkbox.undraw()
                sleep(0.5)
                boss.undraw()
                Walking_Boss_2 = Image(Point(0.75, 4.8), 'images/Walking_Boss_2.gif')
                Walking_Boss_2.draw(win)
                band = Rectangle(Point(0.32, 1.9), Point(1.22, 3.1))
                band.setOutline('white')
                band.setFill('white')
                band.draw(win)
                pygame.mixer.music.load('audios/footstep.wav')
                pygame.mixer.music.play()

                for i in range(275):
                    Walking_Boss_2.move(-0.01, 0)

                pygame.mixer.music.stop()

            pygame.mixer.music.stop()
            break

        if .6 < x_pos < 0.9 and 6 < y_pos < 6.5:
            alignment += 1
            decision_box1.undraw()
            choice1.undraw()
            decision_box2.undraw()
            choice2.undraw()
            dialogue = Text(Point(1.5, 1), "Good!")
            dialogue.setSize(25)
            talkbox.draw(win)
            dialogue.draw(win)
            if win.getMouse():
                dialogue.undraw()
            dialogue = Text(Point(1.5, 1), "I guess you liked the present!")
            dialogue.setSize(25)
            dialogue.draw(win)
            if win.getMouse():
                dialogue.undraw()
            dialogue = Text(Point(1.5, 1), 'Good luck again!')
            dialogue.setSize(25)
            dialogue.draw(win)

            if win.getMouse():
                boss.undraw()
                dialogue.undraw()
                talkbox.undraw()
                Smiling_Boss = Image(Point(0.75, 4.8), 'images/Smiling_Boss.gif')
                Smiling_Boss.draw(win)
                sleep(1)
                Walking_Boss_2 = Image(Point(0.75, 4.8), 'images/Walking_Boss_2.gif')
                Walking_Boss_2.draw(win)
                Smiling_Boss.undraw()
                pygame.mixer.music.load('audios/footstep.wav')
                pygame.mixer.music.play()

                for i in range(275):
                    Walking_Boss_2.move(-0.01, 0)

                pygame.mixer.music.stop()
                break

# ------------------------------------------------------------------------------------------------ event for prof. adam
def adamstory():
    customer.undraw()
    band = Rectangle(Point(0.32, 1.9), Point(1.22, 3.1))
    band.setOutline('white')
    band.setFill('white')
    band.draw(win)

    pygame.mixer.music.load('audios/Adam Theme.wav')
    pygame.mixer.music.play()

    adam_moving = Image(Point(0,5.1), 'images/adam_counter.gif')
    adam_moving.draw(win)

    for i in range(400):
        adam_moving.move(0.002,0)

    talkbox.draw(win)
    dialogue = Text(Point(1.5, 1), "Hey, fluffykitten420....")
    dialogue.setSize(25)
    dialogue.draw(win)
    if win.getMouse():
        dialogue.undraw()


    x = 0.5
    for i in range(5):
        Monster = Image(Point(x, 2.4), 'images/Fat_Monster.gif')
        Monster.draw(win)
        x += .15

    dialogue = Text(Point(1.5, 1), "These totally aren't my 4th batch of monsters.")
    dialogue.setSize(25)
    dialogue.draw(win)
    if win.getMouse():
        dialogue.undraw()

    dialogue = Text(Point(1.5, 1), "Cmon, quickly. Here's 50 dollars.")
    dialogue.setSize(25)
    dialogue.draw(win)
    if win.getMouse():
        dialogue.undraw()

    dialogue = Text(Point(1.5, 1), "Keep the change just sell these Monsters to me.")
    dialogue.setSize(25)
    dialogue.draw(win)
    if win.getMouse():
        dialogue.undraw()
        talkbox.undraw()
    decision_box1 = Rectangle(Point(.4, 6), Point(1.1, 6.5))
    decision_box1.setFill('white')
    decision_box1.draw(win)
    choice1 = Text(Point(.75, 6.25), "Sell the drinks")
    choice1.draw(win)
    decision_box2 = Rectangle(Point(1.9, 6), Point(2.6, 6.5))
    decision_box2.setFill('white')
    decision_box2.draw(win)
    choice2 = Text(Point(2.25, 6.25), "Don't sell the drinks")
    choice2.draw(win)

    talk28 = Text(Point(1.5, 1), 'Choose what you want to do.\n'
                                 'This will affect the ending of this game.')
    talk28.setSize(25)
    talkbox.draw(win)
    talk28.draw(win)

    if win.getMouse():
        talk28.undraw()
        talkbox.undraw()

    while True:
        point = win.getMouse()
        x_pos = point.getX()
        y_pos = point.getY()
        if 2 < x_pos < 2.5 and 6 < y_pos < 6.5:
            global alignment
            alignment += 1
            decision_box1.undraw()
            choice1.undraw()
            decision_box2.undraw()
            choice2.undraw()
            dialogue = Text(Point(1.5, 1), "WOW. You are so mean. \n"
                                           "Guess who won't get an A in CSE101?")
            dialogue.setSize(25)
            talkbox.draw(win)
            dialogue.draw(win)
            if win.getMouse():
                dialogue.undraw()
            dialogue = Text(Point(1.5, 1), "YOU! FLUFFYKITTEN420!!")
            dialogue.setSize(25)
            dialogue.draw(win)
            if win.getMouse():
                dialogue.undraw()
                talkbox.undraw()
            for i in range(400):
                adam_moving.move(-0.02, 0)
            counter_image.undraw()
            break
        if .5 < x_pos < 1 and 6 < y_pos < 6.5:
            alignment -= 1
            decision_box1.undraw()
            choice1.undraw()
            decision_box2.undraw()
            choice2.undraw()
            dialogue = Text(Point(1.5, 1), "Thanks. \n"
                                           "Someone might get an A in CSE101 ;)")
            dialogue.setSize(25)
            talkbox.draw(win)
            dialogue.draw(win)
            if win.getMouse():
                dialogue.undraw()
            dialogue = Text(Point(1.5, 1), "Have a great day!!!!")
            dialogue.setSize(25)
            dialogue.draw(win)
            if win.getMouse():
                dialogue.undraw()
                talkbox.undraw()
            band = Rectangle(Point(0.32, 1.9), Point(1.22, 3.1))
            band.setOutline('white')
            band.setFill('white')
            band.draw(win)
            for i in range(400):
                adam_moving.move(-0.02, 0)
            counter_image.undraw()
            break

# ------------------------------------------------------------------------------------------------ event for president
def presidentstory():
    pygame.mixer.music.load('audios/president_theme.wav')
    pygame.mixer.music.play()
    customer.undraw()
    band = Rectangle(Point(0.32, 1.9), Point(1.22, 3.1))
    band.setOutline('white')
    band.setFill('white')
    band.draw(win)

    counter_image.draw(win)

    president_moving = Image(Point(0, 5), 'images/president_counter.gif')
    president_moving.draw(win)

    for i in range(400):
        president_moving.move(0.002, 0)

    talkbox.draw(win)
    dialogue = Text(Point(1.5, 1), "The time has come for us to make a move... ", )
    dialogue.setSize(25)
    dialogue.draw(win)
    if win.getMouse():
        dialogue.undraw()

    dialogue = Text(Point(1.5, 1), "It is time to initiate the plan...")
    dialogue.setSize(25)
    dialogue.draw(win)
    if win.getMouse():
        dialogue.undraw()

    dialogue = Text(Point(1.5, 1), "Execute SKFSD.")
    dialogue.setSize(25)
    dialogue.draw(win)
    if win.getMouse():
        dialogue.undraw()
        talkbox.undraw()

    decision_box1 = Rectangle(Point(.4, 6), Point(1.1, 6.5))
    decision_box1.setFill('white')
    decision_box1.draw(win)
    choice1 = Text(Point(.75, 6.25), "Execute SKFSD")
    choice1.draw(win)
    decision_box2 = Rectangle(Point(1.9, 6), Point(2.6, 6.5))
    decision_box2.setFill('white')
    decision_box2.draw(win)
    choice2 = Text(Point(2.25, 6.25), "Delay SKFSD")
    choice2.draw(win)

    point = win.getMouse()
    x_pos = point.getX()
    y_pos = point.getY()

    if .5 < x_pos < 1 and 6 < y_pos < 6.5:  # if choice 1/ Execute SKFSD
        global alignment
        alignment -= 1
        decision_box1.undraw()
        choice1.undraw()
        decision_box2.undraw()
        choice2.undraw()
        dialogue = Text(Point(1.5, 1), "You know what to do.")
        dialogue.setSize(25)
        talkbox.draw(win)
        dialogue.draw(win)
        if win.getMouse():
            dialogue.undraw()
        dialogue = Text(Point(1.5, 1), "Good luck soldier.")
        dialogue.setSize(25)
        dialogue.draw(win)
        if win.getMouse():
            dialogue.undraw()
            talkbox.undraw()
        for i in range(400):
            president_moving.move(-0.02, 0)

    if 2 < x_pos < 2.5 and 6 < y_pos < 6.5:  # if choice 2/ Delay SKFSD
        alignment += 1
        decision_box1.undraw()
        choice1.undraw()
        decision_box2.undraw()
        choice2.undraw()
        dialogue = Text(Point(1.5, 1), "You think it is too early to initiate SKFSD?")
        dialogue.setSize(25)
        talkbox.draw(win)
        dialogue.draw(win)
        if win.getMouse():
            dialogue.undraw()
        dialogue = Text(Point(1.5, 1), "Hmm, you may be right. It has been long enough for you.")
        dialogue.setSize(25)
        dialogue.draw(win)
        if win.getMouse():
            dialogue.undraw()
        dialogue = Text(Point(1.5, 1), "Until further instructions, stay put and continue working.")
        dialogue.setSize(25)
        dialogue.draw(win)
        if win.getMouse():
            dialogue.undraw()
            talkbox.undraw()
        for i in range(400):
            president_moving.move(-0.02, 0)
        pygame.mixer.music.stop()

# ----------------------------------------------------------------------------------------function for game over screen
def game_over():
    pygame.mixer.music.stop()
    pygame.mixer.music.load('audios/game over song.wav')
    pygame.mixer.music.play()
    New_Page = Rectangle(Point(0, 0), Point(3, 8))
    New_Page.setOutline('white')
    New_Page.setFill('white')
    New_Page.draw(win)
    for i in range(100):
        adamface = randrange(1,4)
        if adamface == 1:
            face = Image(Point(random() * 3, random() * 8), 'images/adam1.gif')
            face.draw(win)
        elif adamface == 2:
            face = Image(Point(random() * 3, random() * 8), 'images/adam2.gif')
            face.draw(win)
        elif adamface == 3:
            face = Image(Point(random() * 3, random() * 8), 'images/adam3.gif')
            face.draw(win)
    Next = Text(Point(1.5, 4), "Game Over")
    Next.setSize(35)
    Next.draw(win)
    if win.getMouse():
        sys.exit()

def ending():
    if alignment < 0:
        RE = Rectangle(Point(0,0), Point(3,8))
        RE.setOutline('white')
        RE.setFill('white')
        RE.draw(win)
        dialogue = Text(Point(1.5, 4), "After a few weeks...")
        dialogue.setSize(25)
        dialogue.draw(win)
        if win.getMouse():
            dialogue.undraw()
        background_image = Image(Point(1.5, 4), 'images/UJ_door_closed.gif')
        background_image.draw(win)
        dialogue = Text(Point(1.5, 1), "The cops came bursting through the \n"
                                       " front door of UJ convenience.")
        dialogue.setSize(25)
        dialogue.draw(win)
        if win.getMouse():
            dialogue.undraw()
        dialogue = Text(Point(1.5, 1), "They arrested the owner of UJ convenience \n"
                                       "for tax evasion.")
        dialogue.setSize(25)
        dialogue.draw(win)
        if win.getMouse():
            dialogue.undraw()
        background_image = Image(Point(1.5, 4), 'images/UJ_door_open.gif')
        background_image.draw(win)
        dialogue = Text(Point(1.5, 1), "The owner was confused but complied to the authority.")
        dialogue.setSize(25)
        dialogue.draw(win)
        if win.getMouse():
            dialogue.undraw()
        dialogue = Text(Point(1.5, 1), "Little did he know, these cops were paid off.")
        dialogue.setSize(25)
        dialogue.draw(win)
        if win.getMouse():
            dialogue.undraw()
        dialogue = Text(Point(1.5, 1), "I messed with the inventory and bank book.\n"
                                       "He couldn't have paid the right amount of tax.")
        dialogue.setSize(25)
        dialogue.draw(win)
        if win.getMouse():
            dialogue.undraw()
        dialogue = Text(Point(1.5, 1), "The UJ owner won't be coming back for a long time.")
        dialogue.setSize(25)
        dialogue.draw(win)
        if win.getMouse():
            dialogue.undraw()
        dialogue = Text(Point(1.5, 1), "Now the convenience store is under \n"
                                       "the control of SUNY Korea.")
        dialogue.setSize(25)
        dialogue.draw(win)
        if win.getMouse():
            dialogue.undraw()
        arrest_image = Image(Point(2.5, 2.85), 'images/arrested.gif')
        arrest_image.draw(win)
        for i in range(140):
            arrest_image.move(-.01, 0)
        dialogue = Text(Point(1.5, 1), "Long live the president.")
        dialogue.setSize(25)
        dialogue.draw(win)
        if win.getMouse():
            dialogue.undraw()
            endingbox = Rectangle(Point(1, 5.5), Point(2, 6.5))
            endingbox.setFill('white')
            endingbox.draw(win)
            dialogue = Text(Point(1.5, 6), "Loyalist Ending")
            dialogue.setSize(25)
            dialogue.draw(win)
        if win.getMouse():
            win.close()

    elif alignment > 0:
        pygame.mixer.music.load('audios/Best_day.wav')
        pygame.mixer.music.play()
        New_Page2 = New_Page.clone()
        New_Page2.draw(win)
        dialogue = Text(Point(1.5, 4), "After a few weeks...")
        dialogue.setSize(25)
        dialogue.draw(win)
        if win.getMouse():
            dialogue.undraw()
        background_image = Image(Point(1.5, 4), 'images/UJ Background.gif')
        background_image.draw(win)
        boss = Image(Point(0.8, 4.8), 'images/Boss counter version.gif')
        boss.draw(win)
        talkbox.draw(win)
        dialogue = Text(Point(1.5, 1), "Hey, you've done a wonderful job \n"
                                       "and you deserve more than being a part timer.")
        dialogue.setSize(25)
        dialogue.draw(win)
        if win.getMouse():
            dialogue.undraw()
        dialogue = Text(Point(1.5, 1), "I'm trying to expand UJ convenience and  \n"
                                       "need a new manager.")
        dialogue.setSize(25)
        dialogue.draw(win)
        if win.getMouse():
            dialogue.undraw()
        badge_box = Image(Point(.8, 2.4), 'images/badge_box.gif')
        badge_box.draw(win)
        dialogue = Text(Point(1.5, 1), "You are the most qualified person I know. \n"
                                       "Here is your manager's badge.")
        dialogue.setSize(25)
        dialogue.draw(win)
        if win.getMouse():
            dialogue.undraw()

        background_image = Image(Point(1.5, 4), 'images/badge_box_background.gif')
        background_image.draw(win)
        dialogue = Text(Point(1.5, 1), "With your level of professionalism, \n"
                                       "I'm sure we can even get a third UJ store")
        dialogue.setSize(25)
        dialogue.draw(win)
        if win.getMouse():
            dialogue.undraw()
        background_image.undraw()

        dialogue = Text(Point(1.5, 1), "Let's do our best, partner.")
        dialogue.setSize(25)
        dialogue.draw(win)
        boss = Image(Point(0.8, 4.8), 'images/Smiling_Boss.gif')
        boss.draw(win)

        if win.getMouse():
            endingbox = Rectangle(Point(1, 5.5), Point(2, 6.5))
            endingbox.setFill('white')
            endingbox.draw(win)
            dialogue = Text(Point(1.5, 6), "Renegade Ending")
            dialogue.setSize(25)
            dialogue.draw(win)
            if win.getMouse():
                win.close()

#-------------------------------------------------------- function for the cash register/calculator
def calc():
    point = win.getMouse()
    x_pos = point.getX()
    y_pos = point.getY()
    global button_lists,button_close,total1, total2, Plus, Minus, Multiply, total_number, total_change_given, \
        customer_price, total_price

        #using getMouse/mouse location for detecting which button is pressed
    if 0.15 < x_pos < 0.25 and 2.3 < y_pos < 2.8:
        button_close = Rectangle(Point(1.5, 6.8), Point(1.635, 7.25))
        button_close.setFill('white')
        button_close.setOutline('white')
        button_close.draw(win)
        button_lists = Image(Point(0.9, 4.5), 'images/Price_list.gif')
        button_lists.draw(win)
    elif 1.5 < x_pos < 1.635 and 6.8 < y_pos < 7.25:
        button_close.undraw()
        button_lists.undraw()
    if 1.84 < x_pos < 1.96 and 2.7 < y_pos < 2.9:
        total1 = total1 + "1"
        refresh()
    elif 2.03 < x_pos < 2.16 and 2.7 < y_pos < 3:
        total1 = total1 + "2"
        refresh()
    elif 2.23 <= x_pos <= 2.35 and 2.7 < y_pos < 2.9:
        total1 = total1 + "3"
        refresh()
    elif 1.845 < x_pos < 1.96 and 3.05 < y_pos < 3.25:
        total1 = total1 + "4"
        refresh()
    elif 2.04 < x_pos < 2.16 and 3.05 <= y_pos <= 3.25:
        total1 = total1 + "5"
        refresh()
    elif 2.23 < x_pos < 2.35 and 3.05 < y_pos < 3.25:
        total1 = total1 + "6"
        refresh()
    elif 1.85 < x_pos < 1.97 and 3.4 < y_pos < 3.6:
        total1 = total1 + "7"
        refresh()
    elif 2.04 < x_pos < 2.16 and 3.4 <= y_pos <= 3.6:
        total1 = total1 + "8"
        refresh()
    elif 2.235 < x_pos < 2.35 and 3.4 < y_pos < 3.6:
        total1 = total1 + "9"
        refresh()
    elif 1.835 < x_pos < 1.95 and 2.3 < y_pos < 2.5:
        total1 = total1 + "0"
        refresh()
    elif 2.03 < x_pos < 2.15 and 2.3 < y_pos < 2.55:  # decimal
        total1 = total1 + "."
        refresh()
    elif 2.23 < x_pos < 2.35 and 2.3 < y_pos < 2.55:  # backspace
        total1 = total1[:-1]
        refresh()
    elif 2.43 < x_pos < 2.55 and 2.33 < y_pos < 2.9:  # clear
        total1 = ""
        refresh()
    elif 2.42 < x_pos < 2.55 and 3.4 < y_pos < 3.6:  # plus
        total2 = total1
        total1 = ""
        refresh()
        Plus = True
        Minus = False
        Multiply = False
    elif 2.43 < x_pos < 2.55 and 3.05 < y_pos < 3.27:  # minus
        total2 = total1
        total1 = ""
        refresh()
        Minus = True
        Plus = False
        Multiply = False
    elif 2.65 < x_pos < 2.75 and 3.3 < y_pos < 3.6:
        total2 = total1
        total1 = ""
        refresh()
        Minus = False
        Plus = False
        Multiply = True
    elif 2.67 < x_pos < 2.78 and 2.3 < y_pos < 3.1:  # enter
        if Plus == True and total1 != "": #addition only works if the total1 variable isn't empty and if Plus == True
            total_number = eval(total1) + eval(total2)  #adds the 2 entered numbers
            total1 = str("{0:.2f}".format(total_number))  #formats the sum into 2 decimals
            total2 = ""
            refresh()                   #clears the cash register screen
            Plus = False                            #resets the variable back to false
        elif Minus == True and total1 != "": #subtracting only works if the total1 variable isn't empty and if Minus == True
            total_number = eval(total2) - eval(total1)   #subtracts the 2 entered numbers
            total1 = str("{0:.2f}".format(total_number))   #formats the difference into 2 decimals
            total2 = ""
            refresh()                  #clears the cash register screen
            Minus = False               #resets the variable back to false
        elif Multiply == True and total1 != "": #multiplication  only works if the total1 variable isn't empty and if Multiply == True
            total_number = eval(total1) * eval(total2) #multiplies the 2 entered numbers
            total1 = str("{0:.2f}".format(total_number))     #formats the product into 2 decimals
            total2 = ""                 #resets the total2 into a blank string
            refresh()                   #clears the cash register screen
            Multiply = False            #resets the variable back to false
        elif total1 != "": #inputing answer and checking it
            change_given = float(total1)
            total_change_given = total_change_given + change_given
            total1 = ""
            refresh()
        #checking if the entered value equals the price of the items
            if change_given == float(customer_price) - float(total_price) or 1:
                return True
            elif change_given != float(customer_price) - float(total_price):
                return False


#-------------------------------------------- life system and the animation for it/boss warning
def boss_walk():
    boss_walking = Image(Point(0, 4.8), 'images/boss walk.gif')
    boss_walking.draw(win)
    pygame.mixer.music.load('audios/footstep.wav')
    pygame.mixer.music.play()
    customer.undraw()
    for i in range(40):
        boss_walking.move(0.03, 0)
    boss_walking.undraw()
    pygame.mixer.music.stop()

    talkbox = Rectangle(Point(0, 0), Point(3, 2.2))
    talkbox.setWidth(5)
    talkbox.setFill('white')
    talkbox.draw(win)
    if life == 2:
        boss = Image(Point(0.75, 4.8), 'images/Boss counter version.gif')
        boss.draw(win)
        pygame.mixer.music.load('audios/mumbling.wav')
        pygame.mixer.music.play()
        boss_talk = Text(Point(1.5, 1), "Hey, it's okay to make mistakes. \n"
                                        "Try don't mess up again, okay?.")
        boss_talk.setSize(25)
        boss_talk.draw(win)
        if win.getMouse():
            pygame.mixer.music.stop()
            boss_talk.undraw()
            talkbox.undraw()
            boss.undraw()
            Walking_Boss_2 = Image(Point(0.75, 4.8), 'images/Walking_Boss_2.gif')
            Walking_Boss_2.draw(win)
            pygame.mixer.music.load('audios/footstep.wav')
            pygame.mixer.music.play()
            for i in range(275):
                Walking_Boss_2.move(-0.03, 0)
            pygame.mixer.music.stop()
            Walking_Boss_2.undraw()
            bgm()
    elif life == 1:
        boss = Image(Point(0.75, 4.8), 'images/boss_angry_1.gif')
        boss.draw(win)
        pygame.mixer.music.load('audios/strike 2.wav')
        pygame.mixer.music.play()
        boss_talk = Text(Point(1.5, 1),
                         "Hey, come on, this is your second time. \n"
                         "If you mess up again, I have to fire you.")
        boss_talk.setSize(25)
        boss_talk.draw(win)
        if win.getMouse():
            pygame.mixer.music.stop()
            boss_talk.undraw()
            talkbox.undraw()
            boss.undraw()
            Walking_Boss_2 = Image(Point(0.75, 4.8), 'images/Walking_Boss_2.gif')
            Walking_Boss_2.draw(win)
            pygame.mixer.music.load('audios/footstep.wav')
            pygame.mixer.music.play()
            for i in range(100):
                Walking_Boss_2.move(-0.02, 0)
            pygame.mixer.music.stop()
            Walking_Boss_2.undraw()
            bgm()
    elif life == 0:
        boss = Image(Point(0.75, 4.8), 'images/boss_angry_2.gif')
        boss.draw(win)
        pygame.mixer.music.load('audios/strike 3.wav')
        pygame.mixer.music.play()
        boss_talk = Text(Point(1.5, 1), "That's it, you are fired! \n"
                                        "Get out of my store!")
        boss_talk.setSize(25)
        boss_talk.draw(win)
        if win.getMouse():
            game_over()  # calls in function for the game over screen

# -------------------------------- creates a white box to clear up the register screen
def refresh():
    refresh_box = Rectangle(Point(1.829, 4), Point(2.768, 5.7))
    refresh_box.setWidth(2)
    refresh_box.setOutline('white')
    refresh_box.setFill('white')
    refresh_box.draw(win)
    Next = Text(Point(2.3, 4.8), total1)
    Next.setSize(30)
    Next.draw(win)


# draw all the buttons
def drawbuttons():

    button_image = Image(Point(0.2, 2.5), 'images/List_button.gif')
    button_image.draw(win)

    backspace_image = Image(Point(2.295, 2.42), 'images/backspace.gif')
    backspace_image.draw(win)

    Next = Text(Point(1.893, 2.8), 1)
    Next.setSize(13)
    Next.draw(win)

    Next = Text(Point(2.09, 2.8), 2)
    Next.setSize(13)
    Next.draw(win)

    Next = Text(Point(2.29, 2.8), 3)
    Next.setSize(13)
    Next.draw(win)

    Next = Text(Point(1.895, 3.15), 4)
    Next.setSize(13)
    Next.draw(win)

    Next = Text(Point(2.09, 3.15), 5)
    Next.setSize(13)
    Next.draw(win)

    Next = Text(Point(2.29, 3.15), 6)
    Next.setSize(13)
    Next.draw(win)

    Next = Text(Point(1.905, 3.5), 7)
    Next.setSize(13)
    Next.draw(win)

    Next = Text(Point(2.1, 3.5), 8)
    Next.setSize(13)
    Next.draw(win)

    Next = Text(Point(2.295, 3.5), 9)
    Next.setSize(13)
    Next.draw(win)

    Next = Text(Point(2.295, 3.5), 9)
    Next.setSize(13)
    Next.draw(win)

    Next = Text(Point(1.893, 2.43), 0)
    Next.setSize(13)
    Next.draw(win)

    Next = Text(Point(2.1, 2.55), ".")
    Next.setSize(25)
    Next.draw(win)

    Next = Text(Point(2.49, 2.8), "c")
    Next.setSize(8)
    Next.draw(win)
    Next = Text(Point(2.49, 2.7), "l")
    Next.setSize(8)
    Next.draw(win)
    Next = Text(Point(2.49, 2.6), "e")
    Next.setSize(8)
    Next.draw(win)
    Next = Text(Point(2.49, 2.5), "a")
    Next.setSize(8)
    Next.draw(win)
    Next = Text(Point(2.49, 2.4), "r")
    Next.setSize(8)
    Next.draw(win)

    Next = Text(Point(2.709, 3), "e")
    Next.setSize(10)
    Next.draw(win)
    Next = Text(Point(2.71, 2.85), "n")
    Next.setSize(10)
    Next.draw(win)
    Next = Text(Point(2.71, 2.7), "t")
    Next.setSize(10)
    Next.draw(win)
    Next = Text(Point(2.71, 2.55), "e")
    Next.setSize(10)
    Next.draw(win)
    Next = Text(Point(2.71, 2.4), "r")
    Next.setSize(10)
    Next.draw(win)

    Next = Text(Point(2.7, 3.4), "*")
    Next.setSize(15)
    Next.draw(win)

    Next = Text(Point(2.48, 3.5), "+")
    Next.setSize(13)
    Next.draw(win)

    Next = Text(Point(2.48, 3.17), "-")
    Next.setSize(18)
    Next.draw(win)

#------------------------------------------------ creates random items from the array for calculation
def item_random():
    global customer, number_of_items, item
    a = randrange(0, 19)
    b = randrange(1, 7)
    c = randrange(0, 6)
    total_price = 0
    b = randrange(1, 7)
    number_of_items = randrange(1, 5)
    x = 0.5
    customer = Image(Point(0.75, 5), customers[c])
    customer.draw(win)
    for i in range(number_of_items):
        a = randrange(0, 19)
        item = Image(Point(x, 2.4), item_name[a])   #calls in random item image from the list
        item.draw(win)
        sleep(0.5)
        total_price += item_price[a]            #adds the item called to the variable
        x += 0.2                                #moves to the right to prevent items overlapping
    customer_price = "{0:.2f}".format(total_price + b)
    return customer_price, "{0:.2f}".format(total_price)
#--------------------------------------------------------------------------------------------------------------


drawbuttons()
customers_served = 0
life = 3
Total = 0
Satisfied = 0
Unsatisfied = 0

while customers_served < 3:    #number of customers that has to be served to go to the next day
    global customer_price, total_price
    now = time.time()       #get current time
    time_limit = 60         #time limit
    band = Rectangle(Point(0.32, 1.75), Point(1.22, 3.1))       #clears item images from the last iteration
    band.setOutline('white')
    band.setFill('white')
    band.draw(win)
    customer_price, total_price = item_random()     #call in the item_random function to determine the prices
    talkbox.draw(win)
    customer_price = "{0:.2f}".format(float(customer_price))
    price_giving = Text(Point(1.5, 1), '$ ' + str(customer_price))   #the amount of money customer gives to the player
    float(customer_price)
    price_giving.setSize(25)
    price_giving.draw(win)
    while Running:
        checker = calc()            #calls in calc() and waits for its return statement
        if checker == True:         # if done correctly, customer_served goes up and finishes one iteration
            customers_served += 1
            now = time.time()
            price_giving.undraw()
            talkbox.undraw()
            customer.undraw()
            Satisfied += 1
            break
        elif checker == False:      # if done incorrectly, takes life away and calls in boss() function
            life -= 1
            boss_walk()
            now = time.time()
            price_giving.undraw()
            talkbox.undraw()
            Unsatisfied += 1
            break
        if time.time() - now > time_limit:     #if player goes over time limit takes a life away and calls in boss()
            life -= 1
            boss_walk()
            price_giving.undraw()
            talkbox.undraw()
            Unsatisfied += 1
            break

adamstory()
statistics()

Boss_event()       #transition animation
pygame.mixer.music.load('audios/TheFatRat - Unity.wav')
pygame.mixer.music.play()
drawbuttons()
customers_served = 0
life = 3
Total = 0
Satisfied = 0
Unsatisfied = 0

while customers_served < 4:
    now = time.time()
    time_limit = 50
    band = Rectangle(Point(0.32, 1.75), Point(1.22, 3.1))
    band.setOutline('white')
    band.setFill('white')
    band.draw(win)
    customer_price, total_price = item_random()
    talkbox.draw(win)
    customer_price = "{0:.2f}".format(float(customer_price))
    price_giving = Text(Point(1.5, 1), '$ ' + str(customer_price))
    float(customer_price)
    price_giving.setSize(25)
    price_giving.draw(win)
    while Running:
        checker = calc()
        if checker == True:
            customers_served += 1
            now = time.time()
            price_giving.undraw()
            talkbox.undraw()
            customer.undraw()
            Satisfied += 1
            break
        elif checker == False:
            life -= 1
            boss_walk()
            now = time.time()
            price_giving.undraw()
            talkbox.undraw()
            Unsatisfied += 1
            break
        if time.time() - now > time_limit:
            life -= 1
            boss_walk()
            price_giving.undraw()
            talkbox.undraw()
            Unsatisfied += 1
            break

x = -2
boss_walking = Image(Point(x, 4.8), 'images/boss walk.gif')
boss_walking.draw(win)
pygame.mixer.music.load('audios/footstep.wav')
pygame.mixer.music.play()

for i in range(275):
    boss_walking.move(0.01, 0)

boss_walking.undraw()
boss = Image(Point(0.75, 4.8), 'images/Boss counter version.gif')
boss.draw(win)
pygame.mixer.music.stop()

talk29 = Text(Point(1.5,1),'Well done!\n'
                           "That's all for today!")
talk29.setSize(25)
talkbox.draw(win)
talk29.draw(win)

if win.getMouse():
    talk29.undraw()
    talkbox.undraw()
    Day = Image(Point(2.55, 6.8), 'images/Two.gif')
    pygame.mixer.music.load('audios/TheFatRat - Unity.wav')
    pygame.mixer.music.play()
    statistics()

Day3()
pygame.mixer.music.load('audios/TheFatRat - Unity.wav')
pygame.mixer.music.play()
drawbuttons()
customers_served = 0
life = 3
Total = 0
Satisfied = 0
Unsatisfied = 0

while customers_served < 5:
    now = time.time()
    time_limit = 40
    band = Rectangle(Point(0.32, 1.75), Point(1.22, 3.1))
    band.setOutline('white')
    band.setFill('white')
    band.draw(win)
    customer_price, total_price = item_random()
    talkbox.draw(win)
    customer_price = "{0:.2f}".format(float(customer_price))
    price_giving = Text(Point(1.5, 1), '$ ' + str(customer_price))
    float(customer_price)
    price_giving.setSize(25)
    price_giving.draw(win)
    Total += 1
    while Running:
        checker = calc()
        if checker == True:
            customers_served += 1
            now = time.time()
            price_giving.undraw()
            talkbox.undraw()
            customer.undraw()
            Satisfied += 1
            if customers_served == 2:
                pygame.mixer.music.stop()
            break
        elif checker == False:
            life -= 1
            boss_walk()
            now = time.time()
            price_giving.undraw()
            talkbox.undraw()
            Unsatisfied +=1
            break
        if time.time() - now > time_limit:
            life -= 1
            boss_walk()
            price_giving.undraw()
            talkbox.undraw()
            Unsatisfied += 1
            break


Day = Image(Point(2.55, 6.8), 'images/Three.gif')
statistics()
presidentstory()
ending()