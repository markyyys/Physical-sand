import random

import numpy
import pygame.constants

from pygame_init import *
particle = numpy.array(2)
surface = numpy.zeros((WIDTH, HEIGHT, 5))

running = True


for i in range(WIDTH):
    for j in range(random.randint(20, 40)):
        surface[i][j][0] = random.randint(120, 170)
        surface[i][j][1] = random.randint(120, 170)
        surface[i][j][2] = 120
        surface[i][j][3] = 1.



def switcher(num):
    if num == 1.:
        num = 0.
    else:
        num = 1.
    return num

def clear_particle(x, y):
    surface[x][y][3] = 0.
    surface[x][y][0] = 0.
    surface[x][y][1] = 0.
    surface[x][y][2] = 0.

def create_particle(r, g, b, x, y, s):
    surface[x][y][3] = 1.
    surface[x][y][0] = r
    surface[x][y][1] = g
    surface[x][y][2] = b
    surface[x][y][4] = s




def delete_particles():
    for i in range(-2, 3):
        for j in range(-2, 3):
            try:
                surface[pygame.mouse.get_pos()[0] + i][HEIGHT - pygame.mouse.get_pos()[1] + j][3] = 0.
                surface[pygame.mouse.get_pos()[0] + i][HEIGHT - pygame.mouse.get_pos()[1] + j][0] = 0.
                surface[pygame.mouse.get_pos()[0] + i][HEIGHT - pygame.mouse.get_pos()[1] + j][1] = 0.
                surface[pygame.mouse.get_pos()[0] + i][HEIGHT - pygame.mouse.get_pos()[1] + j][2] = 0.
            except IndexError:
                continue

def add_particles(s, r, g):
    for i in range(-1, 2):
        for j in range(-1, 2):
            try:
                surface[pygame.mouse.get_pos()[0] + i][HEIGHT - pygame.mouse.get_pos()[1] + j][3] = 1.
                surface[pygame.mouse.get_pos()[0] + i][HEIGHT - pygame.mouse.get_pos()[1] + j][0] = random.randint(r, r + (r // 5))
                surface[pygame.mouse.get_pos()[0] + i][HEIGHT - pygame.mouse.get_pos()[1] + j][1] = random.randint(g, g + (g // 5))
                surface[pygame.mouse.get_pos()[0] + i][HEIGHT - pygame.mouse.get_pos()[1] + j][2] = 120
                surface[pygame.mouse.get_pos()[0] + i][HEIGHT - pygame.mouse.get_pos()[1] + j][4] = s
                print(surface[pygame.mouse.get_pos()[0] + i][HEIGHT - pygame.mouse.get_pos()[1] + j][4])
            except IndexError:
                continue

def calculate_falling(x, y):
    if y > 0:
        try:
            if surface[x][y - 1][3] == 0.:
                create_particle(surface[x][y][0], surface[x][y][1], surface[x][y][2], x, y - 1, surface[x][y][4])
                clear_particle(x, y)
            #elif surface[x][y - 1][4] == 1. and surface[x][y][4] != 1.:
            #    water = surface[x][y - 1]
            #    create_particle(surface[x][y][0], surface[x][y][1], surface[x][y][2], x, y - 1, 0.)
            #    clear_particle(x, y)
            #    create_particle(water[0], water[1], water[2], x, y, 1.)
        except IndexError:
            return

def calculate_physics(x, y):
    dirs = [-1, 1]
    if y > 0:
        if surface[x - 1][y - 1][3] == 0. and surface[x + 1][y - 1][3] == 0.:
            dir = dirs[random.randint(0, 1)]
            #print(dir)
            create_particle(surface[x][y][0], surface[x][y][1], surface[x][y][2], x + dir, y - 1, 0.)
            clear_particle(x, y)
        elif surface[x - 1][y - 1][3] == 0.:
            create_particle(surface[x][y][0], surface[x][y][1], surface[x][y][2], x - 1, y - 1, 0.)
            clear_particle(x, y)
        elif surface[x + 1][y - 1][3] == 0.:
            create_particle(surface[x][y][0], surface[x][y][1], surface[x][y][2], x + 1, y - 1, 0.)
            clear_particle(x, y)
        elif surface[x - 1][y - 1][4] == 1. and surface[x + 1][y - 1][4] == 1.:
            dir = dirs[random.randint(0, 1)]
            #print(dir)
            water = surface[x + dir][y - 1]
            create_particle(surface[x][y][0], surface[x][y][1], surface[x][y][2], x + dir, y - 1, 0.)
            clear_particle(x, y)
            create_particle(water[0], water[1], water[2], x, y, 1.)
        elif surface[x - 1][y - 1][4] == 1.:
            water = surface[x + 1][y - 1]
            create_particle(surface[x][y][0], surface[x][y][1], surface[x][y][2], x - 1, y - 1, 0.)
            clear_particle(x, y)
            create_particle(water[0], water[1], water[2], x, y, 1.)
        elif surface[x + 1][y - 1][4] == 1.:
            water = surface[x - 1][y - 1]
            create_particle(surface[x][y][0], surface[x][y][1], surface[x][y][2], x + 1, y - 1, 0.)
            clear_particle(x, y)
            create_particle(water[0], water[1], water[2], x, y, 1.)

def calculate_physics_water(x, y):
    dirs = [-1, 1]
    if y > 0:
        if surface[x - 1][y][3] == 0. and surface[x + 1][y][3] == 0.:
            dir = dirs[random.randint(0, 1)]
            #print(dir)
            create_particle(surface[x][y][0], surface[x][y][1], surface[x][y][2], x + dir, y, 1.)
            clear_particle(x, y)
        elif surface[x - 1][y][3] == 0.:
            create_particle(surface[x][y][0], surface[x][y][1], surface[x][y][2], x - 1, y, 1.)
            clear_particle(x, y)
        elif surface[x + 1][y][3] == 0.:
            create_particle(surface[x][y][0], surface[x][y][1], surface[x][y][2], x + 1, y, 1.)
            clear_particle(x, y)


while running:

    mouse_presses = pygame.mouse.get_pressed()

    if mouse_presses[0]:
        add_particles(0., 120, 120)
    elif mouse_presses[1]:
        add_particles(1., 12, 12)
    elif mouse_presses[2]:
        delete_particles()

    for event in pygame.event.get():
        # проверить закрытие окна
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    for i in range(WIDTH):
        for j in range(HEIGHT):
            if surface[i][j][3] != 0.:
                if surface[i][j - 1][3] == 0. or surface[i][j - 1][4] == 1.:
                    #print(surface[i][j])
                    calculate_falling(i, j)
                elif surface[i][j][4] == 0.:
                    if 0 < i < WIDTH - 2 and surface[i - 1][j - 1][3] == 0.:
                        calculate_physics(i, j)
                    elif 0 < i < WIDTH - 2 and surface[i + 1][j - 1][3] == 0.:
                        calculate_physics(i, j)
                    elif 0 < i < WIDTH - 2 and surface[i - 1][j - 1][4] == 1.:
                        calculate_physics(i, j)
                    elif 0 < i < WIDTH - 2 and surface[i + 1][j - 1][4] == 1.:
                        calculate_physics(i, j)
                elif surface[i][j][4] == 1.:
                    if 0 < i < WIDTH - 2 and surface[i - 1][j][3] == 0.:
                        calculate_physics_water(i, j)
                    elif 0 < i < WIDTH - 2 and surface[i + 1][j][3] == 0.:
                        calculate_physics_water(i, j)


    for i in range(WIDTH):
        for j in range(HEIGHT):
            if surface[i][j][3] == 1.:
                pygame.draw.rect(screen, (surface[i][j][0], surface[i][j][1], surface[i][j][2]), (i, HEIGHT - j, 1, 1))

    pygame.display.flip()
    clock.tick(FPS)