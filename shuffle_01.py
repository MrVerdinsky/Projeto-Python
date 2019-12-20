# imports pygame into our program
import pygame
import pygame.freetype

# Class that makes the buttons and takes input from the mouse
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
        
        if outline:
            pygame.draw.rect(screen, outline, (self.x,self.y,self.width+4,self.height+4),0)
            
        pygame.draw.rect(screen, self.color, (self.x,self.y,self.width,self.height),2)
        
        if self.text != '':
            font = pygame.freetype.Font('NotoSans-Regular.ttf', 23)
            text_w, text_h = font.rect(self.text)
            text = font.render(self.text, self.color, self.color)
            screen.blit(text, (self.x + (self.width/2 - text_w/2), self.y + (self.height/2 - text_h/2)))

    # function that detects if mouse is hovering the button
    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False
    
# Defining main function
def main():
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
    while(True):
        
        
        # Get Mouse position
        pygame.mouse.get_pos()

        # Cycle to process windows events, like closing the window, or pressing a key
        for event in pygame.event.get():
            # Condition to check if user closed the window
            if (event.type == pygame.QUIT):
                # Closes the application
                exit()
        
        for button in Button_Set:
            button.draw(screen)
        
        # Draws the image with function *blit*
        screen.blit(image, (240,0))
        # Swaps buffers, displaying what was rendered before
        pygame.display.flip()

# Run function
main()
