import pygame, sys
from pygame.locals import *
from random import randint                      #Crear números aleatorios

#Ventana: Parámetros iniciales
pygame.init()
ventana = pygame.display.set_mode((600,300))
pygame.display.set_caption("CloudS")

#IMAGENES:
D_quieto = pygame.image.load("Proyecto_CloudS/IMG_Derecha/Quieto/Quieto.png")
I_quieto = pygame.image.load("Proyecto_CloudS/IMG_Izquierda/Quieto/Quieto.png")

D_correr1 = pygame.image.load("Proyecto_CloudS/IMG_Derecha/Correr/Correr1.png")
D_correr2 = pygame.image.load("Proyecto_CloudS/IMG_Derecha/Correr/Correr2.png")
D_correr3 = pygame.image.load("Proyecto_CloudS/IMG_Derecha/Correr/Correr3.png")
D_correr4 = pygame.image.load("Proyecto_CloudS/IMG_Derecha/Correr/Correr4.png")
D_correr5 = pygame.image.load("Proyecto_CloudS/IMG_Derecha/Correr/Correr5.png")
D_correr6 = pygame.image.load("Proyecto_CloudS/IMG_Derecha/Correr/Correr6.png")

I_correr1 = pygame.image.load("Proyecto_CloudS/IMG_Izquierda/Correr/Correr1.png")
I_correr2 = pygame.image.load("Proyecto_CloudS/IMG_Izquierda/Correr/Correr2.png")
I_correr3 = pygame.image.load("Proyecto_CloudS/IMG_Izquierda/Correr/Correr3.png")
I_correr4 = pygame.image.load("Proyecto_CloudS/IMG_Izquierda/Correr/Correr4.png")
I_correr5 = pygame.image.load("Proyecto_CloudS/IMG_Izquierda/Correr/Correr5.png")
I_correr6 = pygame.image.load("Proyecto_CloudS/IMG_Izquierda/Correr/Correr6.png")

#Variables:
posX = 200
posY = 100
velocidad = 8
Derecha = True
CARGA = D_quieto

#Ejecución:
while True:
    ventana.fill((255,255,255))
    ventana.blit(CARGA,(posX,posY))
    for evento in pygame.event.get():
        #Cerrar ventana:
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
        #Presionar tecla:
            elif evento.type == pygame.KEYDOWN:
                if evento.key == K_LEFT:
                    CARGA = I_quieto
                    posX -= velocidad
                elif evento.key == K_RIGHT:
                    CARGA = D_quieto
                    posX += velocidad
        #Liberar tecla:
            elif evento.type == pygame.KEYUP:
                if evento.key == K_LEFT:
                    print "Tecla izquierda liberada"
                elif evento.key == K_RIGHT:
                    print "Tecla derecha liberada"
#Ejecutar/Actualizar ventana:
    pygame.display.update()
