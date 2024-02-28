import pygame
import random
#pygame initialization
pygame.init()
#screen settings
screen = pygame.display.set_mode((1600, 798))
#title and icon settings
pygame.display.set_caption('Jurassic Game')
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

#game background settings

background = pygame.image.load('fondod.png')


#player settings
player_img = pygame.image.load('dinop.png')
player_x = 568
player_y = 0
player_x_change = 0 #variable for player movement
player_y_change = 0 #variable for player movement
#player first position
def player(axis_x, axis_y):
    screen.blit(player_img, (axis_x, axis_y))
def enemy(axis_x, axis_y):
    screen.blit(enemy_img, (axis_x, axis_y))

#bullet shooring
def bullet(x, y):
    global visible_bullet
    visible_bullet = True
    screen.blit(bullet_img, (x+60, y+80))

#enemy settings

enemy_img = pygame.image.load('enemigo.png') #enemy image
enemy_x = random.randint(0,1000)
enemy_y =  500
enemy_x_change = 3 #variable for enemy movement



#bullet settings

bullet_img = pygame.image.load('bullet.png') #bullet image
bullet_x = player_x
bullet_y =  player_y
bullet_x_change = 5 #variable for enemy movement
bullet_y_change = 5 #variable for enemy movement
visible_bullet=False



#screen display settings
screen_alive=True
while screen_alive: #screen display loop
    screen.blit(background,(0,0)) # screen color settings
    #event loop evaluation
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #screen display quit event
            screen_alive=False # transform the boolean to false for loop quit
        if event.type == pygame.KEYDOWN: #event for movement with key down
            if event.key == pygame.K_LEFT:
                player_x_change -= 3
            if event.key == pygame.K_RIGHT:
                player_x_change += 3
            if event.key == pygame.K_UP:
                player_y_change -= 3
            if event.key == pygame.K_DOWN:
                player_y_change += 3
            #evento space bar
            if event.key == pygame.K_SPACE:
                bala_x= player_x
                bullet(player_x, player_y)

        if event.type == pygame.KEYUP:  #event for movement with key up
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player_y_change = 0
                player_x_change = 0



    #bullet movement
    if bullet_y<900:
        bullet_y = 0
    if visible_bullet == True:
        bullet(bullet_x, bullet_y)
        bullet_y += bullet_x_change


    #player
    # player  with dynamic movement for x and y axis
    player_x+=player_x_change
    player_y+=player_y_change
    #limit for player movement
    if player_x < 0:
        player_x = 0
    if player_x > 1400:
        player_x = 1400
    if player_y < 0:
        player_y = 0
    if player_y > 700:
        player_y = 700

    #enemy

    # enemy  with dynamic movement for x and y axis
    enemy_x+=enemy_x_change
    #limit for enemy movement
    if enemy_x < 0:
        enemy_x_change = 3
    if enemy_x > 1500:
        enemy_x_change = -3




    #player function
    player(player_x,player_y)
    #enemy function
    enemy(enemy_x,enemy_y)

    #screen display update event
    pygame.display.update()

