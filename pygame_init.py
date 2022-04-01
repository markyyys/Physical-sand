import pygame
import numpy
import random

WIDTH = 130  # ширина игрового окна
HEIGHT = 80 # высота игрового окна
FPS = 30

pygame.init()
pygame.mixer.init()  # для звука
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.SCALED)
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()