import pygame, sys
from pygame.locals import *
from time import sleep

#Variables:
posX,posY = 200,100
Mov_izquierda, Mov_derecha = True, False
velocidad = 10
Contador,e= 0,0
iruta = "Proyecto_CloudS/IMG_Izquierda/"
druta = "Proyecto_CloudS/IMG_Derecha/"
#IMAGENES:
FRY = pygame.image.load("Proyecto_CloudS/fry.png")
R_FRY = FRY.get_rect()  #Devuelve un rectangulo de la imagen
ImagenFondo = pygame.image.load("Proyecto_CloudS/TamFondo0.jpg")
I_quieto = pygame.image.load("Proyecto_CloudS/IMG_Izquierda/Quieto/Quieto.png")
D_quieto = pygame.image.load("Proyecto_CloudS/IMG_Derecha/Quieto/Quieto.png")
CARGA = D_quieto

#Ventana: Parámetros iniciales
pygame.init()
ventana = pygame.display.set_mode((500,281))
pygame.display.set_caption("CloudS")

#Ejecución:
while True:
    ventana.blit(ImagenFondo,(0,0))
    ventana.blit(CARGA,(posX,posY))
    ventana.blit(FRY,(75,110))

    for evento in pygame.event.get():
        #Cerrar ventana:
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
        #Presionar tecla: Movimiento Lateral
        pulsar = pygame.key.get_pressed
            elif evento.type == pygame.KEYDOWN:
                if pulsar[K_LEFT]:
                #if evento.key == K_LEFT:
                    Mov_izquierda = True
                    Mov_derecha = False
                    CARGA = I_quieto
                    posX -= velocidad
                    Contador = Contador + 1
                    if Contador >= 6 or evento.key == K_RIGHT or evento.key == K_s:
                        Contador = 1
                    Correr = pygame.image.load(iruta+"Correr/Correr"+str(Contador)+".png")
                    CARGA = Correr
                elif evento.key == K_RIGHT:
                    Mov_izquierda = False
                    Mov_derecha = True
                    CARGA = D_quieto
                    posX += velocidad
                    Contador = Contador + 1
                    if Contador >= 6 or evento.key == K_LEFT or evento.key == K_s:
                        Contador = 1
                    Correr = pygame.image.load(druta+"Correr/Correr"+str(Contador)+".png")
                    CARGA = Correr
                elif evento.key == K_UP:
                    CARGA = pygame.image.load(iruta+"Quieto/Defensa.png")
                    posY =- 10
                elif evento.key == K_DOWN:
                    CARGA = pygame.image.load(iruta+"Quieto/Defensa.png")
                    posY =+ 10

        #Presionar tecla: Atacar_1
                elif evento.key == K_s and Mov_izquierda == True:
                    Contador = Contador + 1
                    if Contador >= 5:
                        Contador = 1
                    Atacar = pygame.image.load(iruta+"Ataque_1/Ataque1"+str(Contador)+".png")
                    CARGA = Atacar

                elif evento.key == K_s and Mov_derecha == True:
                    Contador = Contador + 1
                    if Contador >= 5:
                        Contador = 1
                    Atacar = pygame.image.load(druta+"Ataque_1/Ataque1"+str(Contador)+".png")
                    CARGA = Atacar

        #Presionar tecla: Atacar_2
                elif evento.key == K_d and Mov_izquierda == True:
                    Contador = Contador + 1
                    if Contador >= 8:
                        Contador = 1
                    Atacar = pygame.image.load(iruta+"Ataque_2/Ataque2"+str(Contador)+".png")
                    CARGA = Atacar

                elif evento.key == K_d and Mov_derecha == True:
                    Contador = Contador + 1
                    if Contador >= 8:
                        Contador = 1
                    Atacar = pygame.image.load(druta+"Ataque_2/Ataque2"+str(Contador)+".png")
                    CARGA = Atacar

#Ejecutar/Actualizar ventana:
    pygame.display.update()
