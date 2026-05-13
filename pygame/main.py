import pygame
pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sprites a obrázky")
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        # Můžete nahradit vlastním obrázkem:
        # self.image = pygame.image.load("assets/images/player.png").convert_alpha()
        self.image = pygame.Surface((50, 50), pygame.SRCALPHA)
        pygame.draw.rect(self.image, (0, 200, 100), (0, 0, 50, 50))
        pygame.draw.rect(self.image, (0, 150, 80), (0, 0, 50, 50), 3)
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        # Omezení na obrazovku
        self.rect.clamp_ip(screen.get_rect())

# Vytvoření sprite a skupiny
player = Player(WIDTH // 2, HEIGHT // 2)
all_sprites = pygame.sprite.Group(player)

running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()

    screen.fill((30, 30, 30))
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()