import pygame
import random
import math

# -- Global Constants

# -- Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255,255,0)
PURPLE = (103,13,173)
PINK = (255,192,203)
LIGHTPINK = (239, 154, 154)
LIGHTBLUE = (209, 237, 242)
BRIGHTBLUE = (15, 137, 202)

# -- variables
level = 0

# -- Initialise Pygame
pygame.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
myfont2 = pygame.font.SysFont('Comic Sans MS', 20)

# -- Black Screen
size = (950,750)
screen = pygame.display.set_mode(size)

# -- Title of new window/screen
pygame.display.set_caption('My Window')


# -- Map
intromap = '''1111111111111111111111111
1000000000000000000000001
1000000000000000000000901
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

def makemap():
    string = ''
    enemyneeded = level
    for line in range(0, 25):
        if line in [0, 24]:
            string += '1111111111111111111111111'
        else:
            for i in range(0, 25):
                if i in [0, 24]:
                    string += '1'
                elif line == 12 and i == 12:
                    string += '2'
                elif enemyneeded > 0 and random.randint(0, int(50*math.exp(-0.0693*line))) == 1:
                    enemyneeded -= 1
                    string += '9'
                elif random.randint(0, 3) == 0:
                    string += '1'
                else:
                    string += '0'
        string += '\n'
    if enemyneeded != 0:
        return(makemap())
    return(string[:-1])

# -- introduction
introduction = True
introtexts = '''Welcome to tile game!
Use arrow keys to move arround
Collect all keys from enemy bases(pink tiles)
then return to your own base(yellow tiles)
Enemies in red follows you and deals damage on contact
They cannot enter your base
When hitted by an enemy, enemy respawn at their
base and you gain invincibility for 3 seconds



If a stage is unplayable, press r to regenerate a new stage

Complete this stage and start you adventure!'''
        

# -- Classes
class player(pygame.sprite.Sprite):
    #define the constructor for player
    def __init__(self, colour, width, height, speed, x, y):
        #call the sprite constructor
        super().__init__()
        #create a sprite and fill it with colour
        self.image = pygame.Surface([width,height])
        self.image.fill(colour)
        self.colour = colour
        #set the position of the sprite
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        #set variables
        self.speed = speed
        self.last_action = 'r'
        self.health = 100
        self.score = 0
        self.first_move = False
        self.last_spawn = pygame.time.get_ticks()
        self.spawntime = 3000
        self.last_flash = pygame.time.get_ticks()
        self.flash = 150
        self.invincible = True
        self.last_invincible = pygame.time.get_ticks()
        self.invincible_time = 3000
    def update(self):
        x_speed = 0
        y_speed = 0
        now = pygame.time.get_ticks()
        if now - self.last_spawn >= self.spawntime:
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
        if now - self.last_flash >= self.flash and self.invincible:
            self.flashing()
            self.last_flash = pygame.time.get_ticks()
        if now - self.last_invincible >= self.invincible_time and self.invincible:
            self.invincible = False
            self.image.fill(BLUE)
        if not self.first_move and (x_speed != 0 or y_speed != 0):
            self.first_move = True
        contactenemies = pygame.sprite.spritecollide(self, enemies_group, False)
        for i in contactenemies:
            if not i.spawn and not self.invincible:
                self.health -= 10
                self.score += 10
                self.invincible = True
                self.last_invincible = pygame.time.get_ticks()
                update_scoreboard()
            i.respawn()
        if pygame.sprite.spritecollide(self, safe_zone_group, False):
            global basecount
            if basecount == 0:
                self.new_level()
        self.rect.x += x_speed
        self.rect.y += y_speed
    def respawn(self):
        self.last_spawn = pygame.time.get_ticks()
        self.last_flash = pygame.time.get_ticks()
        self.first_move = False
        self.invincible = True
        self.last_invincible = pygame.time.get_ticks()
        self.rect.x = 365
        self.rect.y = 365
    def flashing(self):
        if self.colour == BLUE:
            self.colour = LIGHTBLUE
        else:
            self.colour = BLUE
        self.image.fill(self.colour)
    def new_level(self):
        global basecount, textlayer1, level, introduction
        if introduction:
            introduction = False
        all_sprites_group.empty()
        all_sprites_group.add(self)
        unbreakable_wall_group.empty()
        enemies_group.empty()
        enemy_base_group.empty()
        safe_zone_group.empty()
        self.respawn()
        self.score += level*100
        level += 1
        self.health += 10
        basecount = draw_map(makemap())
        update_scoreboard()
            
class tile(pygame.sprite.Sprite):
    #define the constructor for player
    def __init__(self, colour, width, height, x, y):
        #call the sprite constructor
        super().__init__()
        #create a sprite and fill it with colour
        self.image = pygame.Surface([width,height])
        self.colour = colour
        self.image.fill(colour)
        #set the position of the sprite
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def update(self):
        if self.colour == PINK and pygame.sprite.spritecollide(self, player_group, False):
            global basecount
            self.colour = GREEN
            self.image.fill(self.colour)
            basecount -= 1
            player.score += 100
            update_scoreboard()

class enemy(pygame.sprite.Sprite):
    #define the constructor for player
    def __init__(self, colour, width, height, speed, x, y):
        #call the sprite constructor
        super().__init__()
        #create a sprite and fill it with colour
        self.image = pygame.Surface([width,height])
        self.colour = colour
        self.image.fill(colour)
        #set the position of the sprite
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        #set variables
        self.spawn_x = x
        self.spawn_y = y
        self.speed = speed
        self.last_action = 'r'
        self.health = 100
        self.last_time = pygame.time.get_ticks()
        self.spawntime = 1500
        self.last_flash = pygame.time.get_ticks()
        self.flash = 150
        self.spawn = True
    def update(self):
        now = pygame.time.get_ticks()
        x_speed = 0
        y_speed = 0
        if now - self.last_time >= self.spawntime and player.first_move:
            self.image.fill(RED)
            self.spawn = False
            if not pygame.sprite.spritecollide(self, unbreakable_wall_group, False):
                keys = pygame.key.get_pressed()
                if self.rect.y >= player.rect.y:
                    y_speed = -self.speed
                    self.last_action = 'u'
                elif self.rect.x >= player.rect.x:
                    x_speed = -self.speed
                    self.last_action = 'l'
                elif self.rect.x < player.rect.x and player.rect.x - self.rect.x > 3:
                    x_speed = self.speed
                    self.last_action = 'r'
                elif self.rect.y < player.rect.y:
                    y_speed = self.speed
                    self.last_action = 'd'
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
        elif now - self.last_flash >= self.flash:
            if self.colour == RED:
                self.colour = LIGHTPINK
            else:
                self.colour = RED
            self.image.fill(self.colour)
            self.last_flash = pygame.time.get_ticks()
        if pygame.sprite.spritecollide(self, safe_zone_group, False):
            self.respawn()
    def respawn(self):
        self.rect.x = self.spawn_x
        self.rect.y = self.spawn_y
        self.spawn = True
        self.last_time = pygame.time.get_ticks()
        
#sprite groups
#create a list of all sprites
all_sprites_group = pygame.sprite.Group()
unbreakable_wall_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
enemies_group = pygame.sprite.Group()
enemy_base_group = pygame.sprite.Group()
safe_zone_group = pygame.sprite.Group()

#create objects
player = player(BLUE, 20, 20, 3, 365, 365)
all_sprites_group.add(player)
player_group.add(player)


#draw map
def draw_map(maptext):
    maplist = maptext.split('\n')
    x = 0
    y = 0
    basecount = 0
    for line in maplist:
        for i in line:
            if i == '1':
                mywall = tile(PURPLE, 30, 30, x, y)
                all_sprites_group.add(mywall)
                unbreakable_wall_group.add(mywall)
            if i == '2':
                mywall = tile(YELLOW, 30, 30, x, y)
                safe_zone_group.add(mywall)
                all_sprites_group.add(mywall)
            if i == '9':
                mywall = tile(PINK, 30, 30, x, y)
                enemy_base_group.add(mywall)
                all_sprites_group.add(mywall)
                myenemy = enemy(RED, 20, 20, 2, x+6, y+5)
                enemies_group.add(myenemy)
                all_sprites_group.add(myenemy)
                basecount += 1
            x += 30
        y += 30
        x = 0
    return basecount
basecount = draw_map(intromap)

#scoreboard
def blit_texts(texts, colour, x, y, y_intervals, font):
    textlist = texts.split('\n')
    counter = 0
    for line in textlist:
        screen.blit(font.render(line, False, colour), (x, y + (y_intervals*counter)))
        counter += 1

def update_scoreboard():
    global level, basecount, scoretexts
    scoretexts = 'Level: ' + str(level) + '\nHealth: ' + str(player.health) + '\nScore: ' + str(player.score) + '\nKeys left: ' + str(basecount)

update_scoreboard()

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
        elif event.type == pygame.KEYDOWN and not introduction:
            if event.key == pygame.K_r:
                level -= 1
                player.score -= level*100
                player.health -= 10
                player.new_level()
        #End If
    #Next event

    # -- game logic goes after this comment

    # -- Screen background is BLACK
    screen.fill(BLACK)

    # -- Draw here
    if introduction:
        blit_texts(introtexts, BRIGHTBLUE, 45, 45, 35, myfont2)

    all_sprites_group.draw(screen)
    enemies_group.draw(screen)
    player_group.draw(screen)

    blit_texts(scoretexts, WHITE, 760, 10, 40, myfont)
    blit_texts("Press 'r' to\nregenerate\nlevel", WHITE, 760, 630, 35, myfont)

    # -- flip display to reveal new position of objects
    pygame.display.flip()

    # -- update
    all_sprites_group.update()

    # - The clock ticks over
    clock.tick(60)

#End While - End of game loop

pygame.quit()
