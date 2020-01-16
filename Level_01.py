import pygame
import random
import pygame.freetype
from main_menu import Main_Menu
import time

#Class for the cards with their specific parameters and functions to be called while running the program
class Card:
    def __init__(self, color, position, width, height, match):
        self.color = color
        self.position = position
        self.width = width
        self.height = height
        self.match = match        
        self.selected = False

    #Funtion to draw cards on screen while face down
    def draw(self, screen, fill = 0):
        pygame.draw.rect(screen, self.color, (self.position[0],self.position[1],self.width,self.height), fill)

    #Function that checks if mouse is over the cards
    def isOver(self, pos):
        if pos[0] > self.position[0] and pos[0] < self.position[0] + self.width:
            if pos[1] > self.position[1] and pos[1] < self.position[1] + self.height:
                return True   
        return False
    
    #Function that draws a shape with a random color inside a card, based on the match paramater ( (RGB), int) from the class
    def shape_draw(self, screen):
        if (self.selected):
            if self.match[0] == 0: # Draws Circle if Shape value = 0
                pygame.draw.circle(screen, self.match[1], (self.position[0]+self.width//2,self.position[1]+self.height//2), 30)            
            elif self.match[0] == 1: # Draws Square if Shape value = 1
                pygame.draw.rect(screen, self.match[1], (self.position[0]+self.width//4,self.position[1]+self.height//3,self.width//2,self.height//3))              
            else: # Draws Triangle if Shape value = 2                 
                pygame.draw.polygon(screen, self.match[1], [(self.position[0]+self.width//2,self.position[1]+self.height//3) , (self.position[0]+self.width*0.75,self.position[1]+(self.height//3+self.height//3)),(self.position[0]+self.width*0.25,self.position[1]+(self.height//3+self.height//3))])

# Class parameters for the buttons on the main menu and in the levels
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
        # Loads font to be used
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

#Function that compares both selected cards
def check_pair (c1, c2):
    if c1.match[0] == c2.match[0] and c1.match[1] == c2.match[1]:
        
        return True
    else:
        return False
    

def levels(Cx,Cy):
    pygame.init()
    
    #Defines window resolution
    res = (1290, 712)

    #Draws the window with previous parameters
    screen = pygame.display.set_mode(res)
    
    #Loads font to be used while running the program
    my_font = pygame.freetype.Font("NotoSans-Regular.ttf", 23)
    
    # Adds the 'Exit' Button to the level screen
    Button_Set = []
    Button_Set.append(Button((255,255,0),5,670, 140, 30, 'EXIT'))
    
    
    # Creates array of X_positon and Y_Position, creates all possible card locations
    Card_position = []
    padding = 10
    Total_H = 550
    Board = (Cx, Cy)
    Card_H = (Total_H - (Board[1]-1)*padding)//Board[1]
    y = 50 - Card_H
    pos_y = []
    for i in range(Board[1]): 
        y = y + Card_H + padding
        pos_y.append(y)

    pos_x = []
    Card_W = int(Card_H - Card_H//Board[1])
    x = 360 - Card_W
    for i in range(Board[0]):
        x = x + Card_W + padding
        pos_x.append(x)
    print(pos_y)
    for i in pos_x:
        for j in pos_y:
            Card_position.append((i,j))
    
    # Array of all colors used for the shapes
    RGB = [(0, 255, 255), (255, 0, 255), (0, 0, 255), (255,0,0), (0,255,0), (255,255,0)]
    
    #Array of of numbers used in the function draw_shape to determine which shape will be drawned
    Shapes = [0, 1, 2]
    
    #Creates empty array of the deck for the level
    Game_Deck = []

    # Creates array to be used in the function that compares both cards
    Selected_Cards = []


    #Creates array of all cards for the specific level and shuffles it
    Possible_Cards = []
    for j in Shapes:
        for k in RGB:
            Possible_Cards.append((j,k))
    random.shuffle(Possible_Cards)

    #Creates array of all pairs for the specific level and shuffles it
    Card_Sequence = []
    for i in range((Board[0]*Board[1]) // 2):
        Card_Sequence.append(Possible_Cards[i])
        Card_Sequence.append(Possible_Cards[i])
    random.shuffle(Card_Sequence)

    # Adds all cards to the Deck to be used with all the parameters created before
    for i in range(len(Card_Sequence)):
         Game_Deck.append(Card((0,255,0), Card_position[i], Card_W, Card_H, Card_Sequence[i]))
    
    # Gets position of the mouse during game
    pos = pygame.mouse.get_pos()

    # Detectes if mouse is pressed during game
    mb = pygame.mouse.get_pressed()

    #Plays music for the specifc level
    pygame.mixer.music.play(-1)
    
    #Shuffles the Deck before starting the game to assure different outcomes every game
    random.shuffle(Game_Deck)

    #Draws every card, face down, in the beginning of the game
    for card in Game_Deck:
        card.draw(screen)
    
    #Initalize all variables used during the game
    num_cards_selected = 0 #Used to see how many cards the player has clicked
    score = 0 # Score at the beginning of the game
    p_attempt = 0 # Used to take points from the players score based on player moves
    pair_set = 6 # Total of pairs in the specific level

    #Load music for this level and plays it at the start of the game
    end_song = False
    
    while (True):
        screen.fill((0,0,20))
        # Prints the Score with the Value on screen
        my_font.render_to(screen, (20, 20), ('Score:' + str(score)), (255,255,0))
        
        # Gets position of the mouse during game
        pos = pygame.mouse.get_pos()

        # Detectes if mouse is pressed during game
        mb = pygame.mouse.get_pressed()

        # Draws the 'Exit' Button and changes it's color if the player hovers it
        for button in Button_Set:
            button.draw(screen)
            if button.isOver(pos):
                button.color = (255, 255 ,255)
            else:
                button.color = (255,255,0)

        # Cycle used to select cards and compare them
        for card in Game_Deck:
            if card.selected == False:
                # Change card color if the players hovers it
                if card.isOver(pos):
                    card.color = (255, 255 ,255)
                    card.draw(screen)

                    # Detects mouse click
                    if (mb[0]):

                        #Resets number of selected cards after checking if they matched or not
                        if num_cards_selected == 2:
                            num_cards_selected = 0

                        #Changes the card state to selected
                        card.selected = True
                        
                        # Adds the selected cards to the empty array to be compared
                        Selected_Cards.append(card)
                        #Adds one to number of cards selected with every click
                        num_cards_selected += 1
                        
                        # Check if the player has selected 2 cards
                        if num_cards_selected == 2:
                            # Adds one to the players move count
                            p_attempt += 1

                            # Checks if the cards match or not using the previous array and the 'check_pair' function  
                            if check_pair(Selected_Cards[-1], Selected_Cards[-2]):

                                # Condition used to remove both cards if they are equal
                                if card.selected:
                                    c1 = None
                                    c2 = None
                                    for c in Game_Deck:
                                        if card.match == c.match:
                                            if c1 != None:
                                                c2 = c
                                            else:
                                                c1 = c
                                    Game_Deck.remove(c1)
                                    Game_Deck.remove(c2)
                                    # Resets the number of cards selected and the player move count
                                    num_cards_selected = 0
                                    p_attempt = 0

                                    #Adds 100 to the player score after removing both cards
                                    score += 100
                                    # Removes one pair from the total of the level
                                    pair_set -= 1
                        
                        # Removes players score based on the number of attempts from the player                     
                            for i in range (1, p_attempt+1):
                                if i == 1:
                                    continue
                                else:
                                    score -= 20*(p_attempt-1)
                                    if score < 0:
                                        score = 0
                                    break
                else:
                    card.color = (0, 255, 0) 
                    card.draw(screen)
            else:
                # Resets the number of cards clicked 
                if num_cards_selected == 2:
                    card.selected = False
                    continue
                
                # Draws the shapes inside of the cards after clicked
                card.shape_draw(screen)

            # Changes the card color if the player hovers a card
                if card.isOver(pos):
                    card.color = (255, 255 ,255)
                    card.draw(screen, 2)
                else:
                    card.color = card.match[1] 
                    card.draw(screen, 2)
         
         # Detects of the player clicked the 'X' in the game's window or uses the 'ALT + F4? command and exits the game
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                exit()

        # Displays the 'Congratulation' message after the player clears the board
        if pair_set == 0:
            if end_song == False:
                pygame.mixer.music.stop()
                end_song = True   
            my_font.render_to(screen, (1290//2-button.width, 720//2-button.height//2), 'CONGRATULATIONS!', random.choice(RGB))
        

        # Detects if the player clicked the 'Exit' Button, stopping the music
        # and sending the player to the main menu
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in Button_Set:
                if button.isOver(pos):
                    if button.text == 'EXIT':
                        pygame.mixer.music.stop()
                        return Main_Menu(True)

        # Flips everything that was buffered and draws it in the screen
        pygame.display.flip()
