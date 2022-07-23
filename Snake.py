# import time
# import pygame
# import random

# pygame.init() # Initializing pygame
# dis_W = 800
# dis_H = 600
# dis = pygame.display.set_mode((dis_W,dis_H)) # The screen size
# pygame.display.set_caption("Snake game") # Naming the sceen

# update = pygame.display.update() # Updating the screen

# white = (255, 255, 255) # Tuples for black and white
# black = (0, 0 , 0)

# red = (255, 0, 0) # Tuples for the rgb colors
# blue = (0, 0, 255)
# green = (0, 255, 0)

# snake_block = 10 # Size of the Snake
# snake_speed = 30

# clock = pygame.time.Clock()

# font_style = pygame.font.SysFont(None, 50)

# def message(msg,color):
#     mesg = font_style.render(msg, True, color)
#     dis.blit(mesg, [dis_W/2, dis_H/2])

# def gameLoop(): # THE game Loop
#     game_over = False
#     game_close = False

#     x = dis_W/2 # Position variables
#     y = dis_H/2

#     x_change = 0 # Change in position
#     y_change = 0
    
#     foodx = round(random.randrange(0, dis_W - snake_block) / 10.0 ) * 10 # Food position in a random place
#     foody = round(random.randrange(0, dis_H - snake_block) / 10.0 ) * 10

#     # ! events: (Mouse Move) (Mouse Click) (Key Press)

#     #game_over = False # Ending the program when game_over or quit button is clicked

#     while not game_over:

#         while game_close == True:
#             dis.fill(white) # Changing the color of the screen
#             message("Game Over! Press Q-Quit or R-Retry", black)
#             update

#             for event in pygame.event.get():
#                 if event.type == pygame.KEYDOWN:
#                     if event.key == pygame.K_q:
#                         game_over = True
#                         game_close = False
#                     if event.key == pygame.K_r:
#                         gameLoop()

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 game_over = True
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_LEFT: # IF key is pressed change positon in a direction
#                     x_change = -snake_block
#                     y_change = 0
#                 elif event.key == pygame.K_RIGHT:
#                     x_change = snake_block
#                     y_change = 0
#                 elif event.key == pygame.K_UP:
#                     x_change = 0
#                     y_change = -snake_block
#                 elif event.key == pygame.K_LEFT:
#                     x_change = 0
#                     y_change = snake_block

#             if x >= dis_W or x < 0 or y >= dis_H or y < 0: # End the game if the player touches the bouderies
#                 game_over = True

#             x += x_change # Updating position
#             y += y_change

#             dis.fill(white)

#             pygame.draw.rect(dis, black, [x, y, snake_block, snake_block]) # Creating a rectangle to represent to snake
#             pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block]) # Creating a rectangle to represent the food

#             update
#             if x == foodx and y == foody:
#                 print("Yum")
#             clock.tick(snake_speed)

#     pygame.quit()
#     quit()

# gameLoop()

import pygame
import time
import random
 
pygame.init()
 
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
 
dis_width = 800
dis_height = 600
 
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game by Edureka')
 
clock = pygame.time.Clock()
 
snake_block = 10
snake_speed = 30
 
font_style = pygame.font.SysFont(None, 30)
 
 
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/3, dis_height/3])
 
 
def gameLoop():  # creating a function
    game_over = False
    game_close = False
 
    x1 = dis_width / 2
    y1 = dis_height / 2
 
    x1_change = 0
    y1_change = 0
 
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
 
    while not game_over:
 
        while game_close == True:
            dis.fill(white)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
 
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
 
        x1 += x1_change
        y1 += y1_change
        dis.fill(white)
        pygame.draw.rect(dis, blue, [foodx, foody, snake_block, snake_block])
        pygame.draw.rect(dis, black, [x1, y1, snake_block, snake_block])
        pygame.display.update()
 
        if x1 == foodx and y1 == foody:
            print("Yummy!!")
        clock.tick(snake_speed)
 
    pygame.quit()
    quit()
 
 
gameLoop()