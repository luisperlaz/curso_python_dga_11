# -*- coding: utf-8 -*-

'''
Starter para crear el juego del mono que come bananas
'''

# imports iniciales
import sys
import pygame
from pygame.locals import *
# archivo con nuestras utilidades
from utils import *

# Constantes del juego
ANCHO, ALTO = 640, 480
FPS = 30

pygame.init()

pantalla = pygame.display.set_mode((ANCHO, ALTO))
#pygame.display.set_caption()

# Creación del entorno
# Fondo
#fondo = pygame.image.load()
#fondo = fondo.convert()

# Sprites


reloj = pygame.time.Clock()


while True:
    tiempo = reloj.tick(FPS)
    # Eventos
    for eventos in pygame.event.get():
        if eventos.type == QUIT:
            sys.exit(0)

    # Actualizar


    # Dibujar
    #pantalla.blit(fondo, (0,0))

    pygame.display.flip()

