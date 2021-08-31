from graphics import *
from random import *
import pygame
import sys
from time import *
import time
from pygame.locals import *

#Variables that we needed to pull out to global
Window_Width, Window_Height = 800, 600
win = GraphWin('UJ Simulator', Window_Width, Window_Height)
win.setCoords(0, 0, 3, 8)
pygame.mixer.init()
New_Page = Rectangle(Point(0, 0), Point(3, 8))
New_Page.setOutline('white')
New_Page.setFill('white')
pygame.mixer.music.load('audios/bgmusic.wav')
talkbox = Rectangle(Point(0, 0), Point(3, 2.2))
talkbox.setWidth('5')
talkbox.setFill('white')

#Cash Register buttons(Rectangles).
def cash_register_buttons():
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

#An item list icon
def list():
    button_image = Image(Point(0.5, 1.5), 'images/List_button.gif')
    button_image.move(-0.3, 1)
    button_image.draw(win)

    button_rectangle = Rectangle(Point(0.45, 1.25), Point(0.55, 1.742))
    button_rectangle.move(-0.3, 1.0005)
    button_rectangle.draw(win)


# -----------------------------------------------------------------------------------------------------------------------
# For Cash Register
Running = True
total1 = ""
total2 = ""
total_number = 0
change_given = 0
total_change_given = 0
Plus = False
Minus = False
Multiply = False

# A refreshing box for typing numbers
def refresh():
    refresh_box = Rectangle(Point(1.829, 4), Point(2.768, 5.7))
    refresh_box.setWidth(2)
    refresh_box.setOutline('white')
    refresh_box.setFill('white')
    refresh_box.draw(win)
    Next = Text(Point(2.3, 4.8), total1)
    Next.setSize(30)
    Next.draw(win)


# -----------------------------------------------------------------------------------------------------------------------

# A function that ables a rectangle to work as a button.
def button(point, rectangle):
    ll = rectangle.getP1()  # assume p1 is ll (lower left)
    ur = rectangle.getP2()  # assume p2 is ur (upper right)

    return ll.getX() < point.getX() < ur.getX() and ll.getY() < point.getY() < ur.getY()


# The first function for the Start setup
def main():
    Title = Text(Point(1.5, 6), 'UJ SIMULATOR')
    Title.setSize(36)
    Title.setStyle('bold')
    Title.draw(win)

    Start = Text(Point(1.5, 2), 'START')
    Start.setSize(36)
    Start.draw(win)

    start = Rectangle(Point(0.75, 2.25), Point(2.25, 3.75))
    start.move(0, -1)
    start.draw(win)

    deco1 = Image(Point(0.6,7), 'images/Haribo.gif')
    deco1.draw(win)

    deco2 = Image(Point(2.6, 3), 'images/Coke.gif')
    deco2.draw(win)

    deco3 = Image(Point(0.1, 2), 'images/Toreta.gif')
    deco3.draw(win)

    deco4 = Image(Point(1.3, 5), 'images/twix.gif')
    deco4.draw(win)

    deco5 = Image(Point(0.4,3.5),'images/Lays_Lemon.gif')
    deco5.draw(win)

    deco6 = Image(Point(1.95, 0.6),'images/Dr.Pepper.gif')
    deco6.draw(win)

    deco7 = Image(Point(2.8, 7.4),'images/box.gif')
    deco7.draw(win)

    deco8 = Image(Point(1.75, 4),"images/hershey's.gif")
    deco8.draw(win)

    deco9 = Image(Point(2.2,5.6), 'images/Haribo.gif')
    deco9.draw(win)

    deco10 = Image(Point(0.66,1.25), 'images/Coke.gif')
    deco10.draw(win)

    deco11 = Image(Point(0.688, 5.56),'images/Toreta.gif')
    deco11.draw(win)

    deco12 = Image(Point(1,3), 'images/twix.gif')
    deco12.draw(win)

    deco13 = Image(Point(2.8,0.5),'images/Noodle.gif')
    deco13.draw(win)

    deco14 =Image(Point(3, 5), 'images/Cracker.gif')
    deco14.draw(win)

    deco15 = Image(Point(1.9,8), "images/Lay's_Pepper.gif")
    deco15.draw(win)


    # Music start
    pygame.mixer.music.play()

    return start


# Narrations before conversations with the boss start.
def START():
    Window_for_narration = Rectangle(Point(0, 0), Point(3, 8))
    Window_for_narration.setFill('white')
    Window_for_narration.setOutline('white')
    Window_for_narration.draw(win)

    y = -5
    Narration1 = Text(Point(1.525, y),
                      'In the year 20XX' '\n''\n'
                      'It has been many years since IGC and its universities have developed.' '\n''\n'
                      'There are significantly more students and has gained reputation for themselves.' '\n''\n'
                      'Despite their prosperity, however, the universities are in high tension.' '\n''\n'
                      'The presidents of the universities are in war to gain the boasting rights of''\n'
                      "having the 'best university'"'\n''\n'
                      'They have tried numerous tactics and strategies in the last several years.''\n''\n'
                      'But none of them was sucessful...''\n''\n''\n''\n'
                      'One day, the president of SUNY Korea has come up with a brilliant idea''\n'
                      'that will earn him the boasting rights.''\n''\n'
                      'It was...''\n''\n''\n''\n''\n''\n')
    Narration1.setSize(20)
    Narration1.draw(win)

    Narration2 = Text(Point(1.525, -1), 'TO TAKE OVER UJ CONVENIENCE STORE!!!!')
    Narration2.setSize(25)
    Narration2.setStyle('bold')
    Narration2.draw(win)

    for i in range(800):
        # the speed was 0.02
        Narration1.move(0, 0.02)

    for i in range(75):
        # the speed was 0.07
        Narration2.move(0, 0.07)

    Next_button = Rectangle(Point(2.4, 1.2), Point(2.9, 0.4))
    Next_button.setWidth(3)
    Next_button.setOutline('black')

    Next = Text(Point(2.65, 0.8), 'Click to Next...')
    Next.setSize(18)
    Next.draw(win)

    if button(win.getMouse(), Window_for_narration):
        Tutorial_start()

    return Window_for_narration


# This is a fuction for the setting slide that pop out after clicking SETTING button.


# Function for a button. Basically, This sets boundaries that we can click on.

#Narration that tells the goal of this game.
def Tutorial_start():
    Window_for_narration_1 = Rectangle(Point(0, 0), Point(3, 8))
    Window_for_narration_1.setOutline('white')
    Window_for_narration_1.setFill('white')
    Window_for_narration_1.draw(win)

    Proceed = Text(Point(2.65, 0.8), 'Click to Proceed...')
    Proceed.setSize(18)
    Proceed.draw(win)

    if win.getMouse():
        narration_1 = Text(Point(1.5, 7), 'You!')
        narration_1.draw(win)
        x = 5
        while x < 37:
            narration_1.setSize(x)
            x = x + 1

        for i in range(5):
            narration_1.move(-0.01, 0)
            narration_1.move(0.01, 0)
            narration_1.move(-0.01, 0.01)
            narration_1.move(0.01, -0.01)
            narration_1.move(0.01, 0)
            narration_1.move(-0.01, 0)
            narration_1.move(0.01, -0.01)
            narration_1.move(-0.01, 0.01)

    if win.getMouse():
        narration_2 = Text(Point(1.5, 0), 'As an infiltrated spy of the president,')
        narration_2.setSize(25)
        narration_2.draw(win)

        for i in range(22):
            narration_2.move(0, 0.25)

    if win.getMouse():
        narration_3 = Text(Point(1.5, 0), 'You can help the president of SUNY Korea \n'
                                          'to take over UJ,')
        narration_3.setSize(25)
        narration_3.draw(win)

        # this goes to Point(1.5, 4.5)
        for i in range(18):
            narration_3.move(0, 0.25)

    if win.getMouse():
        narration_4 = Text(Point(1.5, 3.5), 'OR')
        narration_4.draw(win)
        x = 5
        while x < 37:
            narration_4.setSize(x)
            x = x + 1

    if win.getMouse():
        Proceed.undraw()
        Next = Text(Point(2.65, 0.8), 'Click to Next...')
        Next.setSize(18)
        Next.draw(win)
        narration_5 = Text(Point(1.5, 0), 'You can betray the president and \n'
                                          "become the uj owner's side.")
        narration_5.setSize(25)
        narration_5.draw(win)

        for i in range(12):
            narration_5.move(0, 0.2)

    if win.getMouse():
        Conversation_with_UJ_Owner()
        pygame.mixer.music.stop()

    return Window_for_narration_1


#Conversation start
def Conversation_with_UJ_Owner():
    pygame.mixer.music.load('audios/mumbling.wav')
    pygame.mixer.music.play()

    Window_for_Conversation = Rectangle(Point(0, 0), Point(3, 8))
    Window_for_Conversation.setFill('white')
    Window_for_Conversation.setOutline('white')
    Window_for_Conversation.draw(win)

    UJ_Owner = Image(Point(1.5, 3.8), 'images/UJ Owner-2.gif')
    UJ_Owner.draw(win)

    mouth = Oval(Point(1.4, 4.75), Point(1.6, 4.45))
    mouth.setFill('white')
    mouth.setOutline('white')

    talkbox = Rectangle(Point(0, 0), Point(3, 2.2))
    talkbox.setWidth('5')
    talkbox.setFill('white')
    talkbox.draw(win)

    talk1 = Text(Point(1.5, 1), "Hello")
    talk1.setSize(25)
    talk1.draw(win)

    for i in range(5):
        mouth.draw(win)
        sleep(0.25)
        mouth.undraw()
        sleep(0.25)

    if win.getMouse():
        pygame.mixer.music.stop()
        Conversation_with_UJ_Owner2()


#Conversation continue
def Conversation_with_UJ_Owner2():
    pygame.mixer.music.play()

    Window_for_Conversation = Rectangle(Point(0, 0), Point(3, 8))
    Window_for_Conversation.setFill('white')
    Window_for_Conversation.setOutline('white')
    Window_for_Conversation.draw(win)

    UJ_Owner = Image(Point(1.5, 3.8), 'images/UJ Owner-2.gif')
    UJ_Owner.draw(win)

    mouth = Oval(Point(1.4, 4.75), Point(1.6, 4.45))
    mouth.setFill('white')
    mouth.setOutline('white')

    talkbox = Rectangle(Point(0, 0), Point(3, 2.2))
    talkbox.setWidth('5')
    talkbox.setFill('white')
    talkbox.draw(win)

    talk1 = Text(Point(1.5, 1), "I'm the owner of the UJ convenient store")
    talk1.setSize(25)
    talk1.draw(win)

    for i in range(5):
        mouth.draw(win)
        sleep(0.2)
        mouth.undraw()
        sleep(0.2)

    if win.getMouse():
        pygame.mixer.music.stop()
        Conversation_with_UJ_Owner3()

#Conversation continue.
def Conversation_with_UJ_Owner3():
    pygame.mixer.music.play()

    Window_for_Conversation = Rectangle(Point(0, 0), Point(3, 8))
    Window_for_Conversation.setFill('white')
    Window_for_Conversation.setOutline('white')
    Window_for_Conversation.draw(win)

    UJ_Owner = Image(Point(1.5, 3.8), 'images/UJ Owner-2.gif')
    UJ_Owner.draw(win)

    mouth = Oval(Point(1.4, 4.75), Point(1.6, 4.45))
    mouth.setFill('white')
    mouth.setOutline('white')

    talkbox = Rectangle(Point(0, 0), Point(3, 2.2))
    talkbox.setWidth(5)
    talkbox.setFill('white')
    talkbox.draw(win)

    talk1 = Text(Point(1.5, 1), 'So I guess you are the work study student \n'
                                'who were going to be here, right?')
    talk1.setSize(25)
    talk1.draw(win)

    for i in range(5):
        mouth.draw(win)
        sleep(0.2)
        mouth.undraw()
        sleep(0.2)

    if win.getMouse():
        talk1.undraw()

    talk2 = Text(Point(1.5, 1), 'Could you tell me your name?')
    talk2.setSize(25)
    talk2.draw(win)

    if win.getMouse():
        pygame.mixer.music.stop()
        Myname()


#Conversation pause, and then user input name.
def Myname():
    global name
    Window_for_Conversation = Rectangle(Point(0, 0), Point(3, 8))
    Window_for_Conversation.setFill('white')
    Window_for_Conversation.setOutline('white')
    Window_for_Conversation.draw(win)

    UJ_Owner = Image(Point(1.5, 3.8), 'images/UJ Owner-2.gif')
    UJ_Owner.draw(win)

    talkbox = Rectangle(Point(0, 0), Point(3, 2.2))
    talkbox.setWidth(5)
    talkbox.setFill('white')
    talkbox.draw(win)

    mouth = Oval(Point(1.4, 4.75), Point(1.6, 4.45))
    mouth.setFill('white')
    mouth.setOutline('white')

    name_type = Entry(Point(1.2, 1), 20)
    name_type.setText('Type in your name: ')
    name_type.setSize(25)
    name_type.draw(win)

    Enter_button = Rectangle(Point(2.3, 0), Point(3, 2.2))
    Enter_button.setWidth(5)
    Enter_button.setFill('white')
    Enter_button.draw(win)

    Enter_Center = Enter_button.getCenter()
    Enter = Text(Enter_Center, 'Enter')
    Enter.setSize(20)
    Enter.setStyle('bold')
    Enter.draw(win)

    while True:
        if button(win.getMouse(), Enter_button):
            name_type.undraw()
            Enter_button.undraw()
            Enter.undraw()
            break

    pygame.mixer.music.play()

    name = name_type.getText()

    talk2 = Text(Point(0.7, 1), 'Okydoky')
    talk2.setSize(25)
    talk2.draw(win)

    talk3 = Text(Point(1.5, 1), name)
    talk3.setSize(25)
    talk3.setFace('courier')
    talk3.draw(win)

    talk4 = Text(Point(2.3, 1), 'Follow me.')
    talk4.setSize(25)
    talk4.draw(win)

    for i in range(5):
        mouth.draw(win)
        sleep(0.2)
        mouth.undraw()
        sleep(0.2)

    if win.getMouse():
        Tutorial()
        pygame.mixer.music.stop()


#Tutorial starts
def Tutorial():
    global total_change_given, total1, total2, total1, Multiply, total1, total2, Minus, total2, total1, Plus, total1, total1, total1, total1, total1, total1, total1, total1, total1, total1, total1, total1, total1, total1, total1, Running

    UJ_Background = Image(Point(1.5, 4), 'images/UJ Background.gif')
    UJ_Background.draw(win)

    # ------------------------------------------------------------------------------------------|
    # this is where list button is.
    button_image = Image(Point(0.5, 1.5), 'images/List_button.gif')
    button_image.move(-0.3, 1)
    button_image.draw(win)

    button_rectangle = Rectangle(Point(0.45, 1.25), Point(0.55, 1.742))
    button_rectangle.move(-0.3, 1.0005)
    button_rectangle.draw(win)
    # ------------------------------------------------------------------------------------------|
    # this is where cash register buttons are.
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

    # ----------------------------------------------------------------------------------------------------|
    talkbox.draw(win)

    talk1 = Text(Point(1.5, 1), 'Alright. I guess you are ready to work!')
    talk1.setSize(25)
    talk1.draw(win)

    if win.getMouse():
        talk1.undraw()

    talk2 = Text(Point(1.5, 1), "Now, I'll teach you what to do.")
    talk2.setSize(25)
    talk2.draw(win)

    if win.getMouse():
        talk2.undraw()

    talk3 = Text(Point(1.5, 1), 'Do you see that small piece of paper \n'
                                'on the left side of the desk?')
    talk3.setSize(25)
    talk3.draw(win)

    if win.getMouse():
        talk3.undraw()

    talk4 = Text(Point(1.5, 1), "It's a list of items in our store")
    talk4.setSize(25)
    talk4.draw(win)

    if win.getMouse():
        talk4.undraw()

    talk5 = Text(Point(1.5, 1), 'You can refer to the list if you do not know the price of items.')
    talk5.setSize(25)
    talk5.draw(win)

    if win.getMouse():
        talk5.undraw()
        talkbox.undraw()
    # ------------------------------------------------------------------------------------------------------------------|
    # this is where the list button works

    down = Image(Point(0.2, 3.8), 'images/down_arrow.gif')

    def lists_button():
        global instruction2, button_lists
        a = 1
        instruction1 = Text(Point(0.2, 4.4), 'Click the list!')
        instruction1.setSize(15)
        instruction1.draw(win)

        button_close = Rectangle(Point(2.1, 6.3), Point(2.235, 6.75))
        button_close.move(-0.6, 0.5)
        button_lists = Image(Point(1.5, 4), 'images/Price_list.gif')
        button_lists.move(-0.6, 0.5)

        instruction2 = Text(Point(0.2, 4.4), 'Click again \n'
                                             'to proceed.')
        instruction2.setSize(15)

        down.draw(win)
        while a < 2:
            while True:
                clickPoint = win.getMouse()

                if button(clickPoint, button_rectangle):
                    button_close.draw(win)
                    button_lists.draw(win)
                    if not button(clickPoint, button_rectangle):
                        None

                elif button(clickPoint, button_close):
                    button_close.undraw()
                    button_lists.undraw()
                    instruction1.undraw()
                    a += 1
                    if a == 2:
                        instruction2.draw(win)
                        down.undraw()
                        while a > 2:
                            instruction2.undraw()
                            break

                elif clickPoint:
                    button_close.undraw()
                    button_lists.undraw()
                    instruction2.undraw()
                    instruction2.undraw()
                    break

    lists_button()
    # ------------------------------------------------------------------------------------------------------------------|
    band = Rectangle(Point(0, 4.1), Point(0.4, 4.7))
    band.setOutline('white')
    band.setFill('white')
    band.draw(win)

    talkbox.draw(win)

    talk6 = Text(Point(1.5, 1), 'Well done!')
    talk6.setSize(25)
    talk6.draw(win)

    if win.getMouse():
        talk6.undraw()

    talk7 = Text(Point(1.5, 1), 'Ok, now, do you see the monitor on the desk?')
    talk7.setSize(25)
    talk7.draw(win)

    if win.getMouse():
        talk7.undraw()

    talk8 = Text(Point(1.5, 1), "That's cash register.")
    talk8.setSize(25)
    talk8.draw(win)

    if win.getMouse():
        talk8.undraw()

    talk8_1 = Text(Point(1.5, 1), 'You will use this to calculate how much each item is.')
    talk8_1.setSize(25)
    talk8_1.draw(win)

    if win.getMouse():
        talk8_1.undraw()

    # Where talk 9 and cutted ones

    talk10 = Text(Point(1.5, 1), 'I guess it will help you a lot.')
    talk10.setSize(25)
    talk10.draw(win)

    if win.getMouse():
        pygame.mixer.music.load('audios/hmm.wav')
        pygame.mixer.music.play()
        talk10.undraw()

    talk11 = Text(Point(1.5, 1), 'Hmm...')
    talk11.setSize(25)
    talk11.draw(win)

    if win.getMouse():
        talk11.undraw()
        talkbox.undraw()

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
    talk12 = Text(Point(1.5, 1), 'OK now, I will teach you how to deal with customers.')
    talk12.setSize(25)
    talk12.draw(win)

    if win.getMouse():
        talk12.undraw()

    talk13 = Text(Point(1.5, 1), 'The customers will bring items like this')
    talk13.setSize(25)
    talk13.draw(win)

    if win.getMouse():
        talk13.undraw()
        talkbox.undraw()

    Fat_Monster = Image(Point(0.8, 2.6), 'images/Fat_Monster.gif')
    Fat_Monster.draw(win)

    sleep(1)

    Slim_Monster = Image(Point(1, 2.5), 'images/Slim_Monster.gif')
    Slim_Monster.draw(win)

    sleep(1)

    talkbox.draw(win)
    talk14 = Text(Point(1.5, 1), 'Then they will tell you how much they are going to give you.')
    talk14.setSize(25)
    talk14.draw(win)

    if win.getMouse():
        talk14.undraw()

    talk15 = Text(Point(1.5, 1), "For now, Let's say the fat one is $2.5, and the slim one is $1.8.")
    talk15.setSize(25)
    talk15.draw(win)

    if win.getMouse():
        talk15.undraw()

    talk15_1 = Text(Point(1.5, 1), "And let's say I gave you $5 to pay.")
    talk15_1.setSize(25)
    talk15_1.draw(win)

    if win.getMouse():
        talk15_1.undraw()

    talk16 = Text(Point(1.5, 1), 'You need to use your cash register to calculate.')
    talk16.setSize(25)
    talk16.draw(win)

    if win.getMouse():
        talk16.undraw()

    talk17 = Text(Point(1.5, 1), 'Use it to calculate the drinks!')
    talk17.setSize(25)
    talk17.draw(win)

    if win.getMouse():
        talk17.undraw()
        talkbox.undraw()

    instruction = Text(Point(2.7, 7), 'Try to use cash register!')
    instruction.setSize(15)
    instruction.draw(win)

    down = Image(Point(2.7, 6.5), 'images/down_arrow.gif')
    down.draw(win)

    if win.getMouse():
        instruction.undraw()
        down.undraw()

    while Running:
        point = win.getMouse()
        x_pos = point.getX()
        y_pos = point.getY()

        if 1.84 < x_pos < 1.96 and 2.7 < y_pos < 2.9:
            total1 = total1 + "1"
            refresh()

        elif 2.03 < x_pos < 2.16 and 2.5 < y_pos < 3:
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
            if Plus == True:
                total_number = eval(total1) + eval(total2)
                total1 = str(total_number)
                total2 = ""
                refresh()
                Plus = False
            elif Minus == True:
                total_number = eval(total2) - eval(total1)
                total1 = str(total_number)
                total2 = ""
                refresh()
                Minus = False
            elif Multiply == True:
                total_number = eval(total1) * eval(total2)
                total1 = str(total_number)
                total2 = ""
                refresh()
                Multiply = False
            else:
                change_given = eval(total1)
                total_change_given = total_change_given + change_given
                print(change_given)
                print(total_change_given)
                total1 = ""
                refresh()
                if change_given == 0.7:
                    Fat_Monster.undraw()
                    sleep(1)
                    Slim_Monster.undraw()
                    Running = False
                else:
                    talkbox.draw(win)
                    NoNo = Text(Point(1.5, 1), "That's wrong value!! Try again!")
                    NoNo.setSize(25)
                    NoNo.draw(win)
                    win.getMouse()
                    talkbox.undraw()
                    NoNo.undraw()
    talkbox.draw(win)

    talk18 = Text(Point(1.5, 1), "That's right!!!")
    talk18.setSize(25)
    talk18.draw(win)

    if win.getMouse():
        talk18.undraw()

    talk19 = Text(Point(1.5, 1), 'Now you are really really really ready!!')
    talk19.setSize(25)
    talk19.draw(win)

    if win.getMouse():
        talk19.undraw()

    talk20 = Text(Point(1.5, 1), 'See you tomorrow morning at 9:00 A.M.')
    talk20.setSize(25)
    talk20.draw(win)

    if win.getMouse():
        boss.undraw()
        talk20.undraw()
        talkbox.undraw()

    Smiling_Boss = Image(Point(0.75, 4.8), 'images/Smiling_Boss.gif')
    Smiling_Boss.draw(win)
    sleep(1.5)

    Walking_Boss_2 = Image(Point(0.75, 4.8), 'images/Walking_Boss_2.gif')
    Walking_Boss_2.draw(win)
    Smiling_Boss.undraw()
    pygame.mixer.music.load('audios/footstep.wav')
    pygame.mixer.music.play()

    for i in range(275):
        Walking_Boss_2.move(-0.01, 0)

    pygame.mixer.music.stop()

    r = 255
    g = 255
    b = 255

    Window_for_Tutorial = Rectangle(Point(0, 0), Point(3, 8))
    Window_for_Tutorial.draw(win)

    for i in range(100):
        Window_for_Tutorial.setOutline(color_rgb(r, g, b))
        Window_for_Tutorial.setFill(color_rgb(r, g, b))
        r -= 7
        g -= 7
        b -= 7

        if r < 0 and g < 0 and b < 0:
            break
    if win.getMouse():
        Day()


#intersection between real game and turtorial
def Day():
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
        r += 7
        g += 7
        b += 7

        if r > 255 and g > 255 and b > 255:
            color_change = 'white'
            break

    Day1 = Text(Point(x, 4.5), 'Day 1')
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
    for i in range(5):
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
    talk21 = Text(Point(1.5,1),'OK ' + name + ', are you ready?')
    talk21.setSize(25)
    talk21.draw(win)

    if win.getMouse():
        talk21.undraw()

    talk22 = Text(Point(1.5,1), 'Your First day man!')
    talk22.setSize(25)
    talk22.draw(win)

    if win.getMouse():
        talk22.undraw()

    talk23 = Text(Point(1.5,1), 'Good luck')
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

# This is where actually the whole python codes starts. Form starting this function, all the others work
# like chain.
start = main()

while True:
    if button(win.getMouse(), start):
        Window_for_narration = START()
        break

win.close()
win.close()

#This is where we import another new window for gaming.
import items
exec('items')