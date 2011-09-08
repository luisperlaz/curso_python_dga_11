# -*- coding: utf-8 -*-
import os
import pygame

def cargar_imagen(nombre, optimizar=False):
    ruta = os.path.join('imagenes', nombre)
    imagen = pygame.image.load(ruta)

    if optimizar:
        return imagen.convert()
    else:
        return imagen.convert_alpha()

def cargar_sonido(nombre):
    ruta = os.path.join('sonidos', nombre)
    return pygame.mixer.Sound(ruta)

def play_music(nombre, loop=1):
    ruta = os.path.join('sonidos', nombre)
    pygame.mixer.music.load(ruta)
    pygame.mixer.music.play(loop)

