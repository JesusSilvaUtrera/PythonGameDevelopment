import os

# ! This file is for configuring our game, so we don't have to define
# ! all configuration in our main script

SCREENSIZE = (640, 640)

PICTURE_ROOT_DIR = os.path.join(os.getcwd(), "resources/pictures")

FONTPATH = os.path.join(os.getcwd(), "resources/font/FZSTK.TTF")

SONG = os.path.join(os.getcwd(), "resources/audio/Pokemon.mp3")

BACKGROUNDCOLOR = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

FPS = 40

RANDNUM = 100
