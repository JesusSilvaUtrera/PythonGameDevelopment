import pygame as pg
import os

# * Global variables to configure our game
WIDTH, HEIGHT = 800, 600
FPS = 60
PICTURE = pg.image.load(os.path.join("resources", "TrollFace.jpg"))
SONG = os.path.join(os.getcwd(), "resources/fart.mp3")


# * This will show the display of our game
GameScreen = pg.display.set_mode((WIDTH, HEIGHT))
# * We should give our game window a name
pg.display.set_caption("First Game")


def draw_fn():
    # * You can fill your screen with the colour you want
    GameScreen.fill((255, 0, 0))  # RGB
    # * Display the image you want
    GameScreen.blit(PICTURE, (0, 0))  # (image, coord)
    # * For the changes to take effect, you need to update the screen
    pg.display.update()


def main():
    # * Initialize the run and the mixer for the songs
    pg.mixer.init()
    pg.mixer.music.load(SONG)
    pg.mixer.music.play(
        -1
    )  # -1 is to play forever, if you dont want that you can specify the loops
    run = True

    # * Create a clock for the fps
    clock = pg.time.Clock()

    # * You will be running the game until the quit event is received
    while run:
        # * Use the clock created to set the fps
        clock.tick(FPS)

        # * Catch every event
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()

        # * Update the screen
        draw_fn()


if __name__ == "__main__":
    main()
