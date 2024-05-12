import pygame
from os import listdir
from os.path import isfile, join

pygame.init()


W, H = 800, 600

background = pygame.transform.scale(pygame.image.load('Background.png'), (W, H))
winn = pygame.display.set_mode((W, H))
pygame.display.set_caption('Платформер')


def flip(sprites):
    return [pygame.transform.flip(sprites, True, False)]
    return 


def load_sprite_s(dir, width, hieght, direction=False):
    path = join('assets', dir)
    images = [f for f in listdir(path) if isfile(join(path, f))]


    all_sprites = {}

    for image in images:
        sprite_sheets = pygame.image.load(join(path, image)).convert_alpha()
        sprites = []
        for i in range(sprite_sheets.get_width() // width):
            surface = pygame.Surface((width, hieght), pygame.SRCALPHA)
            rect = pygame.Rect(i * width, 0, i * hieght)
            surface.blit(sprite_sheets, (0, 0), rect)
            sprites.append(pygame.transform.scale2x(surface))

            if direction:
                all_sprites[image.replace('.png', '') + '_right'] = sprites 
                all_sprites[image.replace('.png', '') + '_left'] = flip(sprites)
            
            else:
                all_sprites[image.replace('.png', '')] = sprites 

    return all_sprites



class Player(pygame.sprite.Sprite):
    GRAVITY = 1
    SPRITES = load_sprite_s('character', 32, 32, True)

    def __init__(self, x, y, widht, hieght):
        super().__init__()
        self.rect = pygame.Rect(x, y, widht, hieght)
        self.surface = pygame.Surface((widht, hieght))
        self.color = (0, 0, 255)
        self.surface.fill((self.color))

        self.x_vel = 5
        self.y_vel = 0
        self.fall_count = 0
        self.direction = 'right'


    def movie(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.rect.x > 0:
            self.rect.x -= self.x_vel
        if keys[pygame.K_d] and self.rect.x < W - 50:
            self.rect.x += self.x_vel


        #self.y_vel += min(1, (self.fall_count / FPS) * self.GRAVITY)
        self.rect.y += self.y_vel
        self.fall_count += 1


    def draw(self):
        self.sprite = self.SPRITES('idle_' + self.direction)[0]
        winn.blit(self.surface, (self.rect.x, self.rect.y))



clock = pygame.time.Clock()
FPS = 90


player = Player(100, 100, 50, 50)

game = True
while game:
    winn.blit(background, (0, 0))
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False

    player.draw()
    player.movie()

    pygame.display.update()