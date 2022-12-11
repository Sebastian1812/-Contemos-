import tkinter
from tkinter import*
from tkinter import messagebox
import sys
from pygame.locals import*
from FS_classes import*

alto = 700
ancho = 1106

pygame.init()

pygame.mixer.init()
pygame.mixer.music.load("Musica/musciakids.mp3")
pygame.mixer.music.set_volume(.2)
pygame.mixer.music.play(900)
soundbot = pygame.mixer.Sound("Musica/boton.wav")

root = pygame.display.set_mode((ancho,alto))
pygame.display.set_caption("¡Contemos!")
ico = pygame.image.load("gato.ico")
pygame.display.set_icon(ico)

naranja = pygame.Color(212,139,11)
negro = pygame.Color(0,0,0)

Fuente = pygame.font.SysFont("Fuentes/Golden Age Shad.ttf",100)
font1 = pygame.font.SysFont('Fuentes/Golden Age Shad.ttf', 72)


logo = image.load("Imagenes/Contemos_log.png")
fond = image.load("Imagenes/Fondo/background.png")
bjugar = [image.load("Imagenes/Botones/b1_jugar.png").convert_alpha(),image.load("Imagenes/Botones/b1_5_jugar.png").convert_alpha(),image.load("Imagenes/Botones/b2_jugar.png").convert_alpha()]
bsalir = [image.load("Imagenes/Botones/b1_salir.png").convert_alpha(),image.load("Imagenes/Botones/b1_5_salir.png").convert_alpha(),image.load("Imagenes/Botones/b2_salir.png").convert_alpha()]
fond_prins = [image.load("Imagenes/Fondo/juego/1.png"),image.load("Imagenes/Fondo/juego/2.png")]
life_bar = [image.load("Imagenes/Gato/Lifes/0.png"),image.load("Imagenes/Gato/Lifes/1.png"),image.load("Imagenes/Gato/Lifes/2.png"),image.load("Imagenes/Gato/Lifes/3.png"),image.load("Imagenes/Gato/Lifes/4.png"),image.load("Imagenes/Gato/Lifes/5.png"),image.load("Imagenes/Gato/Lifes/6.png"),image.load("Imagenes/Gato/Lifes/7.png")]
b_pausa = [image.load("Imagenes/Botones/pause_1.png").convert_alpha(),image.load("Imagenes/Botones/pause_1_1.png").convert_alpha(),image.load("Imagenes/Botones/pause_2.png").convert_alpha()]

#img2 = font2.render('didot.ttc', True, GREEN)



#standar


jug_button = Button(701, 398, bjugar[0],bjugar[1],bjugar[2])
sal_button = Button(701, 529, bsalir[0],bsalir[1],bsalir[2])
pause_button = Button(10, 119, b_pausa[0],b_pausa[1],b_pausa[2])

root.blit(fond,(0,0))


vel = 183
posx = 75
posy = 497
derech = True
game_start = False

class gatoSalto(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.gato = pygame.image.load("Imagenes/Gato/Gsptrite/Gato/1.png")

        self.rect = self.gato.get_rect()

        self.rect.x = 22
        self.rect.y = 460

        self.gatoSalto = []
        self.vidas = True

    def dibujar(self,ventana):
        ventana.blit(self.gato,self.rect)

def juegomain(jugador):
    root.blit(fond_prins[0],(0,0))
    root.blit(life_bar[3],(588,10))
    jugador.dibujar(root)
    if  pause_button.draw(root, soundbot) == True:
        pass



def juegomenu():
    global vel,posy,posx,derech,juegocontemos,game_start


    jugador = gatoSalto()
    while True:
        root.blit(fond,(0,0))
        root.blit(logo,(24,-20))
        #root.blit(fig,(posx,posy))
        #tiempo = pygame.time.get_ticks()/1000

        if  game_start:
            juegomain(jugador)

        else:
            if  jug_button.draw(root, soundbot) == True:
                game_start = True
                print("Start")


            if  sal_button.draw(root, soundbot) == True:
                pygame.quit()
                sys.exit()
                print("End")

        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
        if evento.type == pygame.KEYDOWN:
            if evento.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

        pygame.display.update()

juegomenu()
