import pygame


class Gato(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.sheet = pygame.image.load("Imagenes/Gato/spriteSheet.png")
        self.sheet.set_clip(pygame.Rect(0, 0, 280, 200))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.frame = 0
        self.right_states = {0: (0, 0, 280, 200),
                             1: (295, 0, 202, 200),
                             2: (581, 0, 210, 200),
                             3: (830, 0, 254, 200),
                             4: (1124, 0, 260, 200),
                             5: (1410, 0, 250, 200),
                             6: (1707, 0, 250, 200),
                             7: (2015, 0, 227, 200)}





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
        if direction == 'left':
            self.clip(self.left_states)
            self.rect.x -= 5
        if direction == 'right':
            self.clip(self.right_states)
            self.rect.x += 5
        if direction == 'up':
            self.clip(self.up_states)
            self.rect.y -= 5
        if direction == 'down':
            self.clip(self.down_states)
            self.rect.y += 5


    def handle_event(self, evento):
        if evento.type == pygame.KEYDOWN:
            if evento.type == pygame.K_RIGHT:
                self.update('right')
        if evento.type == pygame.KEYUP:
            if evento.type == pygame.K_RIGHT:
                self.update('stand_right')
