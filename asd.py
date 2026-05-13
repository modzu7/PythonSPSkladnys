import pygame

pygame.init()
# Vytvoření okna
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moje první hra")

# Game loop
running = True
while running:
    for event in pygame.event.get():       # 1. Zpracování událostí
        if event.type == pygame.QUIT:       #    Zavření okna
            running = False

    screen.fill((30, 30, 30))               # 2. Vyplnění pozadí (tmavě šedá)
    pygame.display.flip()                   # 3. Aktualizace displeje

pygame.quit()