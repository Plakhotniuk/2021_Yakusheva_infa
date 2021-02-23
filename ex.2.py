import pygame
import math

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 300))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)
Tan4 = (139, 90, 43)
Cyan4 = (0, 139, 139)
Firebrick4 = (139, 26, 26)
Green4 = (0, 139, 0)
x = 446
y = 110
phi = 3 / 5 * math.pi
R = 30
x1 = 290
y1 = 60

pygame.draw.rect(screen, LIGHT_BLUE, (0, 0, 600, 195))
pygame.draw.rect(screen, GREEN, (0, 150, 600, 205))
pygame.draw.rect(screen, Tan4, (100, 120, 120, 120))
pygame.draw.rect(screen, Cyan4, (140, 160, 40, 40))
pygame.draw.rect(screen, BLACK, (425, 140, 10, 80))
pygame.draw.polygon(screen, Firebrick4, [[100, 120], [220, 120], [160, 50]])
pygame.draw.circle(screen, Green4, (x - R / 2, y + 10), 2 * R / 3)
pygame.draw.circle(screen, BLACK, (x - R / 2, y + 10), 2 * R / 3, 1)
x = x + 10
y = y + 3
for i in range(5):
    pygame.draw.circle(screen, Green4, (x, y), 2 * R / 3)
    pygame.draw.circle(screen, BLACK, (x, y), 2 * R / 3, 1)
    x = x + R * math.cos(phi)
    y = y + R * math.sin(phi)
    phi = phi + 2 / 5 * math.pi

pygame.draw.circle(screen, WHITE, (x1, y1), 2 * R / 3)
pygame.draw.circle(screen, BLACK, (x1, y1), 2 * R / 3, 1)
for j in range(6):
    if j == 1 or j == 3 or j == 5:
        x1 = x1 + 2 * R / 3
    if j == 2:
        y1 = y1 - 2 * R / 3
    if j == 4:
        y1 = y1 + 2 * R / 3
    pygame.draw.circle(screen, WHITE, (x1, y1), 2 * R / 3)
    pygame.draw.circle(screen, BLACK, (x1, y1), 2 * R / 3, 1)

n = 30
a = 2 * math.pi / n
R1 = 40
z = 0
z1 = 0
R2 = 38
x0 = 550
y0 = 50

for f in range(n):
    if i == 0:
        x2 = x0 + R1 * math.cos(0)
        y2 = y0 + R1 * math.sin(0)
        x3 = x0 + math.cos(a)
        y3 = y0 + math.sin(a)
        x4 = x0 + math.cos(a / 2)
        y4 = y0 + math.sin(a / 2)
        z1 = a / 2

    if i > 0:
        z = z + a
        z1 = z1 + a
        x2 = x0 + R1 * math.cos(z)
        y2 = y0 + R1 * math.sin(z)
        x3 = x0 + math.cos(z - a)
        y3 = y0 + math.sin(z - a)
        x4 = x0 + math.cos(z1)
        y4 = y0 + math.sin(z1)
    pygame.draw.aalines(screen, YELLOW, False, [[x2, y2], [x4, y4], [x3, y3]])

pygame.display.update()

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
