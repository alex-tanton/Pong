import pygame

class Object(pygame.sprite.Sprite):
    def __init__(self, position: tuple, size: tuple, image_path: str, group: pygame.sprite.Group):
        super().__init__(group)

        # ---------- ATTRIBUTE SETUP ---------- #
        self.position = position
        self.size = size
        self.image_path = image_path

    def set_image(self):
        # Creates and draws sprite image, anchored from top left
        self.image = pygame.image.load(self.image_path)
        self.image = pygame.transform.scale(self.image, self.size)

        self.surf = pygame.Surface(self.size).convert_alpha()
        self.surf.fill((0, 0, 0, 0))

        self.rect = self.surf.get_rect(topleft = self.position)
        self.surf.blit(self.image, (0, 0))

    def update(self):
        self.set_image()