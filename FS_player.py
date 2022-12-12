from pygame import*

bg = 0
xbackground = 24

class Gato(sprite.Sprite):
    def __init__(self, position, x):
        super().__init__()
        self.sheet = image.load("Imagenes/Gato/spriteSheet.png")
        self.sheet.set_clip(Rect(830, 0, 254, 200))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.frame = 0
        self.right_states = {0: (830, 0, 254, 200),
                             1: (1124, 0, 260, 200),
                             2: (1410, 0, 250, 200),
                             3: (1707, 0, 250, 200),
                             4: (2015, 0, 227, 200),
                             5: (0, 0, 280, 200),
                             6: (295, 0, 202, 200),
                             7: (581, 0, 210, 200)}

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

    def handle_event(self, evento, x):
        global xbackground, bg

        if evento.type == KEYDOWN:
            if evento.key == K_RIGHT:
                self.clip(self.right_states)
                self.rect.x += 183
                xbackground += 183
                if self.rect.x >= 946:
                    self.rect.x = x
                if xbackground < 946:
                    bg = 0
                    print("SIGUE CERO")
                else:
                    print("CAMBIO")
                    bg = 1
                    if xbackground > 2076:
                        bg = 0
                        xbackground = x
                print(xbackground)
            if evento.key == K_ESCAPE:
                quit()
                exit()

            """elif evento.key == pygame.K_LEFT:
                self.clip(self.right_states)
                self.rect.x -= 183
                xbackground -= 183
                if self.rect.x < x:
                    self.rect.x = x"""

            #print(self.rect.x)


        if evento.type == KEYUP:
            if evento.key == K_RIGHT:
                self.clip(self.right_states[0])
            """elif evento.key == pygame.K_LEFT:
                self.clip(self.right_states[0])"""

        self.image = self.sheet.subsurface(self.sheet.get_clip())

        return bg


