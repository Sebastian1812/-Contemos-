from pygame import*

mixer.init()
soundbot = mixer.Sound("Musica/boton.wav")

class Button():
    def __init__(self, x, y, imagenes):
        self.image = imagenes[0]
        self.imagetwo = imagenes[1]
        self.imagebot = imagenes[2]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, root):
        action = False
        root.blit(self.image, (self.rect.x, self.rect.y))
        pos = mouse.get_pos()
        if self.rect.collidepoint(pos):
            root.blit(self.imagetwo, (self.rect.x, self.rect.y))
            if mouse.get_pressed()[0] == 1 and self.clicked == False:
                root.blit(self.imagebot, (self.rect.x, self.rect.y))
                mixer.Sound.play(soundbot)
                self.clicked = True
                action = True
        if mouse.get_pressed()[0] == 0:
            self.clicked = False
        return action
