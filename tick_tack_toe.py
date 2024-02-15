import pygame, sys

clock = pygame.time.Clock()

from pygame.locals import *

pygame.init()
pygame.font.init()

pygame.display.set_caption('Tick-Tack-Toe')

window_size = (640, 480)
screen = pygame.display.set_mode(window_size)


#create the playing canvas
rect_background = pygame.Rect(10, 10, window_size[0] - 20, window_size[1] - 20)
rect_vert_div1 = pygame.Rect(212, 10, 10, 460)
rect_vert_div2 = pygame.Rect(419, 10, 10, 460)
rect_horiz_div1 = pygame.Rect(10, 158, 620, 10) 
rect_horiz_div2 = pygame.Rect(10, 311, 620, 10) 

#create text to place on playing canvas
font = pygame.font.SysFont('Times New Roman', 100)
text_O = font.render('O', True, (0, 200, 0), (150, 0, 0))
text_X = font.render('X', True, (0, 0, 200), (150, 0, 0))
text_rect_O = text_O.get_rect()
text_rect_X = text_X.get_rect()
text_player1_win = font.render('P1 WINS!!!!', True, (255, 255, 255), (0, 0, 0))
text_rect_p1_win = text_player1_win.get_rect()
text_player2_win = font.render('P2 WINS!!!!', True, (255, 255, 255), (0, 0, 0))
text_rect_p2_win = text_player2_win.get_rect()

#create rectangles for clicking in position

rect_0_0 = pygame.Rect(10, 10, 202, 148)
rect_0_1 = pygame.Rect(222, 10, 202, 158)
rect_0_2 = pygame.Rect(429, 10, 201, 158)

rect_1_0 = pygame.Rect(10, 168, 202, 148)
rect_1_1 = pygame.Rect(222, 168, 202, 158)
rect_1_2 = pygame.Rect(429, 168, 201, 158)

rect_2_0 = pygame.Rect(10, 321, 202, 148)
rect_2_1 = pygame.Rect(222, 321, 202, 158)
rect_2_2 = pygame.Rect(429, 321, 201, 158)


area_0_0 = False
area_0_1 = False
area_0_2 = False

area_1_0 = False
area_1_1 = False
area_1_2 = False

area_2_0 = False
area_2_1 = False
area_2_2 = False

player = 1

score = [[3, 3, 3],
             [3, 3, 3],
             [3, 3, 3]]

while True:

#drawing the playing canvas

    pygame.draw.rect(screen, (150, 0, 0), rect_background)
    pygame.draw.rect(screen, (200, 200, 200), rect_vert_div1)
    pygame.draw.rect(screen, (200, 200, 200), rect_vert_div2)
    pygame.draw.rect(screen, (200, 200, 200), rect_horiz_div1)
    pygame.draw.rect(screen, (200, 200, 200), rect_horiz_div2)

#the below to remember values for the areas of the playing canvas
#this keeps the O's and X's on the board while the game is running

    if area_0_0 == True:
        if score[0][0] == 1:
            screen.blit(text_O, (70, 20))
        elif score[0][0] == 2:
            screen.blit(text_X, (70, 20))
    if area_0_1 == True:
        if score[0][1] == 1:
            screen.blit(text_O, (282, 20))
        elif score[0][1] == 2:
            screen.blit(text_X, (282, 20))
    if area_0_2 == True:
        if score[0][2] == 1:
            screen.blit(text_O, (484, 20))
        elif score[0][2] == 2:
            screen.blit(text_X, (484, 20))
    if area_1_0 == True:
        if score[1][0] == 1:
            screen.blit(text_O, (70, 183))
        elif score[1][0] == 2:
            screen.blit(text_X, (70, 183))
    if area_1_1 == True:
        if score[1][1] == 1:
            screen.blit(text_O, (282, 183))
        elif score[1][1] == 2:
            screen.blit(text_X, (282, 183))
    if area_1_2 == True:
        if score[1][2] == 1:
            screen.blit(text_O, (484, 183))
        elif score[1][2] == 2:    
            screen.blit(text_X, (484, 183))
    if area_2_0 == True:
        if score[2][0] == 1:
            screen.blit(text_O, (70, 336))
        elif score[2][0] == 2:
            screen.blit(text_X, (70, 336))
    if area_2_1 == True:
        if score[2][1] == 1:
            screen.blit(text_O, (282, 336))
        elif score[2][1] == 2:
            screen.blit(text_X, (282, 336))
    if area_2_2 == True:
        if score[2][2] == 1:
            screen.blit(text_O, (484, 336))    
        elif score[2][2] == 2:
            screen.blit(text_X, (484, 336))
            
#check for winning conditions

#check horizontal lines player 1

    if score[0] == [1, 1, 1]:
        screen.blit(text_player1_win, (20, 20))
    if score[1] == [1, 1, 1]:
        screen.blit(text_player1_win, (20, 20))
    if score[2] == [1, 1, 1]:
        screen.blit(text_player1_win, (20, 20))

#check vertical lines player 1

    if score[0][0] == 1 and score[1][0] == 1 and score[2][0] == 1:
        screen.blit(text_player1_win, (20, 20))
    if score[0][1] == 1 and score[1][1] == 1 and score[2][1] == 1:
        screen.blit(text_player1_win, (20, 20))
    if score[0][2] == 1 and score[1][2] == 1 and score[2][2] == 1:
        screen.blit(text_player1_win, (20, 20))

#check across lines player 1

    if score[0][0] == 1 and score[1][1] == 1 and score[2][2] == 1:
        screen.blit(text_player1_win, (20, 20))
    if score[0][2] == 1 and score[1][1] == 1 and score[2][0] == 1:
        screen.blit(text_player1_win, (20, 20))

#check horizontal lines player 2

    if score[0] == [2, 2, 2]:
        screen.blit(text_player2_win, (20, 20))
    if score[1] == [2, 2, 2]:
        screen.blit(text_player2_win, (20, 20))
    if score[2] == [2, 2, 2]:
        screen.blit(text_player2_win, (20, 20))

    # check vertical lines player 1

    if score[0][0] == 2 and score[1][0] == 2 and score[2][0] == 2:
        screen.blit(text_player2_win, (20, 20))
    if score[0][1] == 2 and score[1][1] == 2 and score[2][1] == 2:
        screen.blit(text_player2_win, (20, 20))
    if score[0][2] == 2 and score[1][2] == 2 and score[2][2] == 2:
        screen.blit(text_player2_win, (20, 20))

#check across lines player 2

    if score[0][0] == 2 and score[1][1] == 2 and score[2][2] == 2:
        screen.blit(text_player2_win, (20, 20))
    if score[0][2] == 2 and score[1][1] == 2 and score[2][0] == 2:
        screen.blit(text_player2_win, (20, 20))


        
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1 and player == 1:
                if rect_0_0.collidepoint(event.pos):
                    area_0_0 = True
                    score[0][0] = 1
                    player = 2
                    break
                elif rect_0_1.collidepoint(event.pos):
                    area_0_1 = True
                    score[0][1] = 1
                    player = 2
                    break
                elif rect_0_2.collidepoint(event.pos):
                    area_0_2 = True
                    score[0][2] = 1
                    player = 2
                    break
                elif rect_1_0.collidepoint(event.pos):
                    area_1_0 = True
                    score[1][0] = 1
                    player = 2
                    break
                elif rect_1_1.collidepoint(event.pos):
                    area_1_1 = True
                    score[1][1] = 1
                    player = 2
                    break
                elif rect_1_2.collidepoint(event.pos):
                    area_1_2 = True
                    score[1][2] = 1
                    player = 2
                    break
                elif rect_2_0.collidepoint(event.pos):
                    area_2_0 = True
                    score[2][0] = 1
                    player = 2
                    break
                elif rect_2_1.collidepoint(event.pos):
                    area_2_1 = True
                    score[2][1] = 1
                    player = 2
                    break
                elif rect_2_2.collidepoint(event.pos):
                    area_2_2 = True
                    score[2][2] = 1
                    player = 2
                    break
                    
            
            if event.button == 1 and player == 2:
                if rect_0_0.collidepoint(event.pos):
                    area_0_0 = True   
                    score[0][0] = 2
                    player = 1
                    break
                elif rect_0_1.collidepoint(event.pos):
                    area_0_1 = True
                    score[0][1] = 2
                    player = 1
                    break
                elif rect_0_2.collidepoint(event.pos):
                    area_0_2 = True
                    score[0][2] = 2
                    player = 1
                    break
                elif rect_1_0.collidepoint(event.pos):
                    area_1_0 = True
                    score[1][0] = 2
                    player = 1
                    break
                elif rect_1_1.collidepoint(event.pos):
                    area_1_1 = True
                    score[1][1] = 2
                    player = 1
                    break
                elif rect_1_2.collidepoint(event.pos):
                    area_1_2 = True
                    score[1][2] = 2
                    player = 1
                    break
                elif rect_2_0.collidepoint(event.pos):
                    area_2_0 = True
                    score[2][0] = 2
                    player = 1
                    break
                elif rect_2_1.collidepoint(event.pos):
                    area_2_1 = True
                    score[2][1] = 2
                    player = 1
                    break
                elif rect_2_2.collidepoint(event.pos):
                    area_2_2 = True
                    score[2][2] = 2
                    player = 1
                    break


    pygame.display.update()
    clock.tick(60)
