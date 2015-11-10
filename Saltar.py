import pygame, sys
from pygame.locals import *
from time import sleep

pygame.init()
ventana = pygame.display.set_mode((500,281))
pygame.display.set_caption("Hola Mundo")

miFuente = pygame.font.Font(None,45)
Coordenadas = pygame.font.SysFont("Arial",15)
x,y,var,suelo=200,100,0,100
signo = -10
while True:
    Asterisco = miFuente.render("*",0,(100,160,255))  #Texto/Antialias/ColorLetras/ColorFondo
    y000 = Coordenadas.render("Y:   0  -    -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   - ",0,(255,255,255))
    y120 = Coordenadas.render("Y: 120  -    -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   - ",0,(255,255,255))
    y200 = Coordenadas.render("Y: 200  -    -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   - ",0,(255,255,255))
    x000 = Coordenadas.render("X:   0  ",0,(255,255,100))
    x100 = Coordenadas.render("X: 100  ",0,(255,255,100))
    x200 = Coordenadas.render("X: 200  ",0,(255,255,100))
    x300 = Coordenadas.render("X: 300  ",0,(255,255,100))
    x400 = Coordenadas.render("X: 400  ",0,(255,255,100))
    ventana.fill((50,50,50))
    for evento in pygame.event.get():
        ventana.blit(y000,(10,0))
        ventana.blit(y120,(10,120))
        ventana.blit(y200,(10,200))
        ventana.blit(x000,(0,260))
        ventana.blit(x100,(100,260))
        ventana.blit(x200,(200,260))
        ventana.blit(x300,(300,260))
        ventana.blit(x400,(400,260))
        #Cerrar ventana:
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
        #Presionar tecla:
        elif evento.type == pygame.KEYDOWN:
            for var in range(100,190,10):
                if evento.key == K_s:
                    x = 200
                    y = y+signo
                    if y <= 50:
                        signo = 10
                    #print "Y: "+str(y)
                    ventana.blit(Asterisco,(x,y))
                    pygame.time.wait(150)
                    pygame.display.update()
                if evento.key == K_d:
                    x = x + 10
                    y = y + 10
                    print ">>>X: "+str(x)
                    ventana.fill((100,100,100))

                    ventana.blit(Asterisco,(x,y))
                    pygame.time.wait(150)
                    pygame.display.update()

    pygame.display.update()
