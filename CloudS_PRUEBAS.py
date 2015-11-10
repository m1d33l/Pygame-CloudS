import pygame, sys
from pygame.locals import *
from time import sleep

pygame.init()
ventana = pygame.display.set_mode((500,281))
pygame.display.set_caption("Hola Mundo")

miFuente = pygame.font.Font(None,45)
Coordenadas = pygame.font.SysFont("Arial",15)

x,y,var=200,120,0

while True:
    Asterisco = miFuente.render("*",0,(100,160,255))  #Texto/Antialias/ColorLetras/ColorFondo
    y000 = Coordenadas.render("Y:   0  --------------------------------------------------------------------------- ",0,(255,255,255))
    y120 = Coordenadas.render("Y: 120  --------------------------------------------------------------------------- ",0,(255,255,255))
    y200 = Coordenadas.render("Y: 200  --------------------------------------------------------------------------- ",0,(255,255,255))


    ventana.fill((50,50,50))
    for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()

    ventana.blit(y000,(10,0))
    ventana.blit(y120,(10,120))
    ventana.blit(y200,(10,200))

    #for y in range(0,50,5):
    #    print "y:  "+str(y)
    #    if y > 25:
    #        for y in range (90,100,5):
    #            print "valor de y:  "+str(y)

    #            ventana.blit(Asterisco,(x,y))
    #            pygame.time.wait(150)
    #            pygame.display.update()
        #ventana.fill((50,50,50))

    pygame.display.update()
