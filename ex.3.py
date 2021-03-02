import pygame
import math
import random

from pygame.constants import (
    KEYDOWN, K_SPACE
)

pygame.init()

FPS = 30
screensize = (800, 400)
screen = pygame.display.set_mode(screensize, pygame.SRCALPHA)
clock = pygame.time.Clock()
finished = False

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 250, 0)
PINK = (230, 50, 230)
Tan4 = (139, 90, 43)
Cyan4 = (0, 139, 139)
Firebrick4 = (139, 26, 26)
Green4 = (0, 139, 0)
DARK_BLUE = (18, 0, 91)
DARK_GREEN = (0, 94, 0)
NIGHT_GRAY = (104, 98, 115)
ck = (127, 33, 33)
BRIGHT_YELLOW = (255, 244, 47)

DARKNESS = pygame.Surface(screensize, pygame.SRCALPHA)
DARKNESS.set_alpha(200)
DARKNESS.fill((0, 0, 0))

SEE_THROUGH = pygame.Surface((800, 180), pygame.SRCALPHA)
SEE_THROUGH.set_alpha(150)
SEE_THROUGH.fill((124, 118, 135))


def grass(color):
    """Рисует траву"""
    pygame.draw.rect(screen, color, (0, screensize[1] // 2, screensize[0], screensize[0] // 2))


def sun(location, size):
    """
        Рисует солнце с заданными координатами и размерами
    """
    r1 = 40 * size
    r2 = 38 * size
    x2 = 0
    y2 = 0
    y3 = 0
    y4 = 0
    x3 = 0
    x4 = 0
    z = 0
    z1 = 0
    n = 30
    a = 2 * math.pi / n
    pygame.draw.circle(screen, YELLOW, (location[0], location[1]), 39 * size)
    for i in range(n):
        if i == 0:
            x2 = location[0] + r1 * math.cos(0)
            y2 = location[1] + r1 * math.sin(0)
            x3 = location[0] + r1 * math.cos(a)
            y3 = location[1] + r1 * math.sin(a)
            x4 = location[0] + r2 * math.cos(a / 2)
            y4 = location[1] + r2 * math.sin(a / 2)
            z1 = a / 2

        if i > 0:
            z = z + a
            z1 = z1 + a
            x2 = location[0] + r1 * math.cos(z)
            y2 = location[1] + r1 * math.sin(z)
            x3 = location[0] + r1 * math.cos(z - a)
            y3 = location[1] + r1 * math.sin(z - a)
            x4 = location[0] + r2 * math.cos(z1)
            y4 = location[1] + r2 * math.sin(z1)
        pygame.draw.aalines(screen, WHITE, False, [[x2, y2], [x4, y4], [x3, y3]])


def house(location, size, window_color):
    """
        Рисует домик по заданным координатам и размеру
    """
    pygame.draw.rect(screen, Tan4, (location[0] - 120 * size, location[1] - 70 * size, 90 * size, 90 * size))
    pygame.draw.rect(screen, window_color, (location[0] - 90 * size, location[1] - 50 * size, 30 * size, 30 * size))
    pygame.draw.polygon(screen, Firebrick4, [[location[0] - 120 * size, location[1] - 70 * size],
                                             [location[0] - 30 * size, location[1] - 70 * size],
                                             [location[0] - 75 * size, location[1] - 100 * size]])
    # radius = 15 * size
    # if not day:
    #     for i in range(int(radius)):
    #         light_surface = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
    #
    #     pygame.draw.circle(light_surface, BRIGHT_YELLOW, location, i)
    #     screen.blit(light_surface, (0, 0))


def tree(location, size):
    """
        Рисует дерево с заданными координатами и размером
    """
    r = 28 * size
    phi = 3 / 5 * math.pi
    pygame.draw.rect(screen, BLACK, (location[0] - 18 * size, location[1] + 10 * size, 10 * size, 80 * size))
    pygame.draw.circle(screen, Green4, (location[0] - r / 2, location[1] + 10 * size), 2 * r / 3)
    pygame.draw.circle(screen, BLACK, (location[0] - r / 2, location[1] + 10 * size), 2 * r / 3, 1)
    location[0] = location[0] + 10 * size
    location[1] = location[1] + 3 * size
    for i in range(5):
        pygame.draw.circle(screen, Green4, (location[0], location[1]), 2 * r / 3)
        pygame.draw.circle(screen, BLACK, (location[0], location[1]), 2 * r / 3, 1)
        location[0] = location[0] + r * math.cos(phi)
        location[1] = location[1] + r * math.sin(phi)
        phi = phi + 2 / 5 * math.pi


def draw_clouds(x, y, size):
    """
        Рисует облако с заданными координатами и размером
    """
    r = 28 * size
    pygame.draw.circle(screen, WHITE, (x, y), 2 * r / 3)
    pygame.draw.circle(screen, BLACK, (x, y), 2 * r / 3, 1)
    for j in range(6):
        if j == 1 or j == 3 or j == 5:
            x = x + 2 * r / 3
        if j == 2:
            y = y - 2 * r / 3
        if j == 4:
            y = y + 2 * r / 3
        pygame.draw.circle(screen, WHITE, (x, y), 2 * r / 3)
        pygame.draw.circle(screen, BLACK, (x, y), 2 * r / 3, 1)


day = True

clouds = []


def create_massive_of_clouds(number):
    """
    Создает массив облаков заданного размера
    """
    for i in range(number):
        x = random.randrange(0, screensize[0] + 200)
        y = random.randrange(0, screensize[1] // 3)
        clouds.append({"x": x, "y": y})


create_massive_of_clouds(10)

while not finished:

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == KEYDOWN:
            if event.key == K_SPACE:
                day = not day

    if day:
        sky_color = LIGHT_BLUE
        grass_color = GREEN
        cloud_color = WHITE
        window_color = Cyan4
    else:
        sky_color = DARK_BLUE
        grass_color = DARK_GREEN
        cloud_color = NIGHT_GRAY
        window_color = BRIGHT_YELLOW

    screen.fill(sky_color)

    for c in clouds:
        c['x'] -= 0.5

        if c['x'] < -100:
            c['x'] = random.randrange(screensize[0], screensize[0] + 100)
            c['y'] = random.randrange(0, screensize[1] // 3)

    screen.fill(sky_color)
    SEE_THROUGH.fill(ck)
    SEE_THROUGH.set_colorkey(ck)


    def sun_moon(sun_location):
        """
        Рисует Солнце и Луну с заданными координатами
        """
        if day:
            sun(sun_location, 1)
        else:
            pygame.draw.ellipse(screen, WHITE, [sun_location[0] - 33, sun_location[1] - 34, 80, 80])
            pygame.draw.ellipse(screen, sky_color, [sun_location[0] - 13, sun_location[1] - 38, 78, 78])


    sun_moon([500, 50])

    for c in clouds:
        draw_clouds(c['x'], c['y'], 0.7)
    screen.blit(SEE_THROUGH, (0, 0))
    grass(grass_color)

    house((200, 200), 1, window_color)
    house((500, 250), 0.5, window_color)
    house((700, 270), 0.7, window_color)
    house((300, 300), 0.8, window_color)

    tree([248, 110], 1)
    tree([400, 180], 0.5)
    tree([750, 180], 0.8)

    if not day:
        screen.blit(DARKNESS, (0, 0))

    pygame.display.flip()
    pygame.display.update()

pygame.quit()
