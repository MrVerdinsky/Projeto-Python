import pygame
import random
import pygame.freetype
from main_menu import Main_Menu
import time

class Card:
    def __init__(self, color, position, width, height, match):
        self.color = color
        self.position = position
        self.width = width
        self.height = height
        self.match = match        
        self.selected = False

    def draw(self, screen, fill = 0):
        pygame.draw.rect(screen, self.color, (self.position[0],self.position[1],self.width,self.height), fill)

    def isOver(self, pos):
        if pos[0] > self.position[0] and pos[0] < self.position[0] + self.width:
            if pos[1] > self.position[1] and pos[1] < self.position[1] + self.height:
                return True
            
        return False
    def shape_draw(self, screen):

        if (self.selected):
            if self.match[0] == 0:
                pygame.draw.circle(screen, self.match[1], (self.position[0]+self.width//2,self.position[1]+self.height//2), 30)            
            elif self.match[0] == 1:
                pygame.draw.rect(screen, self.match[1], (self.position[0]+self.width//4,self.position[1]+self.height//3,self.width//2,self.height//3))              
            else:                  
                pygame.draw.polygon(screen, self.match[1], [(self.position[0]+self.width//2,self.position[1]+self.height//3) , (self.position[0]+self.width*0.75,self.position[1]+(self.height//3+self.height//3)),(self.position[0]+self.width*0.25,self.position[1]+(self.height//3+self.height//3))])


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


def check_pair (c1, c2):
    if c1.match[0] == c2.match[0] and c1.match[1] == c2.match[1]:
        print("They natch")
        return True
    else:
        print("they dont")
        return False
    

def level_01():
    pygame.init()
    
    res = (1290, 712)
    screen = pygame.display.set_mode(res)
    
    my_font = pygame.freetype.Font("NotoSans-Regular.ttf", 23)
    
    
    Button_Set = []
    Button_Set.append(Button((255,255,0),5,670, 140, 30, 'EXIT'))
    
    Card_position = []
    pos_x = [360,490,620,750]
    pos_y = [50, 255, 460]
    for i in pos_x:
        for j in pos_y:
            Card_position.append((i,j))
    
    RGB = [(0, 255, 255), (255, 0, 255), (0, 0, 255), (255,0,0), (0,255,0), (255,255,0)]
    Shapes = [0, 1, 2]
    Game_Deck = []
    Possible_Cards = []
    
    Selected_Cards = []

    for j in Shapes:
        for k in RGB:
            Possible_Cards.append((j,k))
    random.shuffle(Possible_Cards)

    Card_Sequence = []
    for i in range(12 // 2):
        Card_Sequence.append(Possible_Cards[i])
        Card_Sequence.append(Possible_Cards[i])

    random.shuffle(Card_Sequence)

    for i in range(len(Card_Sequence)):
         Game_Deck.append(Card((0,255,0), Card_position[i], 125, 200, Card_Sequence[i]))
    
    pos = pygame.mouse.get_pos()
    mb = pygame.mouse.get_pressed()
    pygame.mixer.music.play(-1)
    random.shuffle(Game_Deck)
    for card in Game_Deck:
        card.draw(screen)
    

    num_cards_selected = 0
    score = 0
    p_attempt = 0
    pair_set = 6
    pygame.mixer.music.load('level_01.ogg')
    pygame.mixer.music.play(-1)
    while (True):
        screen.fill((0,0,20))
        
        my_font.render_to(screen, (20, 20), ('Score:' + str(score)), (255,255,0))
        
        pos = pygame.mouse.get_pos()
        
        mb = pygame.mouse.get_pressed()
        
        for button in Button_Set:
            button.draw(screen)
            if button.isOver(pos):
                button.color = (255, 255 ,255)
            else:
                button.color = (255,255,0)

        for card in Game_Deck:
            if card.selected == False:  
                if card.isOver(pos):
                    card.color = (255, 255 ,255)
                    card.draw(screen)
                    if (mb[0]):
                        if num_cards_selected == 2:
                            num_cards_selected = 0

                        card.selected = True
                        Selected_Cards.append(card)
                        num_cards_selected += 1

                        if num_cards_selected == 2:
                            p_attempt += 1   
                            if check_pair(Selected_Cards[-1], Selected_Cards[-2]):
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
                                    num_cards_selected = 0
                                    score += 100
                                    num_cards_selected = 0
                                    p_attempt = 0
                                    pair_set -= 1
                        
                        # Adds value to score, resets attempt values and removes one pair from the level                     
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
                if num_cards_selected == 2:
                    card.selected = False
                    continue

                card.shape_draw(screen)

                if card.isOver(pos):
                    card.color = (255, 255 ,255)
                    card.draw(screen, 2)
                else:
                    card.color = card.match[1] 
                    card.draw(screen, 2)
         
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                exit()

        if pair_set == 0:
            my_font.render_to(screen, (1290//2-button.width, 720//2-button.height//2), 'CONGRATULATIONS!', random.choice(RGB))

        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in Button_Set:
                if button.isOver(pos):
                    if button.text == 'EXIT':
                        pygame.mixer.music.stop()
                        return Main_Menu(True)
      
        pygame.display.flip()
