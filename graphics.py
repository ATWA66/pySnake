import pygame
from config import SW,SH,BLOCK_SIZE

def screen_init():
    
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("HackaSnake")
    pygame.display.set_icon(pygame.image.load("img/icon.png"))
    clock = pygame.time.Clock()
    return screen, clock


def drawGrid(screen):

    for x in range(0, SW, BLOCK_SIZE):
        for y in range(0, SH, BLOCK_SIZE):

            rect = pygame.Rect(x, y, BLOCK_SIZE,BLOCK_SIZE)
            pygame.draw.rect(screen, "black", rect, 1)
