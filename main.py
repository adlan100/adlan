import pygame.display
from pygame import *

pygame.init()
window = pygame.display.set_mode((500,500))
display.set_caption(' моя игра')
back = (32, 158, 135)
window.fill(back)
pic = image.load('59eb93e2b691815f4039adbc.jpg')
fon = transform.scale(pic,(500,500))
run = True
while run:
    time.delay(50)
    for e in event.get():
        if e.type == QUIT:
            run = False
    window.blit(pic,(0,0))
    pygame.display.update()