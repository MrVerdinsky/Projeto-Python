import pygame
import random
import pygame.freetype

class Button:
    def __init__(self, color, x,y,width,height, text=''):
            self.color = color
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.text = text
        
    # function that draws the buttons the screen
    def draw(self,screen, outline=None):
        
        my_font = pygame.freetype.Font("NotoSans-Regular.ttf", 23)   
        
        # Draws the buttons on the screen from with the specified values
        pygame.draw.rect(screen, self.color, (self.x,self.y,self.width,self.height),2)
        
        # Prints the level tile set in the buttons
        if self.text != '':
            rect = my_font.get_rect(self.text)
            my_font.render_to(screen, (self.x + (self.width//2 -  rect.width//2), self.y + (self.height//2 -  rect.height//2)), self.text, self.color)
            
    # function that detects if mouse is hovering the button
    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False

def Main_Menu(bool):
        pygame.init() # Initializes pygame, with the default parameters
        # Define window size/resolution
        res = (1280,712) 

        #Creates the game window and display surface
        screen = pygame.display.set_mode(res)

        # Loads title page image
        image = pygame.image.load("shuffle.png") 

        # Creates Button list
        Button_Set = []
        Button_Set.append(Button((255,255,0), 572,262, 140, 30, '4x3'))
        Button_Set.append(Button((255,255,0),572,302, 140, 30, '4x4'))
        Button_Set.append(Button((255,255,0),572,342, 140, 30, '5x4'))
        Button_Set.append(Button((255,255,0),572,382, 140, 30, '6x5'))
        Button_Set.append(Button((255,255,0),572,422, 140, 30, '6x6'))
        Button_Set.append(Button((255,255,0),572,482, 140, 30, 'EXIT'))

        # Game loop, to keep the game running until window closed of "Exit" button pressed
        while (True):
        # Prints the buttons on screen
            for button in Button_Set:
                button.draw(screen)
            
            # Get Mouse position
            pos = pygame.mouse.get_pos()

            # Cycle to process windows events, like closing the window, or pressing a key
            for event in pygame.event.get():
                # Condition to check if user closed the window
                if (event.type == pygame.QUIT):
                    # Closes the application
                    exit()
            
                # Detects the click of the mouse on the buttons
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for button in Button_Set:
                        if button.isOver(pos):
                                if button.text == 'EXIT':
                                    quit()
                                
                                elif button.text == '4x3':
                                    Level = 1
                                    return Level
                                
                                elif button.text == '4x4':
                                    Level = 2
                                    return Level
                
                # Detects the hovering of the mouse over the buttons
                # And changes their color accordingly
                if event.type == pygame.MOUSEMOTION:
                    for button in Button_Set:
                        if button.isOver(pos):
                            button.color = (255, 255 ,255)
                        else:
                            button.color = (255, 255, 0)
            
            # Draws the image with function *blit*
            screen.blit(image, (240,0))
            # Swaps buffers, displaying what was rendered before

            pygame.display.flip()

            # Detects the click of the mouse on the buttons