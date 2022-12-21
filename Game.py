from Object import Object
from Player import Player
import pygame, sys

class Game:
    def __init__(self, dimensions: tuple, title: str, color: tuple, icon_path: str):
        pygame.init()

        self.screen_color = color

        # ---------- WINDOW SETUP ---------- #
        pygame.display.set_mode(dimensions)
        pygame.display.set_caption(title)
        pygame.display.set_icon(pygame.image.load(icon_path).convert())

        self.DISPLAY = pygame.display.get_surface()

        # ---------- GROUP SETUPS ---------- #
        self.object_group = pygame.sprite.Group()
        # TODO create all other groups, including collision groups and kill groups
        self.player_group = pygame.sprite.Group()
        self.collision_groups = [] # TODO populate with collision groups
        self.kill_groups = [] # TODO populate will kill groups
        self.all_groups = [self.object_group]

        # ---------- ASSET SETUP ---------- #
        self.asset_setup()

    def asset_setup(self):
        # ---------- ALL OBJECT CREATION ---------- #
        # Create objects

        # ----- PLAYER CREATION ----- #
        self.player = Player((0, 0), (0, 0), "assets\\player\\down.png", self.player_group, self.collision_groups, self.kill_groups, .5) # TODO set player start point and size

    def run(self):
        carry_on = True
        CLOCK = pygame.time.Clock()

        # --------------- MAIN PROGRAM LOOP --------------- #
        while carry_on:

            self.player.keyups = []

            for event in pygame.event.get():
                if event.type == pygame.QUIT: # If user clicked close,
                    break                     # Exit game loop
                if event.type == pygame.KEYUP:
                    self.player.keyups.append(event.key)

            # ---------- MAIN GAME LOGIC ---------- #
            for group in self.all_groups:
                for sprite in group:
                    sprite.update()
                group.draw(self.DISPLAY)

            # ---------- DISPLAY UPDATE ---------- #
            pygame.display.update()

            # ---------- TIMING/FPS ---------- #
            CLOCK.tick(60)

        # ----- KILL ALL PROCESSES ----- #
        pygame.quit()
        sys.exit()