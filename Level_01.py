import pygame
import random
import pygame.freetype
from main_menu import Main_Menu
import time

class Card:
    RGB = [(0, 255, 255),(255, 0, 255), (0, 0, 255),(255,0,0), (0,255,0), (255,255,0)]
    random.shuffle(RGB)
    def __init__(self, color, x, y, width, height, pair):
        
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.pair = pair
        self.selected = False
    def draw(self, screen, fill = 0):
        pygame.draw.rect(screen, self.color, (self.x,self.y,self.width,self.height), fill)

    def isOver(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False
    def shape_draw(self, screen, pair):
        if pair == 1 or pair == 3:
            pygame.draw.circle(screen, self.RGB[self.pair-1], (self.x+self.width//2,self.y+self.height//2), 30)
        
        elif pair == 2 or pair == 4:
            pygame.draw.rect(screen, self.RGB[self.pair-1], (self.x+self.width//2-35,self.y+self.height//2-35,70,70))

        else:
            pygame.draw.polygon(screen, self.RGB[self.pair-1], [(self.x+self.width//2,self.y+self.height//3) , (self.x+self.width*0.75,self.y+(self.height//3+self.height//3)),(self.x+self.width*0.25,self.y+(self.height//3+self.height//3))])
    # def circle_draw(self, screen):
    #     pygame.draw.circle(screen, self.RGB[self.pair-1], (self.x+self.width//2,self.y+self.height//2), 30)

    # def sqr_draw(self, screen):
    #     pygame.draw.rect(screen, self.RGB[self.pair-1], (self.x+self.width//2-35,self.y+self.height//2-35,70,70))

    # def tri_draw(self, screen):
    #     pygame.draw.polygon(screen, self.RGB[self.pair-1], [(self.x+self.width//2,self.y+self.height//3) , (self.x+self.width*0.75,self.y+(self.height//3+self.height//3)),(self.x+self.width*0.25,self.y+(self.height//3+self.height//3))])

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

def level_01():
    pygame.init()
    
    res = (1290, 712)
    screen = pygame.display.set_mode(res)
    
    my_font = pygame.freetype.Font("NotoSans-Regular.ttf", 23)
    
    Button_Set = []
    Button_Set.append(Button((255,255,0),5,670, 140, 30, 'EXIT'))
    
    pos_x = [360,490,620,750]
    random.shuffle(pos_x)
    pos_y = [50, 255, 460]
    random.shuffle(pos_y)
    Card_Set = []
    card_x = 0
    card_y = 0
    
    for i in range(12):
        Card_Set.append(Card((0, 255, 0), pos_x[card_x], pos_y[card_y], 125, 200,i//2+1))
        card_x += 1
        if (card_x > 3):
            card_x = 0
            card_y += 1


    
    pos = pygame.mouse.get_pos()
    mb = pygame.mouse.get_pressed()
    
    for card in Card_Set:
        card.draw(screen)
    
    num_cards_selected = 0
    card_shape = 0
    score = 0
    p_attempt = 0
    pair_set = 6
    
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

        for card in Card_Set:
            if card.selected == False:
                
                if card.isOver(pos):
                    card.color = (255, 255 ,255)
                    card.draw(screen)
                    if (mb[0]):
                        
                        if num_cards_selected == 3:
                            num_cards_selected = 0
                            pass
                        
                        card.selected = True
                        num_cards_selected += 1
                        
                        if num_cards_selected == 2:
                            p_attempt += 1
                            if p_attempt == 2:
                                score-= 20
                            if p_attempt == 3:
                                score-= 40
                            if p_attempt == 4:
                                score -= 80
                            if score < 0:
                                score = 0
                            if card_shape == card.pair:
                                if card.selected == True:
                                    c1 = None
                                    c2 = None  
                                    for c in Card_Set:
                                        if card.pair == c.pair:
                                            if c1 != None:
                                                c2 = c
                                            else:
                                                c1 = c
                                    pygame.time.delay(1000)
                                    Card_Set.remove(c1)
                                    Card_Set.remove(c2)
                                    
                        # Adds value to score, resets attempt values and removes one pair from the level       
                                    score += 100
                                    num_cards_selected = 0
                                    p_attempt = 0
                                    pair_set -= 1
                                    
                else:
                    card.color = (0, 255, 0) 
                    card.draw(screen)
                
            else:
                if num_cards_selected == 3:
                    card.selected = False
                    continue
                
                
                card_shape = card.pair
                
                card.shape_draw(screen, card.pair)   
                    
                if card.isOver(pos):
                    card.color = (255, 255 ,255)
                    card.draw(screen, 2)
                else:
                    card.color = card.RGB[card.pair-1]
                    card.draw(screen, 2)
            
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                exit()

        if pair_set == 0:
            my_font.render_to(screen, (600, 300), 'CONGRATULATIONS!', (0, 253, 253))

        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in Button_Set:
                if button.isOver(pos):
                    if button.text == 'EXIT':
                        return Main_Menu(True)

        pygame.display.flip()
level_01()