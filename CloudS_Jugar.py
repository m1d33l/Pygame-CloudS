import pygame, sys
from pygame.locals import *
from time import sleep
from random import randint

#Variables. Inicializar:
posX,posY,posXfry,posXenemigo = 200,120,40,380
signo,var,SUELO = -10,0,120
Mov_derecha,Activar =  False,False
velocidad,Contador,e = 10,0,0
VidaDeFry,VidaDeEnemigo,VidaDePersonaje = 550,1280,100
iruta,druta = "IMG_Izquierda/","IMG_Derecha/"
#IMAGENES:
FRY = pygame.image.load("fry0.png")
Enemigo = pygame.image.load("Zoidbergs/Zoidbergs-0.png")
R_Enemigo = Enemigo.get_rect()  #Devuelve un rectangulo de la imagen
ImagenFondo = pygame.image.load("Fondos/Fondo0.jpg")
I_quieto = pygame.image.load("IMG_Izquierda/Quieto/Quieto.png")
D_quieto = pygame.image.load("IMG_Derecha/Quieto/Quieto.png")
CARGA = D_quieto

#Ventana: Parametros iniciales
pygame.init()
ventana = pygame.display.set_mode((500,281))
pygame.display.set_caption("CloudS")
FuenteS = pygame.font.SysFont("Arial",23)
VidaFry = FuenteS.render(str(VidaDeFry),0,(210,0,50))
VidaEnemigo = FuenteS.render(str(VidaDeEnemigo),0,(210,0,50))
VidaPersonaje = FuenteS.render("Vida del personaje: "+str(VidaDePersonaje),0,(50,10,255))

def CargaInicial():
    ventana.blit(ImagenFondo,(0,0))
    ventana.blit(CARGA,(posX,posY))
    ventana.blit(FRY,(posXfry,130))
    ventana.blit(Enemigo,(posXenemigo,175))
    ventana.blit(VidaFry,(90,100))
    ventana.blit(VidaEnemigo,(400,140))
    ventana.blit(VidaPersonaje,(30,20))

#Ejecucion:
while True:
    CargaInicial()
    signo = -10

    for evento in pygame.event.get():
        #Cerrar ventana:
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
        #Presionar tecla: Movimiento Lateral
            elif evento.type == pygame.KEYDOWN:
                if evento.key == K_LEFT:
                    Mov_derecha = False
                    CARGA = I_quieto
                    posX -= velocidad
                    Contador = Contador + 1
                    if Contador >= 6 or evento.key == K_RIGHT or evento.key == K_s:
                        Contador = 1
                    Correr = pygame.image.load(iruta+"Correr/Correr"+str(Contador)+".png")
                    CARGA = Correr

                elif evento.key == K_RIGHT:
                    Mov_derecha = True
                    CARGA = D_quieto
                    posX += velocidad
                    Contador = Contador + 1
                    if Contador >= 6 or evento.key == K_LEFT or evento.key == K_s:
                        Contador = 1
                    Correr = pygame.image.load(druta+"Correr/Correr"+str(Contador)+".png")
                    CARGA = Correr

                #Salto:
                elif evento.key == K_UP:
                    for var in range(0,160,10):
                        posY+=signo
                        if posY < 50:
                            signo = 10
                            if Mov_derecha == False:
                                CARGA = pygame.image.load(iruta+"Correr/Correr3.png")
                            else:
                                CARGA = pygame.image.load(druta+"Correr/Correr3.png")
                        if var == 150:
                            if Mov_derecha == False:
                                CARGA = pygame.image.load(iruta+"Quieto/Quieto.png")
                            else:
                                CARGA = pygame.image.load(druta+"Quieto/Quieto.png")
                        CargaInicial()
                        pygame.time.wait(55)
                        pygame.display.update()
                #Defenderse
                elif evento.key == K_DOWN:
                    if Mov_derecha == False:
                        CARGA = pygame.image.load(iruta+"Quieto/Defensa.png")
                    else:
                        CARGA = pygame.image.load(druta+"Quieto/Defensa.png")
                    print "Defensa"

        #Presionar tecla: Atacar_1
                elif evento.key == K_s:
                    for e in range(1,7):
                        if Mov_derecha == False:
                            Atacar = pygame.image.load(iruta+"Ataque_1/Ataque1"+str(e)+".png")
                        else:
                            Atacar = pygame.image.load(druta+"Ataque_1/Ataque1"+str(e)+".png")
                        #Movimiento de los enemigos:
                        if posX <= posXfry and posX >= (posXfry-40):
                            print "Has golpeado a Fry!"
                            VidaDeFry -= 10
                            VidaFry = FuenteS.render(str(VidaDeFry),0,(20,60,80))
                            for e in range(0,4): #0~3
                                FRY = pygame.image.load("fry"+str(e)+".png")
                                CargaInicial()
                                pygame.time.wait(80)
                                pygame.display.update()
                                Contra = randint(0,10)
                                print "Contra: "+str(Contra)
                            if Contra>= 0 and Contra<=4:
                                posX = posX+100
                                VidaDePersonaje -= 10
                                VidaPersonaje = FuenteS.render("Vida del personaje: "+str(VidaDePersonaje),0,(0,0,0))

                        elif posX >= (posXenemigo-100) and posX <= (posXenemigo):
                            print "Has golpeado a Zoidbergs!"
                            VidaDeEnemigo -= 50
                            VidaEnemigo = FuenteS.render(str(VidaDeEnemigo),0,(20,60,80))
                            for e in range(0,10): #0~33
                                Enemigo = pygame.image.load("Zoidbergs/Zoidbergs-"+str(e)+".png")
                                CargaInicial()
                                pygame.time.wait(50)
                                pygame.display.update()
                                Activar = True
                            if Activar == True:
                                posX = posX-60
                        CARGA = Atacar
                        CargaInicial()
                        pygame.time.wait(90)
                        pygame.display.update()
        #Presionar tecla: Atacar_2
                elif evento.key == K_d:
                    for e in range(1,10):
                        if Mov_derecha == False:
                            Atacar = pygame.image.load(iruta+"Ataque_2/Ataque2"+str(e)+".png")
                        else:
                            Atacar = pygame.image.load(druta+"Ataque_2/Ataque2"+str(e)+".png")
                        CARGA = Atacar
                        CargaInicial()
                        pygame.time.wait(110)
                        pygame.display.update()

#Ejecutar/Actualizar ventana:
    pygame.display.update()
