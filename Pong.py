from Game import Game

############### WINDOW SETUP ###############
DIMENSIONS = (1920, 1080)
TITLE = "Pong"
ICON = "assets/icon.png"

Pong = Game(DIMENSIONS, TITLE, ICON)

del DIMENSIONS, TITLE, ICON
############################################

Pong.run()