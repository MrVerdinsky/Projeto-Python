import pygame
import random
import pygame.freetype
from main_menu import Main_Menu

class Card:
    def __init__(self, color, x, y, width, height, radius, pair):
        
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.pair = pair
        self.radius = radius
        self.selected = False
    
    def draw(self, screen, fill = 0):
        pygame.draw.rect(screen, self.color, (self.x,self.y,self.width,self.height), fill)

    def isOver(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False
    
    def circle_draw(self, screen):
        for i in range(self.pair):
            if i == 2:
                pygame.draw.circle(screen, (255,0,0), (self.x+self.width//2,self.y+self.height//2), self.radius, 0)
            else:
                pygame.draw.circle(screen, (0,255,0), (self.x+self.width//2,self.y+self.height//2), self.radius)

    
    def sqr_draw(self, screen):
       for i in range(self.pair):
            if i == 1:
                pygame.draw.rect(screen, (255, 0, 255), (self.x+self.width//2-35,self.y+self.height//2-35,70,70))
            else:
                pygame.draw.rect(screen, (0, 0, 255), (self.x+self.width//2-35,self.y+self.height//2-35,70,70))

    def tri_draw(self, screen):
       for i in range(self.pair):
            if i == 4:
                pygame.draw.polygon(screen, (255, 0, 255), [(self.x+self.width//2,self.y+self.height//3) , (self.x+self.width*0.75,self.y+(self.height//3+self.height//3)),(self.x+self.width*0.25,self.y+(self.height//3+self.height//3))])
            else:
                pygame.draw.polygon(screen, (0, 253, 253), [(self.x+self.width//2,self.y+self.height//3) , (self.x+self.width*0.75,self.y+(self.height//3+self.height//3)),(self.x+self.width*0.25,self.y+(self.height//3+self.height//3))])

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
    
    Button_Set = []
    Button_Set.append(Button((255,255,0),5,670, 140, 30, 'EXIT'))
    
    pos_x = [360,490,620,750]
    random.shuffle(pos_x)
    pos_y = [50, 255, 460]
    random.shuffle(pos_y)
    Card_01 = Card((0, 255, 0), pos_x[0], pos_y[0], 125, 200, 30, 1)
    Card_02 = Card((0, 255, 0), pos_x[1], pos_y[1], 125, 200,30, 1)
    Card_03 = Card((0, 255, 0), pos_x[2], pos_y[2], 125, 200, 0, 2)
    Card_04 = Card((0, 255, 0), pos_x[3], pos_y[0], 125, 200, 0, 2)
    Card_05 = Card((0, 255, 0), pos_x[0], pos_y[1], 125, 200, 30, 3)
    Card_06 = Card((0, 255, 0), pos_x[1], pos_y[2], 125, 200, 30, 3)
    Card_07 = Card((0, 255, 0), pos_x[2], pos_y[0], 125, 200, 0, 4)
    Card_08 = Card((0, 255, 0), pos_x[3], pos_y[1], 125, 200, 0, 4)
    Card_09 = Card((0, 255, 0), pos_x[0], pos_y[2], 125, 200, 0, 5)
    Card_10 = Card((0, 255, 0), pos_x[1], pos_y[0], 125, 200, 0, 5)
    Card_11 = Card((0, 255, 0), pos_x[2], pos_y[1], 125, 200, 0, 6)
    Card_12 = Card((0, 255, 0), pos_x[3], pos_y[2], 125, 200, 0, 6)
    
    Card_Set = [Card_01, Card_02, Card_03, Card_04, Card_05, Card_06, Card_07, Card_08, Card_09, Card_10, Card_11, Card_12]
    
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
        my_font = pygame.freetype.Font("NotoSans-Regular.ttf", 23)
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
                            if card_shape == 1 and card.pair == 1:
                                if card.selected == True:
                                    Card_Set.remove(Card_01)
                                    Card_Set.remove(Card_02)
                                    score += 100
                                    num_cards_selected = 0
                                    p_attempt = 0
                                    pair_set -= 1
                                    print(pair_set)

                            if card_shape == 2 and card.pair == 2:
                                if card.selected == True:
                                    Card_Set.remove(Card_03)
                                    Card_Set.remove(Card_04)
                                    score += 100
                                    num_cards_selected = 0
                                    p_attempt = 0
                                    pair_set -= 1
                                    
                            if card_shape == 3 and card.pair == 3:
                                if card.selected == True:
                                    Card_Set.remove(Card_05)
                                    Card_Set.remove(Card_06)
                                    score += 100
                                    num_cards_selected = 0
                                    p_attempt = 0
                                    pair_set -= 1
                                    print(pair_set)
                            
                            if card_shape == 4 and card.pair == 4:
                                if card.selected == True:
                                    Card_Set.remove(Card_07)
                                    Card_Set.remove(Card_08)
                                    score += 100
                                    num_cards_selected = 0
                                    p_attempt = 0
                                    pair_set -= 1
                                    print(pair_set)

                            if card_shape == 5 and card.pair == 5:
                                if card.selected == True:
                                    Card_Set.remove(Card_09)
                                    Card_Set.remove(Card_10)
                                    score += 100
                                    num_cards_selected = 0
                                    p_attempt = 0
                                    pair_set -= 1
                                    print(pair_set)
                            
                            if card_shape == 6 and card.pair == 6:
                                if card.selected == True:
                                    Card_Set.remove(Card_11)
                                    Card_Set.remove(Card_12)
                                    score += 100
                                    num_cards_selected = 0
                                    pair_set -= 1
                                    print(pair_set)
                 
                else:
                    card.color = (0, 255, 0) 
                    card.draw(screen)
            
            else:
                if num_cards_selected == 3:
                        card.selected = False
                        continue
                
                if card.pair == 1 or card.pair == 3:
                    card.circle_draw(screen)
                    if card.pair == 1:
                        card_shape = 1
                        card.color = (0,255,0)
                        card.draw(screen, 2)   
                        if card.isOver(pos):
                            card.color = (255, 255 ,255)
                            card.draw(screen, 2)
                        else:
                            card.color = (0,255,0)
                            card.draw(screen, 2)
                    
                    elif card.pair == 3:
                        card_shape = 3
                        if card.isOver(pos):
                            card.color = (255, 255 ,255)
                            card.draw(screen, 2)
                        else:
                            card.color = (255, 0, 0) 
                            card.draw(screen,2)
            
                elif card.pair == 2 or card.pair == 4:
                    card.sqr_draw(screen)
                    
                    if card.pair == 2:
                        card_shape = 2
                        card.color = (255, 0, 255)
                        card.draw(screen, 2)
                        if card.isOver(pos):
                            card.color = (255, 255 ,255)
                            card.draw(screen, 2)
                        else:
                            card.color = (255, 0, 255)
                            card.draw(screen,2)
                    
                    elif card.pair == 4:
                        card_shape = 4
                        if card.isOver(pos):
                            card.color = (255, 255 ,255)
                            card.draw(screen, 2)
                        else:
                            card.color = (0, 0, 255)
                            card.draw(screen,2)
                    
                else:
                    card.tri_draw(screen)
                    
                    if card.pair == 5:
                        card_shape = 5
                        card.color = (255, 0, 255)
                        card.draw(screen, 2)
                        if card.isOver(pos):
                            card.color = (255, 255 ,255)
                            card.draw(screen, 2)
                        else:
                            card.color = (255, 0, 255)
                            card.draw(screen,2)
                    elif card.pair == 6:
                        card_shape = 6
                        if card.isOver(pos):
                            card.color = (255, 255 ,255)
                            card.draw(screen, 2)
                        else:
                            card.color = (0, 253, 253)
                            card.draw(screen,2)
                        
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
