from Game import Game

############### WINDOW SETUP ###############
DIMENSIONS = (1280, 720)
TITLE = "Pong"
ICON = "assets/icon.png"

Pong = Game(DIMENSIONS, TITLE, ICON)

del DIMENSIONS, TITLE, ICON
############################################

Pong.run()