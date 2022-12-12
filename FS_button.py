from pygame import*

class Button():
    def __init__(self, x, y, image, imagetwo, imagebot):
        self.image = image
        self.imagetwo = imagetwo
        self.imagebot = imagebot
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, root, soundbot):
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
