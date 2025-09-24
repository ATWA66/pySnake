import pygame
import random
from config import BLOCK_SIZE, SW, SH
class Apple:
    def __init__(self):
        self.x = int(random.randint(0, SW)/BLOCK_SIZE)*BLOCK_SIZE
        self.y = int(random.randint(0, SH)/BLOCK_SIZE)*BLOCK_SIZE
        self.rect = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)

    def update(self):
        from main import screen
        pygame.draw.rect(screen, "red", self.rect)

class Snake:
    
    _snake = None  # приватное статическое поле для хранения экземпляра

    def __new__(cls, *args, **kwargs):
        if cls._snake is None:
            cls._snake = super(Snake, cls).__new__(cls)
        return cls._snake

    def __init__(self):
        self.x, self.y = BLOCK_SIZE, BLOCK_SIZE
        self.xdir = 1
        self.ydir = 0
        self.head = pygame.Rect(self.x,self.y, BLOCK_SIZE, BLOCK_SIZE)
        self.body = [pygame.Rect(self.x - BLOCK_SIZE,self.y, BLOCK_SIZE, BLOCK_SIZE)]
        self.dead = False

    def update(self):
        for square in self.body:
            if self.head.x == square.x and self.head.y == square.y:
                self.dead = True
            if self.head.x not in range(0,SW) or self.head.y not in range(0,SH):
                self.dead = True

        if self.dead:
            self.x, self.y = BLOCK_SIZE, BLOCK_SIZE
            self.head = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)
            self.body = [pygame.Rect(self.x-BLOCK_SIZE, self.y, BLOCK_SIZE, BLOCK_SIZE)]
            self.xdir = 1
            self.ydir = 0
            self.dead = False

        self.body.append(self.head)
        for i in range(len(self.body)-1):
            self.body[i].x, self.body[i].y = self.body[i+1].x, self.body[i+1].y
        self.head.x += self.xdir*BLOCK_SIZE
        self.head.y += self.ydir*BLOCK_SIZE
        self.body.remove(self.head)

snake = Snake()