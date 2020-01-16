# imports pygame into our program
import pygame
import pygame.freetype
from Level_01 import levels
from main_menu import Main_Menu
from Level_02 import level_02

# Class that makes the buttons and takes input from the mouse


def main():
    pygame.init()
    pygame.mixer.music.load('main_menu.ogg')
    pygame.mixer.music.play(-1)
    # Game loop, to keep the game running until window closed of "Exit" button pressed
    Level = Main_Menu(True)    
    while (True):
        
        if (Level == 1):

            Level = levels(4, 3)

        elif (Level == 2):  
            Level = levels(4, 4)

main()
