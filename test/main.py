import pygame

pygame.init()

# Параметры окна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Загрузка фонового изображения
background = pygame.image.load("img/screen.png")

# Цвет рамки
RED = (255, 0, 0)

# Определяем рамку (x, y, ширина, высота)
click_area2 = pygame.Rect(700, 400, 200, 100)  # Прямоугольная область
click_area = pygame.Rect(800, 600, 200, 100)  # Прямоугольная область

running = True
while running:
    screen.blit(background, (0, 0))  # Отображение фона

    # Отрисовка рамки поверх фона
    pygame.draw.rect(screen, RED, click_area, 3)  # 3 - толщина линии
    pygame.draw.rect(screen, RED, click_area2, 3) 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if click_area.collidepoint(event.pos):  # Проверка нажатия в рамке
                print("Клик в рамке!")
            if click_area2.collidepoint(event.pos):  # Проверка нажатия в рамке
                print("Клик в рамке!")

    pygame.display.flip()  # Обновление экрана

pygame.quit()
