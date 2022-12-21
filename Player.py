import pygame
from Object import Object

class Player(Object):
    def __init__(self, position: tuple, size: tuple, image_path: str, group: pygame.sprite.Group, collision_groups: list, kill_groups: list, speed: int):
        super().__init__(position, size, image_path, group)

        # ---------- ATTRIBUTE SETUP ---------- #
        self.position, self.x, self.y = position, position[0], position[1]
        self.speed = self.speed
        self.collision_groups = collision_groups
        self.kill_groups = kill_groups

        self.direction = "down"
        self.keyups = []

    def move(self):
        if pygame.K_UP in self.keyups:
            self.y -= self.speed
            self.direction = "up"
        if pygame.K_DOWN in self.keyups:
            self.y += self.speed
            self.direction = "down"
        if pygame.K_LEFT in self.keyups:
            self.x -= self.speed
            self.direction = "left"
        if pygame.K_RIGHT in self.keyups:
            self.x += self.speed
            self.direction = "right"

        self.check_collisions()     # Check collisions, reverts movement if collides
        self.pos = (self.x, self.y) # Set new position

    def check_collisions(self):
        self.position = (self.x, self.y)

        # Revert movement if colliding with object
        if (pygame.sprite.spritecollideany(self, group) for group in self.collision_groups):
            if self.direction == "up":
                self.y += self.speed
            if self.direction == "down":
                self.y -= self.speed
            if self.direction == "left":
                self.y += self.speed
            if self.direction == "right":
                self.y -= self.speed

        if (pygame.sprite.spritecollideany(self, group) for group in self.kill_groups):
            self.x, self.y = 0, 0 # TODO set respawn point

        self.position = (self.x, self.y)

    def update(self):
        self.move()
        self.set_image()