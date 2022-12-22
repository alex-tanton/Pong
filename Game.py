from Bumper import Bumper
from Ball import Ball

import pygame, sys

class Game:
    def __init__(self, dimensions, title, icon_path):
        pygame.init()

        self.dimensions, self.width, self.height = dimensions, dimensions[0], dimensions[1]
        pygame.display.set_mode(self.dimensions)

        pygame.display.set_caption(title)
        pygame.display.set_icon(pygame.image.load(icon_path).convert())

        self.display = pygame.display.get_surface()

        # Sprite group initialization
        self.bumper_group = pygame.sprite.Group()
        self.ball_group = pygame.sprite.Group()
        self.misc_group = pygame.sprite.Group()
        self.all_groups = [self.bumper_group, self.ball_group, self.misc_group]

        self.asset_setup()

    def asset_setup(self):
        self.p1 = Bumper(self, (0, (self.height-100)/2), (20, 150), 20, "./Assets/bumper.png", self.bumper_group)
        self.p2 = Bumper(self, (self.width-20, (self.height-100)/2),
                         (20, 150), 20, "./Assets/bumper.png", self.bumper_group)
        self.ball = Ball(self, ((self.width-10)/2, (self.height-10)/2), (10, 10),
                         1.5, 1.5, "./Assets/ball.png", self.ball_group, self.bumper_group)

    def run(self):
        clock = pygame.time.Clock()
        break_loop = False

        while True:
            # Exit loop if game closed
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    break_loop = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        self.p1.move("up")
                    if event.key == pygame.K_s:
                        self.p1.move("down")

                    if event.key == pygame.K_i:
                        self.p2.move("up")
                    if event.key == pygame.K_k:
                        self.p2.move("down")
            if break_loop: break

            # Bumper movement
            keys_pressed = pygame.key.get_pressed()
            if keys_pressed[pygame.K_w]:
                self.p1.move("up")
            if keys_pressed[pygame.K_s]:
                self.p1.move("down")
            if keys_pressed[pygame.K_i]:
                self.p2.move("up")
            if keys_pressed[pygame.K_k]:
                self.p2.move("down")

            # Display updating
            self.display.fill((0, 0, 0))
            for group in self.all_groups:
                for sprite in group:
                    sprite.update()
                group.draw(self.display)
            pygame.display.update()

            clock.tick(144)

        pygame.quit()
        sys.exit()
