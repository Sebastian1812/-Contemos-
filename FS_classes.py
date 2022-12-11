from pygame import*
import pygame

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
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            root.blit(self.imagetwo, (self.rect.x, self.rect.y))
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                root.blit(self.imagebot, (self.rect.x, self.rect.y))
                pygame.mixer.Sound.play(soundbot)
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False


        return action
