import pygame


class Gato(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.sheet = pygame.image.load("Imagenes/Gato/spriteSheet.png")
        self.sheet.set_clip(pygame.Rect(0, 0, 37, 32))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.frame = 0
        self.right_states = {0: (0, 0, 37, 32),
                             1: (37, 0, 37, 32),
                             2: (74, 0, 37, 32),
                             3: (111, 0, 37, 32),
                             4: (148, 0, 37, 32),
                             5: (185, 0, 37, 32),
                             6: (222, 0, 37, 32),
                             7: (259, 0, 37, 32)}

    def get_frame(self, frame_set):
        self.frame += 1
        if self.frame > (len(frame_set) - 1):
            self.frame = 0
        return frame_set[self.frame]

    def clip(self, clipped_rect):
        if type(clipped_rect) is dict:
            self.sheet.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
        else:
            self.sheet.set_clip(pygame.Rect(clipped_rect))
        return clipped_rect

    def update(self, direction):
        if direction == "right":
            self.clip(self.right_states)
            self.rect.x += 183
        if direction == "stand_right":
            self.clip(self.right_states[0])
        self.image = self.sheet.subsurface(self.sheet.get_clip())

    def handle_event(self, evento):
        if evento.type == pygame.KEYDOWN:
            if evento.type == pygame.K_RIGHT:
                self.update("right")
        if evento.type == pygame.KEYUP:
            if evento.type == pygame.K_RIGHT:
                self.update("stand_right")
