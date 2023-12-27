import pygame as pg
import os
import sys
import random
from .cfg import *


class PokemonPuzzle:
    def __init__(self):
        # * Initialize the display
        self.GameScreen = pg.display.set_mode(SCREENSIZE)
        # * Give name to our game window
        pg.display.set_caption("Pokemon Puzzle Game")
        # * Fill the colour of the initial display and start playing the music
        self.GameScreen.fill((255, 0, 0))
        pg.mixer.init()
        pg.mixer.music.load(SONG)
        pg.mixer.music.play(-1)
        # TODO Add the font to the initial display
        # TODO Add the board as attribute

    def isGameOver(self, size):
        # * This function checks if the game has finished by checking if all cells has their expected value
        assert isinstance(size, int)
        num_cells = size * size
        for cell in range(num_cells - 1):
            if self.board[cell] != cell:
                return False
        return True

    def moveR(self, blank_cell_index, num_cols):
        if blank_cell_index % num_cols == 0:
            return blank_cell_index
        self.board[blank_cell_index - 1], self.board[blank_cell_index] = (
            self.board[blank_cell_index],
            self.board[blank_cell_index - 1],
        )
        return blank_cell_index - 1

    def moveL(self, blank_cell_index, num_cols):
        if (blank_cell_index + 1) % num_cols == 0:
            return blank_cell_index
        self.board[blank_cell_index + 1], self.board[blank_cell_index] = (
            self.board[blank_cell_index],
            self.board[blank_cell_index + 1],
        )
        return blank_cell_index - 1

    def draw_fn():
        # RGB
        # * Display the image you want
        GameScreen.blit(PICTURE, (0, 0))  # (image, coord)

    def run(self):
        # * This function is the main loop for the game
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
            # * For the changes to take effect, you need to update the screen
            pg.display.update()


if __name__ == "__main__":
    game = PokemonPuzzle()
    game.run()
