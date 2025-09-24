import pygame
import sys
import random
from config import SW,SH,BLOCK_SIZE
from classes import snake, Apple
from graphics import drawGrid, screen_init


screen, clock = screen_init()
screen.fill((3, 99, 32)) 
apple = Apple()
drawGrid(screen)
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            # Винести в функцию controlsCheck
        if event.type ==pygame.KEYDOWN:
            if event.key ==pygame.K_DOWN:
                snake.ydir = 1
                snake.xdir = 0
            elif event.key ==pygame.K_UP:
                snake.ydir = -1
                snake.xdir = 0
            elif event.key ==pygame.K_RIGHT:
                snake.ydir = 0
                snake.xdir = 1
            elif event.key ==pygame.K_LEFT:
                snake.ydir = 0
                snake.xdir = -1

    snake.update()
    screen.fill((3, 99, 32))
    drawGrid(screen)
    apple.update()
    pygame.draw.rect(screen, "green", snake.head)

    for square in snake.body:
        pygame.draw.rect(screen, "green", square)
    if snake.head.x ==apple.x and snake.head.y == apple.y:
        snake.body.append(pygame.Rect(square.x, square.y, BLOCK_SIZE, BLOCK_SIZE))
        apple = Apple()

    pygame.display.update()
    clock.tick(5)
    

