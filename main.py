import pygame

ancho=800
largo=600


pantalla=pygame.display.set_mode((ancho,largo))


running = True

for event in pygame.event.get():

    if event.type == pygame.QUIT:

        running = False