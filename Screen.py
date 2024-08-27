import pygame

WIDTH = 500
HEIGHT = 500

screen = pygame.display.set_mode((WIDTH , HEIGHT))
screen.fill((255,255,255))
pygame.display.update()
running = True
while running:
    for event in pygame.event.get(): # to get all events in pygame.get function
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()