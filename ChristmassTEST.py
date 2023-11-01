import pygame
import sys

# Inicializujeme Pygame
pygame.init()

# Nastavíme veľkosť obrazovky na aktuálnu veľkosť obrazovky
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
width, height = screen.get_size()

# Nastavíme transparentné pozadie
screen.fill((0, 0, 0))
screen.set_colorkey((0, 0, 0))

# Načítame GIF súbor
gif = pygame.image.load("ChristmassGIF.gif")

# Počiatočná pozícia a rýchlosť
x, y = width // 2, height // 2
speed_x, speed_y = 5, 5

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Pohyb gifu
    x += speed_x
    y += speed_y

    # Odrážanie od okrajov obrazovky
    if x < 0 or x + gif.get_width() > width:
        speed_x = -speed_x
    if y < 0 or y + gif.get_height() > height:
        speed_y = -speed_y

    # Znovu vyplníme obrazovku transparentným pozadím
    screen.fill((0, 0, 0))
    
    # Zobrazenie gifu na aktuálnej pozícii
    screen.blit(gif, (x, y))
    
    # Zobrazíme na obrazovku
    pygame.display.flip()
