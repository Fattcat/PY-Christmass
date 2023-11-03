import pygame
import random
import os
import pyautogui
import time
from PIL import ImageGrab  # Pridaná knižnica pre screenshot
import keyboard

# Startnutie casovaca
StartTime = time.time()

# Nastavenie casu ktorý keď sa napočíta, tak sa script VYPNE
# ---------- (v sekundach)
MaxTime = 10
# ----------

Song = "RickRollAudio.mp3"

# Inicializujeme Pygame
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(Song)
pygame.mixer.music.play()

# ----------------------------------
#
# Created by Fattcat (Dominik Hulin)
#      For Prank Use ONLY !
#
# ----------------------------------



# Rozmery obrazovky
screen_width = 1920
screen_height = 1080

# Vytvorenie okna bez okrajov a pozadia
screen = pygame.display.set_mode((screen_width, screen_height), pygame.NOFRAME)
pygame.display.set_caption('Moving GIF')

# Screenshot aktuálnej obrazovky
screenshot = ImageGrab.grab(bbox=(0, 0, screen_width, screen_height))
screenshot = screenshot.convert('RGBA')

# Načítanie screenshotu ako pozadia
background = pygame.image.fromstring(screenshot.tobytes(), screenshot.size, screenshot.mode)
background = pygame.transform.scale(background, (screen_width, screen_height))

# Nastavenie transparentnej farby pozadia
transparent_color = (0, 0, 0)
screen.set_colorkey(transparent_color)

# Načítanie GIFu s transparentnou farbou
gif = pygame.image.load('Christmass01.jpg').convert_alpha()
original_gif_rect = gif.get_rect()
gif = pygame.transform.scale(gif, (290, 290))  # Prispôsobte veľkosť podľa potreby

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
    
    CurrentTime = time.time()
    ElapsedTime = CurrentTime - StartTime
    if ElapsedTime >= MaxTime:
        break
    
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

    # Zobrazenie screenshotu ako pozadia
    screen.blit(background, (0, 0))

    # Zobrazenie gifu na aktuálnej pozícii
    screen.blit(gif, (x, y))

    # Aktualizácia obrazovky
    pygame.display.update()

    # Odstávka na simuláciu pohybu
    clock.tick(frame_delay)
    if keyboard.is_pressed("f7"):
        break
        # Ukončenie Pygame
pygame.quit()
