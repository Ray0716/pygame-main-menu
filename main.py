#import pygame
#from pygame import mixer
#import os
from data import *
import random
#import time
#import image
#import sys
#import math

#IMPORTANT NOTE  ; ALL VARS ARE STORED IN THE DATA.PY FILE
# DEVELOPMENT START - FEB 6 2022
#
# Contributors :
#Ray Tang  Github - Ray861
#
#
#
#
#
#tasks:
#
# make credits menu
#
# prototype animation for mmenu
# prototype dialogue chain structure (should we use OOP ?)
#
#fix glitch effect when play pressed
#
#

pygame.init()
pygame.font.init()
pygame.mixer.init()
#--------------------------

#channel 0 is bckg sound
#channel 1 is click and other

channel0 = pygame.mixer.Channel(0) # argument must be int
channel1 = pygame.mixer.Channel(1)

vol = 1.0

while running:

    #main menu loop
    screen.fill((0, 0, 0))

    mouse_pos = pygame.mouse.get_pos()  # Get mouse position
    print("X : ", str(mouse_pos[0]), "Y : ",str(mouse_pos[1]))  # printing mouse position, this is just for testing purposes

    while mainmenu:
        screen.blit(mainmenu_surf, (0, 0))

        #background ambience


        #if sound is True:
        #channel0.play(low_hum, loops = 1)
        if sound is True:
            low_hum.play(1)
        #sound = False



        #titleborderlime

        pygame.draw.rect(screen, (100, 100, 100), pygame.Rect(27, 156, 560, 3))

        mainmenu_surf.fill((0, 5, 0)) #fills the background color
        #displays the text for menu
        mainmenu_surf.blit(titletext, (60, 50))        #game title
        mainmenu_surf.blit(playtext, (80, 200))        #play button display
        mainmenu_surf.blit(settingstext, (80, 260))    #settings button
        mainmenu_surf.blit(credittext, (80, 320))      #credits button
        mainmenu_surf.blit(quittext_main_menu, (80, 380))        #quit button


        #glitch amount and effect
        glitch(50, 288, 60, 141, 150, random.randint(25, 60))

        mouse_pos = pygame.mouse.get_pos() # Get mouse position
        print("X : ", str(mouse_pos[0]), "Y : ",str(mouse_pos[1]))  # printing mouse position, this is just for testing purposes


        #displaying the arrows if mouse is hovering
        if is_pos_inside(71, 158, 186, 242, mouse_pos):  # if the mouse is inside the play button:
            mainmenu_surf.blit(left_arrow, (300, 213))
            glitch(71, 158, 196, 232, 150, 15)      #glitch effect when mouse hovers
            channel1.play(static)


        if is_pos_inside(71, 228, 256, 306, mouse_pos):  # if the mouse is clicked inside the settings button:
            mainmenu_surf.blit(left_arrow, (300, 275))
            glitch(71, 228, 266, 296, 150, 15) #glitch effect when mouse hovers


        if is_pos_inside(71, 208, 310, 355, mouse_pos):  # if the mouse is clicked inside the credits button:
            mainmenu_surf.blit(left_arrow, (300, 331))
            glitch(71, 208, 320, 345, 150, 15)#glitch effect when mouse hovers


        if is_pos_inside(71, 150, 376, 418, mouse_pos):  # if the mouse is clicked inside the quits button:
            mainmenu_surf.blit(left_arrow, (300, 392))
            glitch(71, 150, 386, 408, 150, 15)#glitch effect when mouse hovers




        for event in pygame.event.get(): #listen for events

            if event.type == pygame.QUIT: # if quit then window closes
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONUP: #if the mouse is clicked...
                if is_pos_inside(71, 158, 191, 237, mouse_pos): #if the mouse is clicked inside the play button:
                    print("GAME HAS STARTED")
                    if sound is True:
                        channel1.play(big_button_sound)
                        channel1.play(glitch_out)

                    for x in range(30):
                        screen.blit(mainmenu_surf, (0, 0))  #when play pressed we make it glitch out
                        if x >0 and x<10:
                            glitch(0, 930, 0, 650, 200, 7)#these are for the glitch effect to increase
                            glitch(0, 930, 0, 650, 200, 7)#in intensity as time goes on

                        if x > 11 and x < 20:
                            glitch(0, 930, 0, 650, 200, 7)
                            glitch(0, 930, 0, 650, 200, 7)
                            glitch(0, 930, 0, 650, 200, 7)
                            glitch(0, 930, 0, 650, 200, 7)

                        if x > 21 and x <30:
                            glitch(0, 930, 0, 650, 200, 7)
                            glitch(0, 930, 0, 650, 200, 7)
                            glitch(0, 930, 0, 650, 200, 7)
                            glitch(0, 930, 0, 650, 200, 7)
                            glitch(0, 930, 0, 650, 200, 7)
                            glitch(0, 930, 0, 650, 200, 7)
                            glitch(0, 930, 0, 650, 200, 7)
                            glitch(0, 930, 0, 650, 200, 7)
                            glitch(0, 930, 0, 650, 200, 7)
                            glitch(0, 930, 0, 650, 200, 7)
                            glitch(0, 930, 0, 650, 200, 7)
                            glitch(0, 930, 0, 650, 200, 7)
                            glitch(0, 930, 0, 650, 200, 7)
                            glitch(0, 930, 0, 650, 200, 7)
                            glitch(0, 930, 0, 650, 200, 7)
                            glitch(0, 930, 0, 650, 200, 7)


                        time.sleep(1/30)

                        pygame.display.update()
                        clock.tick(random.randint(24, 75))
                        screen.fill((0,0,0))

                    game_playing = True

                    mainmenu = False

                if is_pos_inside(71, 228, 261, 302, mouse_pos): #if the mouse is clicked inside the settings button:
                    print("settingsmenu")
                    settings_menu = True
                    mainmenu = False
                    if sound is True:
                        channel1.play(open_menu_sound)

                if is_pos_inside(71, 208, 315, 351, mouse_pos): #if the mouse is clicked inside the credits button:
                    print("creditsmenu")

                    if sound is True:
                        channel1.play(open_menu_sound)

                    credits_menu = True
                    mainmenu = False

                if is_pos_inside(71, 150, 381, 415, mouse_pos): #if the mouse is clicked inside the quits button:
                    print("quitmenu")
                    mainmenu = False
                    quitmenu = True
                    if sound is True:
                        channel1.play(open_menu_sound)


                    what_menu_quit = "main"


        pygame.display.update()
        clock.tick(24)

    #-----------------------------------------------------------------

    while quitmenu:
        mouse_pos = pygame.mouse.get_pos()
        print("X : ", str(mouse_pos[0]), "Y : ",str(mouse_pos[1]))  # printing mouse position, this is just for testing purposes

        screen.blit(quitmenu_surf, (325, 150))  # theres a seperate surface for the quit menu
        quitmenu_surf.fill((255, 255, 255))
        pygame.draw.rect(quitmenu_surf, (0, 0, 0), pygame.Rect(2, 2, 296, 346))


        if is_pos_inside(356, 408, 298, 351, mouse_pos): # if mouse inside yes and no buttons
            screen.blit(left_arrow, (431, 309))
            glitch(356, 408, 298, 351, 90, 15)

        if is_pos_inside(357, 398, 358, 387, mouse_pos):
            screen.blit(left_arrow, (431, 370))
            glitch(357, 398, 358, 387, 90, 15)


        for event in pygame.event.get(): #listen for events

            if event.type == pygame.QUIT: # if quit then window closes
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONUP:

                if sound is True:
                    channel1.play(click)
                if is_pos_inside(356, 408, 298, 351, mouse_pos): #if click on yes :
                    pygame.quit()
                    quit()
                if is_pos_inside(357, 398, 358, 387, mouse_pos) or is_pos_inside(596, 618, 156, 179, mouse_pos):
                    quitmenu = False
                    if what_menu_quit == "main":
                        mainmenu = True
                    print("cancelquit")




        screen.blit(quit_text, (350, 210)) #text saying are you sure ?
        screen.blit(yes, (360, 300))    #text saying yes
        screen.blit(no, (363, 360))     #"no " text

        #x button
        screen.blit(x_button, (594, 155))

        pygame.display.update()
        clock.tick(24)



    #Setings menu

    while settings_menu:
        screen.blit(settings_surf, (190, 80))
        mouse_pos = pygame.mouse.get_pos()

        print("X : ", str(mouse_pos[0]), "Y : ",str(mouse_pos[1]))  # printing mouse position, this is just for testing purposes

        settings_surf.fill((255, 255, 255))
        pygame.draw.rect(settings_surf, (0, 0, 0), pygame.Rect(2, 2, 546, 496))



        if sound is True:
            screen.blit(left_arrow, (319, 270))
            #vol = 0
            if settings_menu_quit == "main":
                low_hum.play(1)
        else:
            screen.blit(left_arrow, (319, 297))
            pygame.mixer.Sound.stop(low_hum)
            vol = 1




        if fullscreen is True:
            screen.blit(left_arrow, (319, 419))
        else:
            screen.blit(left_arrow, (319, 447))



        for event in pygame.event.get(): #listen for events

            if event.type == pygame.QUIT: # if quit then window closes
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONUP:
                if sound is True:
                    channel1.play(click)
                if is_pos_inside(711, 736, 85, 109, mouse_pos): #if click the x button
                    settings_menu = False
                    if settings_menu_quit == "main":
                        mainmenu = True

                if is_pos_inside(255, 289, 261, 283, mouse_pos):  # if the mouse is clicked on on button for sound
                    sound = True
                if is_pos_inside(255, 303, 287, 316, mouse_pos):  # if mouse is clicked on off button for sound
                    sound = False


                if is_pos_inside(253, 290, 408, 432, mouse_pos):  # if the mouse is clicked on on button for fullscr
                    fullscreen = True
                    screen = pygame.display.set_mode((930, 650), pygame.FULLSCREEN)
                if is_pos_inside(252, 304, 435, 466, mouse_pos):  # if mouse is clicked on off button for scr
                    fullscreen = False
                    screen = pygame.display.set_mode((930, 650))


        screen.blit(x_button, (710, 83))

        screen.blit(settingstext_menu, (225, 95))

        screen.blit(sound_txt, (227, 204))
        screen.blit(on_txt, (257, 256))
        screen.blit(off_txt, (257, 286))

        screen.blit(fullscreen_txt, (227, 350))
        screen.blit(on_txt, (257, 402))
        screen.blit(off_txt, (257, 432))

        pygame.display.update()
        clock.tick(24)


    while credits_menu:
        screen.blit(credits_surf, (190, 80))
        mouse_pos = pygame.mouse.get_pos()

        print("X : ", str(mouse_pos[0]), "Y : ",str(mouse_pos[1]))  # printing mouse position, this is just for testing purposes

        credits_surf.fill((255, 255, 255))
        pygame.draw.rect(credits_surf, (0, 0, 0), pygame.Rect(2, 2, 546, 496))

        for event in pygame.event.get(): #listen for events

            if event.type == pygame.QUIT: # if quit then window closes
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONUP:
                if sound is True:
                    channel1.play(click)
                if is_pos_inside(711, 736, 85, 109, mouse_pos): #if click the x button
                    credits_menu = False
                    mainmenu = True

        screen.blit(credit_txt, (225, 95))
        screen.blit(x_button, (710, 83))
        pygame.display.update()
        clock.tick(24)


    #main game loop VERY IMPORTANT

    while game_playing:
        screen.fill((100, 100, 100))#fill bcgk color(r, g, b)

        for event in pygame.event.get(): #listen for events

            if event.type == pygame.QUIT: # if quit then window closes
                pygame.quit()
                quit()


        pygame.display.update()
        clock.tick(24)


    pygame.display.update()
    clock.tick(24)












