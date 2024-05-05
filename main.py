import pygame

pygame.init()


W, H = 800, 600

background = pygame.transform.scale(pygame.image.load('Background.png'), (W, H))
winn = pygame.display.set_mode((W, H))
pygame.display.set_caption('Платформер')


class Player(pygame.sprite.Sprite):
    GRAVITY = 1

    def __init__(self, x, y, widht, hieght):
        super().__init__()
        self.rect = pygame.Rect(x, y, widht, hieght)
        self.surface = pygame.Surface((widht, hieght))
        self.color = (0, 0, 255)
        self.surface.fill((self.color))

        self.x_vel = 5
        self.y_vel = 0
        self.fall_count = 0


    def movie(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.rect.x > 0:
            self.rect.x -= self.x_vel
        if keys[pygame.K_d] and self.rect.x < W - 50:
            self.rect.x += self.x_vel


        self.y_vel += min(1, (self.fall_count / FPS) * self.GRAVITY)
        self.rect.y += self.y_vel
        self.fall_count += 1


    def draw(self):
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