import sys
from FS_button import *
from FS_player import*

pygame.init()

#M U S I C A  Y  S O N I D O
pygame.mixer.init()
pygame.mixer.music.load("Musica/musciakids.mp3")
pygame.mixer.music.set_volume(.2)
pygame.mixer.music.play(900)
soundbot = pygame.mixer.Sound("Musica/boton.wav")

#V E N T A N A
alto = 700
ancho = 1106
root = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("¡Contemos!")
ico = pygame.image.load("gato.ico")
pygame.display.set_icon(ico)

#C O L O R E S
naranja = pygame.Color(212, 139, 11)
negro = pygame.Color(0, 0, 0)

#F U E N T E S
Fuente = pygame.font.SysFont("Fuentes/Golden Age Shad.ttf", 100)
font1 = pygame.font.SysFont('Fuentes/Golden Age Shad.ttf', 72)


#I M A G E N E S
logo = image.load("Imagenes/Contemos_log.png")
fond = image.load("Imagenes/Fondo/background.png")
bjugar = [image.load("Imagenes/Botones/b1_jugar.png").convert_alpha(),
          image.load("Imagenes/Botones/b1_5_jugar.png").convert_alpha(),
          image.load("Imagenes/Botones/b2_jugar.png").convert_alpha()]
bsalir = [image.load("Imagenes/Botones/b1_salir.png").convert_alpha(),
          image.load("Imagenes/Botones/b1_5_salir.png").convert_alpha(),
          image.load("Imagenes/Botones/b2_salir.png").convert_alpha()]
fond_prins = [image.load("Imagenes/Fondo/juego/1.png"), image.load("Imagenes/Fondo/juego/2.png")]
life_bar = [image.load("Imagenes/Gato/Lifes/0.png"), image.load("Imagenes/Gato/Lifes/1.png"),
            image.load("Imagenes/Gato/Lifes/2.png"), image.load("Imagenes/Gato/Lifes/3.png"),
            image.load("Imagenes/Gato/Lifes/4.png"), image.load("Imagenes/Gato/Lifes/5.png"),
            image.load("Imagenes/Gato/Lifes/6.png"), image.load("Imagenes/Gato/Lifes/7.png")]
b_pausa = [image.load("Imagenes/Botones/pause_1.png").convert_alpha(),
           image.load("Imagenes/Botones/pause_1_1.png").convert_alpha(),
           image.load("Imagenes/Botones/pause_2.png").convert_alpha()]

#B O T O N E S
jug_button = Button(701, 398, bjugar[0], bjugar[1], bjugar[2])
sal_button = Button(701, 529, bsalir[0], bsalir[1], bsalir[2])
pause_button = Button(10, 119, b_pausa[0], b_pausa[1], b_pausa[2])

#V A R I A B L E S
    #Enteros
x = -60
y = 400
xbackground = x
    #Booleanos
game_start = False
game = True
    #Otros
clock = pygame.time.Clock()
player = Gato((x, y), x)


def juegomain(evento):
    if player.handle_event(evento, x) == 0:
        root.blit(fond_prins[0], (0, 0))

    else:
        root.blit(fond_prins[1], (0, 0))
    root.blit(life_bar[3], (588, 10))
    root.blit(player.image, player.rect)
    if pause_button.draw(root, soundbot):
        pass

    clock.tick(10)

def juegomenu():
    global x,game, game_start

    evento = event.get()
    while game:
        root.blit(fond, (0, 0))
        root.blit(logo, (24, -20))

        for evento in event.get():
            if evento.type == pygame.QUIT:
                game = False

        if game_start:
            juegomain(evento)

        else:
            if jug_button.draw(root, soundbot):
                game_start = True
                print("Start")

            if sal_button.draw(root, soundbot):
                pygame.quit()
                sys.exit()

        pygame.display.update()
        #pygame.display.flip()

juegomenu()
