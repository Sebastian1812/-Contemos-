import sys
from FS_button import *
from FS_player import *

init()

# M U S I C A  Y  S O N I D O
mixer.init()
mixer.music.load("Musica/musciakids.mp3")
mixer.music.set_volume(.2)
mixer.music.play(900)

# V E N T A N A
alto = 700
ancho = 1106
root = display.set_mode((ancho, alto))
display.set_caption("¡Contemos!")
ico = image.load("gato.ico")
display.set_icon(ico)

# C O L O R E S
naranja = Color(212, 139, 11)
negro = Color(0, 0, 0)

# F U E N T E S
font1 = font.SysFont('Fuentes/Golden Age Shad', 30)
font2 = font.SysFont('Fuentes/Golden Age Shad', 30)

# I M A G E N E S
logo = image.load("Imagenes/Contemos_log.png")
fond = image.load("Imagenes/Fondo/background.png")
bjugar = [image.load("Imagenes/Botones/b1_jugar.png").convert_alpha(),
          image.load("Imagenes/Botones/b1_5_jugar.png").convert_alpha(),
          image.load("Imagenes/Botones/b2_jugar.png").convert_alpha()]
bsalir = [image.load("Imagenes/Botones/b1_salir.png").convert_alpha(),
          image.load("Imagenes/Botones/b1_5_salir.png").convert_alpha(),
          image.load("Imagenes/Botones/b2_salir.png").convert_alpha()]
fond_prins = [image.load("Imagenes/Fondo/juego/1.png"),
              image.load("Imagenes/Fondo/juego/2.png")]
b_pausa = [image.load("Imagenes/Botones/pause_1.png").convert_alpha(),
           image.load("Imagenes/Botones/pause_1_1.png").convert_alpha(),
           image.load("Imagenes/Botones/pause_2.png").convert_alpha()]
pausafond = image.load("Imagenes/Fondo/pausa.png")

breanudar = [image.load("Imagenes/Botones/b1_reanudar.png").convert_alpha(),
             image.load("Imagenes/Botones/b1_5_reanudar.png").convert_alpha(),
             image.load("Imagenes/Botones/b2_reanudar.png").convert_alpha()]

bsi = [image.load("Imagenes/Botones/b1_si.png"),
       image.load("Imagenes/Botones/b1_5_si.png"),
       image.load("Imagenes/Botones/b2_si.png")]
bno = [image.load("Imagenes/Botones/b1_no.png"),
       image.load("Imagenes/Botones/b1_5_no.png"),
       image.load("Imagenes/Botones/b2_no.png")]


# B O T O N E S
jug_button = Button(701, 398, bjugar)
sal_button = Button(701, 529, bsalir)
pause_button = Button(10, 125, b_pausa)
reanud_button = Button(408, 231, breanudar)
pausesal_button = Button(408, 401, bsalir)
si_button = Button(408, 274, bsi)
no_button = Button(408, 441, bno)

# V A R I A B L E S
# Enteros
x = 20
y = 380
# Booleanos
game_start = False
game = True
game_pause = False
game_over = False
# Otros
clock = time.Clock()
player = Gato((x, y), x)


def imprinNum(saltjugador):
    i = 5 * saltjugador

    txt1 = [font2.render(str(i - 4), 0, negro),
            font2.render(str(i - 3), 0, negro),
            font2.render(str(i - 2), 0, negro),
            font2.render(str(i - 1), 0, negro),
            font2.render(str(i), 0, negro)]

    if i < 10:
        root.blit(txt1[0], (108, 648))
        root.blit(txt1[1], (312, 648))
        root.blit(txt1[2], (510, 648))
        root.blit(txt1[3], (708, 648))
        root.blit(txt1[4], (912, 648))
    else:
        root.blit(txt1[0], (103, 648))
        root.blit(txt1[1], (305, 648))
        root.blit(txt1[2], (503, 648))
        root.blit(txt1[3], (706, 648))
        root.blit(txt1[4], (908, 648))


def juegomain(evento):
    global game_pause, game, game_over
    if not game_pause:
        jugador = player.handle_event(root, fond_prins, evento, x)
        saltjugador = jugador
        if pause_button.draw(root):
            game_pause = True
        imprinNum(saltjugador)
        root.blit(player.image, player.rect)
    else:
        root.blit(pausafond, (0, 0))
        if pausesal_button.draw(root):
            game = False
        if reanud_button.draw(root):
            game_pause = False




def juegomenu():
    global x, game, game_start, game_over

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
            if jug_button.draw(root):
                game_start = True

            if sal_button.draw(root):
                quit()
                exit()

        display.update()
        # pygame.display.flip()


juegomenu()
