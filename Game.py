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

        self.score = [0, 0]
        self.asset_setup()

    def asset_setup(self):
        self.bumper_width, self.bumper_height = 20, 150
        bumper_speed = 10

        self.p1 = Bumper(self, (0, (self.height-self.bumper_height)/2), (self.bumper_width,self.bumper_height), bumper_speed, "./Assets/bumper.png", self.bumper_group)
        self.p2 = Bumper(self, (self.width-self.bumper_width, (self.height-self.bumper_height)/2), (self.bumper_width,self.bumper_height), bumper_speed, "./Assets/bumper.png", self.bumper_group)

        ball_radius = 10
        self.initial_ball_speed_x, self.initial_ball_speed_y = -5, 0
        self.ball = Ball(self, ((self.width-ball_radius)/2, (self.height-ball_radius)/2), ball_radius,
                         self.initial_ball_speed_x, self.initial_ball_speed_y, "./Assets/ball.png", self.ball_group)

    def run(self):
        clock = pygame.time.Clock()
        break_loop = False

        while True:
            for event in pygame.event.get():
                # Exit loop if game closed
                if event.type == pygame.QUIT:
                    break_loop = True
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
