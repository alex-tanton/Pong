from Game import Game

############### WINDOW SETUP ###############
DIMENSIONS = (1920, 1080)
TITLE = "Game Name"
COLOR = (0, 0, 0)
ICON = "assets\\icon.png"

game = Game(DIMENSIONS, TITLE, COLOR, ICON) # TODO change variable to name of game

del DIMENSIONS, TITLE, COLOR, ICON
############################################

game.run()