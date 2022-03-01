import pygame
from pygame import mixer
import os
import random
import time
#import image
#import sys
#import math

#testing for class functions for text hope this works

#class text("textinput")





from pygame import font

pygame.font.init()
pygame.init()

def load(path):  #-LOADS DIRECT FILE PATH FOR IMAGES AND OTHER FILES BECAUSE PYGAME JUST DOESNRT COOPERATE
    return os.path.join(os.path.dirname(__file__), path)

def glitch(x1, x2, y1, y2, x_limit, chance):
    whichrect = random.randint(1, chance)


    rect1 = pygame.Rect(random.randrange(x1, x2), random.randrange(y1, y2), random.randrange(15, x_limit), random.randrange(1, 15))
    rect2 = pygame.Rect(random.randrange(x1, x2), random.randrange(y1, y2), random.randrange(15, x_limit), random.randrange(1, 15))
    rect3 = pygame.Rect(random.randrange(x1, x2), random.randrange(y1, y2), random.randrange(15, x_limit), random.randrange(1, 15))


    #since there are 7 possible combos of yes/no for 3 values we can use random
    #to decide which rect we blit

    #rect1 is red, rect2 is green, rect3 is blu

    #          1st val - rect1
    #          2nd val - rect2
    #          3rd val - rect3

    if whichrect == 1:# [1] [0] [0]
        pygame.draw.rect(screen, (255, 0, 0), rect1)

    if whichrect == 2:# [0] [1] [0]
        pygame.draw.rect(screen, (0, 255, 0), rect2)

    if whichrect == 3:# [0] [0] [1]
        pygame.draw.rect(screen, (0, 0, 255), rect3)

    if whichrect == 4:# [1] [1] [0]
        pygame.draw.rect(screen, (255, 0, 0), rect1)
        pygame.draw.rect(screen, (0, 255, 0), rect2)

    if whichrect == 5:# [0] [1] [1]
        pygame.draw.rect(screen, (0, 255, 0), rect2)
        pygame.draw.rect(screen, (0, 0, 255), rect3)

    if whichrect == 6:# [1] [0] [1]
        pygame.draw.rect(screen, (255, 0, 0), rect1)
        pygame.draw.rect(screen, (0, 0, 255), rect3)

    if whichrect == 7:# [1] [1] [1]
        pygame.draw.rect(screen, (255, 0, 0), rect1)
        pygame.draw.rect(screen, (0, 255, 0), rect2)
        pygame.draw.rect(screen, (0, 0, 255), rect3)

def is_pos_inside(x1, x2, y1, y2, pos):  #IF A POINT IS INSIDE AN AREA OF COORDS
    if (pos[0] >= x1 and pos[0] <= x2) and (pos[1] >= y1 and pos[1] <= y2):
        return True
    else:
        return False

#heres how the above function's paraneters work
#
#   1st x value (x1)           2nd x value(x2)  the x values determine the width of the rect area
#   <---------------------------------------->
#
#                                             ^ 1st y val (y1)
#                                             |
#                                             |        the y vals determine the height of the area
#                                             |
#                                             | 2nd y val (y2)
#
#

fullscreen = False

#--------------------------------------------------------------------------SURFACES
mainmenu_surf = pygame.Surface((930, 650))
quitmenu_surf = pygame.Surface((300, 350))
settings_surf = pygame.Surface((550, 500))
credits_surf = pygame.Surface((550, 500))


#--------------------------------------------------------------------------MAIN SCREEN

if fullscreen == True:
    screen = pygame.display.set_mode((930,650), pygame.FULLSCREEN)
else:
    screen = pygame.display.set_mode((930, 650))
clock = pygame.time.Clock()


pygame.display.set_caption("Game Title")   #lets come up with a better title later...
icon = pygame.image.load(load("generic_currency.png"))
pygame.display.set_icon(icon)
what_menu_quit = "main"
settings_menu_quit = "main"
#this variable is for when we quit and we cancel quit we know what menu to go back to

#--------------------------------------------------------------------------MENU VARIABLES

mainmenu = True
quitmenu = False
settings_menu = False
credits_menu = False

sound = True
running = True
game_playing = False


quitmenu_count = 0 #these count vars are for the animations so that they dont play on loop in the "while" lop

#--------------------------------------------------------------------------FONTS


title = pygame.font.Font(load("JetBrainsMono-Medium.ttf"), 75)
sml = pygame.font.Font(load("JetBrainsMono-Light.ttf"), 25)
font_norm = pygame.font.Font(load("JetBrainsMono-Regular.ttf"), 30)
font_lg = pygame.font.Font(load("JetBrainsMono-Regular.ttf"), 50)


#--------------------------------------------------------------------------IMAGES

ai_logo = pygame.image.load(load('ai-img.png'))
left_arrow = pygame.image.load(load('left_arrow.png'))
x_button = pygame.image.load((load("x_button_sml.png")))

#--------------------------------------------------------------------------TEXT


# MAINMENU
titletext = title.render("Title", True, (255,255,255))
playtext = font_norm.render("Play", True, (255,255,255))
settingstext = font_norm.render("Settings", True, (255,255,255))
credittext = font_norm.render("Credits", True, (255,255,255))
quittext_main_menu = font_norm.render("Quit", True, (255,255,255))

#QUITMENU
quit_text = font_norm.render("Are you sure ?", True, (255,255,255))
yes = sml.render("Yes", True, (255,255,255))
no = sml.render("No", True, (255,255,255))

#SETTINGS MENU

settingstext_menu = font_lg.render("Settings", True, (255,255,255))
sound_txt = font_norm.render("Sound", True, (255,255,255))
on_txt = sml.render("On", True, (255,255,255))
off_txt = sml.render("Off", True, (255,255,255))

fullscreen_txt = font_norm.render("Fullscreen", True, (255,255,255))

#CREDITS

credit_txt = font_lg.render("Credits", True, (255,255,255))

#--------------------------------------------------------------------------SOUND

big_button_sound = mixer.Sound(load("click.wav"))
open_menu_sound = mixer.Sound(load("open_menu.wav"))
click = mixer.Sound(load("play_button.wav"))
low_hum = mixer.Sound(load("low_hum.wav"))
static = mixer.Sound(load("glitch_static_out.wav"))
glitch_out = mixer.Sound(load("glitch_static_out.wav"))
