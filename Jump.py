import pygame, sys
from pygame.locals import *
from time import sleep

pygame.init()
ventana = pygame.display.set_mode((500,281))
pygame.display.set_caption("Hola Mundo")

miFuente = pygame.font.Font(None,45)
Coordenadas = pygame.font.SysFont("Arial",15)
x,y,var=200,100,0
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
        def actualizar(x,y):
            ventana.blit(Asterisco,(x,y))
            pygame.time.wait(150)
            pygame.display.update()
        #Cerrar ventana:
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
        #Presionar tecla:
        elif evento.type == pygame.KEYDOWN:
            if evento.key == K_UP:
                for var in range(0,110,10):
                    y=y+signo
                    print "Subir: "+str(y)
                    if y < 50:
                        signo = 10
                        Asterisco = miFuente.render("*",0,(255,0,0))
                        print "Bajar: "+str(y)
                    actualizar(x,y)

            elif evento.key == K_RIGHT:
                for var in range(0,50,10):
                    x=x+25
                    y=y+10
                    Asterisco = miFuente.render("*",0,(255,255,0))
                    actualizar(x,y)
            elif evento.key == K_LEFT:
                x=x-10
                actualizar(x,y)
            if evento.key == K_DOWN:
                y=y+10
                actualizar(x,y)

    #pygame.display.update()
