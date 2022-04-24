import pygame
import sys

screen_size = (720,720)

pygame.init()

pygame.display.set_caption("Chaos Game")
screen = pygame.display.set_mode(screen_size, 0, 32)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    
    pygame.display.update()