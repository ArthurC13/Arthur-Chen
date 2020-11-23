import pygame
import random

# -- Global Constants


# -- Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255,255,0)

# -- Initialise Pygame
pygame.init()

# -- Black Screen
size = (750,750)
screen = pygame.display.set_mode(size)

# -- Title of new window/screen
pygame.display.set_caption('My Window')

# -- Map
gamemap = '''1111111111111111111111111
1000000000000000000000001
1000000000000000000000001
1000000000000000000000001
1000000000000000000000001
1000000000000000000000001
1000000000000000000000001
1000000000000000000000001
1000000000000000000000001
1000000000000000000000001
1000000000000000000000001
1000000000000000000000001
1000000000002000000000001
1000000000000000000000001
1000000000000000000000001
1000000000000000000000001
1000000000000000000000001
1000000000000000000000001
1000000000000000000000001
1000000000000000000000001
1000000000000000000000001
1000000000000000000000001
1000000000000000000000001
1000000000000000000000001
1111111111111111111111111
'''

gamemap2 = '''
1111111111111111111111111
1000010010000001000100001
1000001000000000010000001
1110000101100000000010001
1010100010000010101111001
1100001101101000100000001
1001101000100000000000111
1001010000000011111001101
1000000000000001000000001
1011100000000010010110011
1110001001000010000000101
1000001100001000000010101
1000001010102000100000011
1100100000010000000000001
1000010000110000001000011
1000000000000000010010101
1000011011100010001000001
1100000000000100010101101
1100100000000010001000001
1011101010001101000010111
1000000000100011001111001
1000000001011100000001101
1000001000111100000001001
1100101001000011000000011
1111111111111111111111111
'''

def makemap():
    string = ''
    for line in range(0, 25):
        if line in [0, 24]:
            string += '1111111111111111111111111'
        else:
            for i in range(0, 25):
                if i in [0, 24]:
                    string += '1'
                elif line == 12 and i == 12:
                    string += '2'
                elif random.randint(0, 3) == 0:
                    string += '1'
                else:
                    string += '0'
        string += '\n'
    return(string[:-1])
print(makemap())
            

# -- Classes
class player(pygame.sprite.Sprite):
    #define the constructor for player
    def __init__(self, colour, width, height, speed):
        #call the sprite constructor
        super().__init__()
        #create a sprite and fill it with colour
        self.image = pygame.Surface([width,height])
        self.image.fill(colour)
        #set the position of the sprite
        self.speed = speed
        self.last_action = 'r'
        self.rect = self.image.get_rect()
        self.rect.x = 365
        self.rect.y = 365
    def update(self):
        x_speed = 0
        y_speed = 0
        if not pygame.sprite.spritecollide(self, unbreakable_wall_group, False):
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                y_speed = -self.speed
                self.last_action = 'u'
            elif keys[pygame.K_LEFT]:
                x_speed = -self.speed
                self.last_action = 'l'
            elif keys[pygame.K_DOWN]:
                y_speed = self.speed
                self.last_action = 'd'
            elif keys[pygame.K_RIGHT]:
                x_speed = self.speed
                self.last_action = 'r'
        else:
            if self.last_action == 'u':
                y_speed = self.speed
            elif self.last_action == 'l':
                x_speed = self.speed
            elif self.last_action == 'd':
                y_speed = -self.speed
            else:
                x_speed = -self.speed
        self.rect.x += x_speed
        self.rect.y += y_speed

class unbreakable_wall(pygame.sprite.Sprite):
    #define the constructor for player
    def __init__(self, colour, width, height, x, y):
        #call the sprite constructor
        super().__init__()
        #create a sprite and fill it with colour
        self.image = pygame.Surface([width,height])
        self.image.fill(colour)
        #set the position of the sprite
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        

#create a list of all sprites
all_sprites_group = pygame.sprite.Group()
unbreakable_wall_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()

#create objects
player = player(BLUE, 20, 20, 3)
all_sprites_group.add(player)
player_group.add(player)

#draw map
maplist = makemap().split('\n')
x = 0
y = 0
for line in maplist:
    for i in line:
        if i == '1':
            mywall = unbreakable_wall(RED, 30, 30, x, y)
            all_sprites_group.add(mywall)
            unbreakable_wall_group.add(mywall)
        if i == '2':
            mywall = unbreakable_wall(YELLOW, 30, 30, x, y)
            all_sprites_group.add(mywall)
        x += 30
    y += 30
    x = 0

# -- Exit game flag set to false
done = False

# -- Manages how fast screen refreshes
clock = pygame.time.Clock()

### -- Game Loop

while not done:
    # -- User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        #End If
    #Next event

    # -- game logic goes after this comment
    

    # -- Screen background is BLACK
    screen.fill(BLACK)

    # -- Draw here
    all_sprites_group.draw(screen)
    player_group.draw(screen)

    # -- flip display to reveal new position of objects
    pygame.display.flip()

    # -- update
    all_sprites_group.update()

    # - The clock ticks over
    clock.tick(60)

#End While - End of game loop

pygame.quit()
