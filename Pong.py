import pygame
import time
import random

# -- Global Constants


# -- Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)

# -- Initialise Pygame
pygame.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)

# -- Black Screen
size = (640,480)
screen = pygame.display.set_mode(size)

# -- Title of new window/screen
pygame.display.set_caption('Pong')

# -- Exit game flag set to false
done = False

#variables
x_val = 310
y_val = 230
x_offset = 0
y_offset = 0
x_padd = 30
y_padd = 210
x_padd2 = 595
y_padd2 = 20
p1_score = 0
p2_score = 0
ball_color = BLUE
start_time = time.time()
start = True

# -- Manages how fast screen refreshes
clock = pygame.time.Clock()

#scoreboard
scores = str(p1_score) + ' : ' + str(p2_score)
scoreboard = myfont.render(scores, False, WHITE)

### -- Game Loop

while not done:
    # -- User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        #End If
    #Next event

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and y_padd > 0:
        y_padd -= 5
    if keys[pygame.K_DOWN] and y_padd < 420:
        y_padd += 5
    

    # -- game logic goes after this comment
    if time.time() > start_time + 1 and start:
        x_offset = random.randrange(-5, 14, 10)
        y_offset = random.randrange(-5, 14, 10)
        print(x_offset, y_offset)
        start = False

    if y_padd2 > y_val - 20 and y_padd2 > 0:
        y_padd2 -= 5
    if y_padd2 < y_val - 20 and y_padd2 < 420:
        y_padd2 += 5

    #check for collisions
    if x_val < x_padd + 15 and x_val > x_padd and y_val > y_padd - 20 and y_val < y_padd + 70:
        x_offset *= -1
        if ball_color == BLUE:
            ball_color = YELLOW
        else:
            ball_color = BLUE
    if x_val > x_padd2 - 15 and x_val < x_padd2 + 15 and y_val > y_padd2 - 20 and y_val < y_padd2 + 70:
        x_offset *= -1
        if ball_color == BLUE:
            ball_color = YELLOW
        else:
            ball_color = BLUE
    if y_val < 0 or y_val > 460:
        y_offset *= -1
        if ball_color == BLUE:
            ball_color = YELLOW
        else:
            ball_color = BLUE
    if x_val < 0:
        p2_score += 1
        x_val = 310
        y_val = 230
        start_time = time.time()
        x_offset = 0
        y_offset = 0
        start = True
        scores = str(p1_score) + ' : ' + str(p2_score)
        scoreboard = myfont.render(scores, False, WHITE)
    if x_val > 620:
        p1_score += 1
        x_val = 310
        y_val = 230
        start_time = time.time()
        x_offset = 0
        y_offset = 0
        start = True
        scores = str(p1_score) + ' : ' + str(p2_score)
        scoreboard = myfont.render(scores, False, WHITE)

    #updateball axis
    x_val += x_offset
    y_val -= y_offset

    # -- Screen background is BLACK
    screen.fill(BLACK)

    # -- Draw here
    pygame.draw.rect(screen, ball_color, (x_val,y_val,20,20))
    pygame.draw.rect(screen, WHITE, (x_padd,y_padd,15,60))
    pygame.draw.rect(screen, WHITE, (x_padd2,y_padd2,15,60))

    screen.blit(scoreboard,(285,0))
    # -- flip display to reveal new position of objects
    pygame.display.flip()

    # - The clock ticks over
    clock.tick(60)

#End While - End of game loop

pygame.quit()
