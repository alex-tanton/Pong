from Bumper import Bumper
from Ball import Ball

import pygame, sys

class Game:
    def __init__(self, dimensions, title, icon_path):
        pygame.init()

        # Set window dimension variables
        self.width, self.height = dimensions[0], dimensions[1]

        # Set window properties
        pygame.display.set_mode(dimensions, pygame.RESIZABLE)
        pygame.display.set_caption(title)
        pygame.display.set_icon(pygame.image.load(icon_path).convert())

        # Get display surface
        self.display = pygame.display.get_surface()

        # Sprite group initialization
        self.bumper_group = pygame.sprite.Group()
        self.ball_group = pygame.sprite.Group()
        self.all_groups = [self.bumper_group, self.ball_group]

        # Score keeping array
        self.score = [0, 0]
        self.asset_setup()

    def asset_setup(self):
        # Calculate bumper dimensions and speed from window size
        self.bumper_width, self.bumper_height = self.width/100, self.height/7.5
        bumper_speed = self.height/150

        # Initialize bumper objects
        self.p1 = Bumper(self, (0, (self.height-self.bumper_height)/2), (self.bumper_width,self.bumper_height), bumper_speed, "./Assets/bumper.png", self.bumper_group)
        self.p2 = Bumper(self, (self.width-self.bumper_width, (self.height-self.bumper_height)/2), (self.bumper_width,self.bumper_height), bumper_speed, "./Assets/bumper.png", self.bumper_group)

        # Calculate ball size and speed
        ball_radius = self.width/175
        self.initial_ball_speed_x, self.initial_ball_speed_y = -self.width/375, 0

        # Initialize ball
        self.ball = Ball(self, ((self.width-ball_radius)/2, (self.height-ball_radius)/2), ball_radius, self.initial_ball_speed_x, self.initial_ball_speed_y, "./Assets/ball.png", self.ball_group)

    def run(self):
        # Set game control variables
        clock = pygame.time.Clock()
        break_loop = False

        while True:
            # Window event handlers
            for event in pygame.event.get():
                # Exit loop if game closed
                if event.type == pygame.QUIT:
                    break_loop = True
                # Handle window resizing
                if event.type == pygame.VIDEORESIZE:
                    # Calculate change and update window dimension variables
                    ratio = [event.w / self.width, event.h / self.height]
                    self.width, self.height = event.w, event.h

                    # Update bumper size
                    self.bumper_width *= ratio[0]
                    self.bumper_height *= ratio[1]
                    self.p1.size = (self.bumper_width, self.bumper_height)
                    self.p1.width, self.p1.height = self.bumper_width, self.bumper_height
                    self.p2.size = (self.bumper_width, self.bumper_height)
                    self.p2.width, self.p2.height = self.bumper_width, self.bumper_height

                    # Update bumper speed
                    self.p1.dy *= ratio[1]
                    self.p2.dy *= ratio[1]

                    # Update bumper X positioning
                    self.p1.x *= ratio[0]
                    self.p2.x *= ratio[0]

                    # Update bumper Y positioning
                    self.p1.y *= ratio[1]
                    self.p2.y *= ratio[1]

                    # Apply bumper updates
                    self.p1.position = (self.p1.x, self.p1.y)
                    self.p2.position = (self.p2.x, self.p2.y)
                    self.p1.set_image()
                    self.p2.set_image()

                    # Update ball size
                    self.ball.diameter *= (ratio[0] + ratio[1]) / 2
                    self.ball.size = (self.ball.diameter, self.ball.diameter)

                    # Update ball speed
                    self.ball.dx *= ratio[0]
                    self.ball.dy *= ratio[1]

                    # Update ball X positioning
                    self.ball.x *= ratio[0]

                    # Update ball Y positioning
                    self.ball.y *= ratio[1]

                    # Apply ball updates
                    self.ball.position = (self.ball.x, self.ball.y)
                    self.ball.set_image()

            if break_loop: break

            # Translate player input to bumper movement
            keys_pressed = pygame.key.get_pressed()
            if keys_pressed[pygame.K_w]:
                self.p1.move("up")
            if keys_pressed[pygame.K_s]:
                self.p1.move("down")
            if keys_pressed[pygame.K_i]:
                self.p2.move("up")
            if keys_pressed[pygame.K_k]:
                self.p2.move("down")

            # Clear display
            self.display.fill((0, 0, 0))

            # Initialize/update font and font size
            font = pygame.font.SysFont(None, int(0.7 * self.height))

            # Render score texts
            p1_score = font.render(str(self.score[0]), 0, (50, 50, 50))
            p2_score = font.render(str(self.score[1]), 0, (50, 50, 50))

            # Get rects for score objects
            p1_score_rect, p2_score_rect = p1_score.get_rect(), p2_score.get_rect()

            # Set score positions
            p1_score_rect.center = (self.width/4, self.height/2)
            p2_score_rect.center = (self.width/4*3, self.height/2)

            # Draw scores
            self.display.blit(p1_score, p1_score_rect)
            self.display.blit(p2_score, p2_score_rect)

            # Update sprites
            for group in self.all_groups:
                for sprite in group:
                    sprite.update()
                group.draw(self.display)

            # Update display
            pygame.display.update()
            clock.tick(144)

        # Quit game
        pygame.quit()
        sys.exit()
