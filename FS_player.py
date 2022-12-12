from pygame import *
from random import *

bg = 1
xbackground = 24
n1 = 0
n2 = 0

init()

# C O L O R E S
naranja = Color(212, 139, 11)
negro = Color(0, 0, 0)

# F U E N T E S
font1 = font.SysFont('Fuentes/Golden Age Shad', 80)



def resultado(n1, n2, resul):
    check = n1 + n2
    puntos = 10
    if resul == check:
        print("CORRECTO")
        return True
    else:
        print("INCORRECTO")
        return False


class Gato(sprite.Sprite):
    def __init__(self, position, x):
        super().__init__()
        self.sheet = image.load("Imagenes/Gato/spriteSheet.png")
        self.sheet.set_clip(Rect(830, 0, 254, 200))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.resul = 1
        self.puntos = 0
        self.problem = True
        self.frame = 0
        self.right_states = {0: (830, 0, 254, 200),
                             1: (1124, 0, 260, 200),
                             2: (1410, 0, 250, 200),
                             3: (1707, 0, 250, 200),
                             4: (2015, 0, 227, 200),
                             5: (0, 0, 280, 200),
                             6: (295, 0, 202, 200),
                             7: (581, 0, 210, 200)}
        self.buton = False

    def get_frame(self, frame_set):
        self.frame += 1
        if self.frame > (len(frame_set) - 1):
            self.frame = 0
        return frame_set[self.frame]

    def clip(self, clipped_rect):
        if type(clipped_rect) is dict:
            self.sheet.set_clip(Rect(self.get_frame(clipped_rect)))
        else:
            self.sheet.set_clip(Rect(clipped_rect))
        return clipped_rect

    def handle_event(self, root, f1, evento, x):
        global xbackground, bg, fond, n1, n2

        if xbackground < 948:
            root.blit(f1[0], (0, 0))
        else:
            root.blit(f1[1], (0, 0))


        if self.problem:
            n1 = self.resul
            n2 = randrange(1, 10)
            self.problem = False

        # T E X T O S
        txt=[font1.render(str(n1), 1, negro),
             font1.render(str(n2), 1, negro),
             font1.render(str(self.resul), 1, negro),]
        points = font1.render(str(self.puntos), 1, negro)

        root.blit(txt[0], (270, 315))
        root.blit(txt[1], (543, 315))
        root.blit(txt[2], (815, 315))
        root.blit(points, (200, 50))

        print(f"{n1} y {n2}")

        if evento.type == KEYDOWN and self.buton == False:
            if evento.key == K_RETURN:
                if resultado(n1,n2,self.resul):
                    self.puntos += 10
                    self.problem = True
                else:
                    bg = 1
                    self.resul = 1
                    self.problem = True
                    self.rect.x = x
                    xbackground = x
            if self.buton == False:
                self.buton = True
                if evento.key == K_RIGHT:
                    self.clip(self.right_states)
                    self.rect.x += 200
                    self.resul += 1
                    xbackground += 200
                    if self.rect.x >= 946:
                        self.rect.x = x
                        bg += 1
                    if xbackground >= 1892:
                        xbackground = x
                elif evento.key == K_ESCAPE:
                    quit()
                    exit()

            """elif evento.key == pygame.K_LEFT:
                self.clip(self.right_states)
                self.rect.x -= 183
                xbackground -= 183
                if self.rect.x < x:
                    self.rect.x = x"""

            # print(self.rect.x)

        if evento.type == KEYUP:
            if evento.key == K_RIGHT:
                self.clip(self.right_states[0])
                self.buton = False
            elif evento.key == K_RETURN:
                self.buton = False
            """elif evento.key == pygame.K_LEFT:
                self.clip(self.right_states[0])"""

        self.image = self.sheet.subsurface(self.sheet.get_clip())

        return bg
