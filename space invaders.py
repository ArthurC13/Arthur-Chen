import pygame
import random
import math

# -- Global Constants


# -- Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)
RED = (255, 0, 0)

# -- Initialise Pygame
pygame.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)

# -- Black Screen
size = (640,480)
screen = pygame.display.set_mode(size)

# -- Title of new window/screen
pygame.display.set_caption('Space Invaders')

# -- classes
class invader(pygame.sprite.Sprite):
    #define the constructor for invaders
    def __init__(self, color, width, height, speed):
        #call the sprite constructor
        super().__init__()
        self.speed = speed
        #create a sprite and fill it with colour
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        #set the position of the sprite
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, 630)
        self.rect.y = random.randrange(-50, 0)
    #End procedure
    def update(self):
        self.rect.y += self.speed
        if self.rect.y >= 480:
            self.rect.y -= 480
            self.speed += 1
            self.rect.x = random.randrange(0, 630)
#End Class

class bullet(pygame.sprite.Sprite):
    def __init__(self, color, x, y, speed):
        #call the sprite constructor
        super().__init__()
        self.speed = speed
        #create a sprite and fill it with colour
        self.image = pygame.Surface([2,2])
        self.image.fill(color)
        #set the position of the sprite
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def update(self):
        self.rect.y -= self.speed

class player(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.speed = 0
        self.lives = 5
        self.bullet_count = 50
        self.score = 0
        #create a sprite and fill it with colour
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        #set the position of the sprite
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = 400
    def player_set_speed(self,speed):
        self.speed = speed
    def update(self):
        self.rect.x += self.speed
        if self.rect.x < 0:
            self.rect.x += 640
        elif self.rect.x > 630:
            self.rect.x -= 640
        

# -- Exit game flag set to false
done = False
#create a list of the snow blocks
invaders_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
#create a list of all sprites
all_sprites_group = pygame.sprite.Group()

#create the invaders
number_of_invaders = 20
for x in range(number_of_invaders):
    my_invader = invader(BLUE, 10, 10, 1)
    invaders_group.add(my_invader)
    all_sprites_group.add(my_invader)
#next x

player = player(YELLOW, 10, 10)
all_sprites_group.add(player)

# -- Manages how fast screen refreshes
clock = pygame.time.Clock()

#display
texts = 'Lives: ' + str(player.lives) + '   Score: ' + str(player.score) + '   Bullets: ' + str(player.bullet_count)
onscreen = myfont.render(texts, False, WHITE)

### -- Game Loop

while not done:
    # -- User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.player_set_speed(-3)
            elif event.key == pygame.K_RIGHT:
                player.player_set_speed(3)
            elif event.key == pygame.K_UP and player.bullet_count > 0:
                my_bullet = bullet(RED, player.rect.x, player.rect.y, 4)
                bullet_group.add(my_bullet)
                all_sprites_group.add(my_bullet)
                player.bullet_count -= 1
                texts = 'Lives: ' + str(player.lives) + '   Score: ' + str(player.score) + '   Bullets: ' + str(player.bullet_count)
                onscreen = myfont.render(texts, False, WHITE)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.player_set_speed(0)
        #End If
    #Next event

    # -- game logic goes after this comment
    all_sprites_group.update()
    player_hit_group = pygame.sprite.spritecollide(player, invaders_group, True)
    for i in bullet_group:
        bullet_hit_group = pygame.sprite.spritecollide(i, invaders_group, True)
        for b in bullet_hit_group:
            player.score += 5
            texts = 'Lives: ' + str(player.lives) + '   Score: ' + str(player.score) + '   Bullets: ' + str(player.bullet_count)
            onscreen = myfont.render(texts, False, WHITE)
    for a in player_hit_group:
        player.lives -= 1
        texts = 'Lives: ' + str(player.lives) + '   Score: ' + str(player.score) + '   Bullets: ' + str(player.bullet_count)
        onscreen = myfont.render(texts, False, WHITE)

    # -- Screen background is BLACK
    screen.fill(BLACK)

    # -- Draw here
    all_sprites_group.draw(screen)

    screen.blit(onscreen, (10, 0))

    # -- flip display to reveal new position of objects
    pygame.display.flip()

    # - The clock ticks over
    clock.tick(60)

#End While - End of game loop

pygame.quit()
