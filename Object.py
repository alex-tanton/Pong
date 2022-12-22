import pygame

class Object(pygame.sprite.Sprite):
    def __init__(self, position, size, image_path, group):
        super().__init__(group)

        self.position = position
        self.size = size
        self.image_path = image_path

    def set_image(self):
        self.image = pygame.image.load(self.image_path)
        self.image = pygame.transform.scale(self.image, self.size)

        self.surf = pygame.Surface(self.size).convert_alpha()
        self.rect = self.surf.get_rect(topleft=self.position)
        self.surf.blit(self.image, (0, 0))

    def update(self):
        self.set_image()