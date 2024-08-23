import pygame

janela = pygame.display.set_mode([800, 600])
pygame.display.set_caption("Tetris")

loop = True

while loop:

    for events in pygame.event.get():

        if events.type == pygame.QUIT:
            loop = False

    pygame.display.update()
