import sys
from FS_button import *
from FS_player import*

init()

#M U S I C A  Y  S O N I D O
mixer.init()
mixer.music.load("Musica/musciakids.mp3")
mixer.music.set_volume(.2)
mixer.music.play(900)
soundbot = mixer.Sound("Musica/boton.wav")

#V E N T A N A
alto = 700
ancho = 1106
root = display.set_mode((ancho, alto))
display.set_caption("¡Contemos!")
ico = image.load("gato.ico")
display.set_icon(ico)

#C O L O R E S
naranja = Color(212, 139, 11)
negro = Color(0, 0, 0)

#F U E N T E S
font1 = font.SysFont('Fuentes/Golden Age Shad', 72)

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
x = 20
y = 380
    #Booleanos
game_start = False
game = True
    #Otros
clock = time.Clock()
player = Gato((x, y), x)


def imprinNum(saltjugador):

    i = 5*saltjugador

    txt1=[font1.render(str(i-4), 0, negro),
          font1.render(str(i-3), 0, negro),
          font1.render(str(i-2), 0, negro),
          font1.render(str(i-1), 0, negro),
          font1.render(str(i), 0, negro)]

    root.blit(txt1[0], (130, 617))
    root.blit(txt1[1], (330, 617))
    root.blit(txt1[2], (530, 617))
    root.blit(txt1[3], (730, 617))
    root.blit(txt1[4], (930, 617))




def juegomain(evento):

    saltjugador = player.handle_event(root, fond_prins, evento, x)

    if pause_button.draw(root, soundbot):
        pass
    imprinNum(saltjugador)
    root.blit(life_bar[3], (588, 10))
    root.blit(player.image, player.rect)

    clock.tick(10)

def juegomenu():
    global x,game, game_start

    evento = event.get()
    while game:
        root.blit(fond, (0, 0))
        root.blit(logo, (24, -20))

        for evento in event.get():
            if evento.type == QUIT:
                game = False

        if game_start:
            juegomain(evento)

        else:
            if jug_button.draw(root, soundbot):
                game_start = True
                print("Start")

            if sal_button.draw(root, soundbot):
                quit()
                exit()

        display.update()
        #pygame.display.flip()

juegomenu()
