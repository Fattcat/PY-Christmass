import pygame
import random
import os
import pyautogui

# Inicializujeme Pygame
pygame.init()

# Rozmery obrazovky
screen_width = 900
screen_height = 600

# Vytvorenie okna bez okrajov a pozadia
screen = pygame.display.set_mode((screen_width, screen_height), pygame.NOFRAME)
pygame.display.set_caption('Moving GIF')

# Nastavenie transparentnej farby pozadia
transparent_color = (0, 0, 0)
screen.set_colorkey(transparent_color)

# Načítanie GIFu s transparentnou farbou
gif = pygame.image.load('Christmass.gif').convert_alpha()
original_gif_rect = gif.get_rect()
gif = pygame.transform.scale(gif, (200, 200))  # Prispôsobte veľkosť podľa potreby

# Počiatočné pozície a rýchlosť gifu
x = random.randint(0, screen_width - gif.get_width())
y = random.randint(0, screen_height - gif.get_height())
dx = 1
dy = 1

# Hlavná slučka
running = True
clock = pygame.time.Clock()
frame_delay = 60  # oneskorenie medzi snímkami (v milisekundách)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Pohyb gifu na mieste (posúvanie)
    x += dx
    y += dy

    # Odbíjanie od stien obrazovky
    if x <= 0 or x >= screen_width - gif.get_width():
        dx = -dx
    if y <= 0 or y >= screen_height - gif.get_height():
        dy = -dy

    # Vymazanie predchádzajúceho snímku
    screen.fill(transparent_color)

    # Zobrazenie gifu na aktuálnej pozícii
    screen.blit(gif, (x, y))

    # Aktualizácia obrazovky
    pygame.display.update()

    # Odstávka na simuláciu pohybu
    clock.tick(frame_delay)

# Ukončenie Pygame
pygame.quit()
