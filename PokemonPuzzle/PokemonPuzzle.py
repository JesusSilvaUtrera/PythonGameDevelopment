import pygame as pg
import os
import sys
import random
from cfg import *


class PokemonPuzzle:
    def __init__(self):
        # * Initialize pygame and clock
        pg.init()
        self.clock = pg.time.Clock()
        # * Image and music
        self.game_img = pg.image.load(self.getImages())
        self.game_img = pg.transform.scale(self.game_img, SCREENSIZE)
        self.game_img_rect = self.game_img.get_rect()
        pg.mixer.init()
        pg.mixer.music.load(SONG)
        pg.mixer.music.play(-1)
        # * Initialize the display
        self.GameScreen = pg.display.set_mode(SCREENSIZE)
        pg.display.set_caption("Pokemon Puzzle Game")
        self.size = self.showInitialInterface(
            self.game_img_rect.width, self.game_img_rect.height
        )
        assert isinstance(self.size, int)
        # * Get rows, cols and cells
        num_rows, num_cols = self.size, self.size
        num_cells = num_rows * num_cols
        self.cell_width = self.game_img_rect.width / num_cols
        self.cell_height = self.game_img_rect.height / num_rows

        while True:
            blank_cell_index = self.createBoard(num_rows, num_cols, num_cells)
            if not self.isGameOver():
                break
        self.is_running = True
        self.run(blank_cell_index, num_rows, num_cols, num_cells)

    def createBoard(self, num_rows, num_cols, num_cells):
        self.board = []

        for cell in range(num_cells):
            self.board.append(cell)

        blank_cell_index = num_cells - 1
        self.board[blank_cell_index] = -1

        for i in range(RANDNUM):
            direction = random.randint(0, 3)
            if direction == 0:
                self.moveL(blank_cell_index, num_cols)
            elif direction == 1:
                self.moveR(blank_cell_index, num_cols)
            elif direction == 2:
                self.moveU(blank_cell_index, num_rows, num_cols)
            elif direction == 3:
                self.moveD(blank_cell_index, num_cols)

        return blank_cell_index

    def showInitialInterface(self, width, height):
        self.GameScreen.fill(BACKGROUNDCOLOR)
        # * Create the different fonts for the title and the content, and also create the rectangles for the texts
        title_font = pg.font.Font(FONTPATH, int(width / 6))
        title = title_font.render("Pokemon Puzzle", True, RED)
        content_font = pg.font.Font(FONTPATH, int(width / 20))
        content1 = content_font.render(
            "Press H, M or L to choose the difficulty of the puzzle", True, BLUE
        )
        content2 = content_font.render("H - 5x5, M - 4x4, L - 3x3", True, BLUE)
        title_rect = title.get_rect()
        title_rect.midtop = (int(width / 2), int(height / 10))
        content_rect1 = content1.get_rect()
        content_rect1.midtop = (int(width / 2), int(height / 2.2))
        content_rect2 = content2.get_rect()
        content_rect2.midtop = (int(width / 2), int(height / 1.8))
        # * Show all on screen
        self.GameScreen.blit(title, title_rect)
        self.GameScreen.blit(content1, content_rect1)
        self.GameScreen.blit(content2, content_rect2)
        # * Be waiting for any event to happen
        while True:
            for event in pg.event.get():
                if (event.type == pg.QUIT) or (
                    event.type == pg.KEYDOWN and event.type == pg.K_ESCAPE
                ):
                    pg.quit()
                    sys.exit()
                elif event.type == pg.KEYDOWN:
                    if event.key == ord("l"):
                        return 3
                    elif event.key == ord("m"):
                        return 4
                    elif event.key == ord("h"):
                        return 5
            pg.display.update()

    def getImages(self):
        image_names = os.listdir(PICTURE_ROOT_DIR)
        assert len(image_names) > 0
        return os.path.join(PICTURE_ROOT_DIR, random.choice(image_names))

    def showEndInterface(self, width, height):
        self.GameScreen.fill(BACKGROUNDCOLOR)
        # * Create the fonts and rectangles, and show them on screen
        font = pg.font.Font(FONTPATH, width / 15)
        title = font.render("Good job! You won!", True, (233, 150, 122))
        rect = title.get_rect()
        rect.midtop = (width / 2, height / 2)  # ! check this
        self.GameScreen.blit(title, rect)
        pg.display.update()
        # * Be waiting for any event to happen
        while True:
            for event in pg.event.get():
                if (event.type == pg.QUIT) or (
                    event.type == pg.KEYDOWN and event.type == pg.K_ESCAPE
                ):
                    pg.quit()
                    sys.exit()
            pg.display.update()

    def isGameOver(self):
        # * This function checks if the game has finished by checking if all cells has their expected value
        num_cells = self.size * self.size
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

    def moveD(self, blank_cell_index, num_cols):
        if blank_cell_index < num_cols:
            return blank_cell_index
        self.board[blank_cell_index - num_cols], self.board[blank_cell_index] = (
            self.board[blank_cell_index],
            self.board[blank_cell_index - num_cols],
        )
        return blank_cell_index - num_cols

    def moveU(self, blank_cell_index, num_rows, num_cols):
        if blank_cell_index >= (num_rows - 1) * num_cols:
            return blank_cell_index
        self.board[blank_cell_index + num_cols], self.board[blank_cell_index] = (
            self.board[blank_cell_index],
            self.board[blank_cell_index + num_cols],
        )
        return blank_cell_index + num_cols

    def run(self, blank_cell_index, num_rows, num_cols, num_cells):
        # * You will be running the game until the quit event is received
        while self.is_running:
            # * Catch every event
            for event in pg.event.get():
                if event.type == pg.QUIT or (
                    event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE
                ):
                    pg.quit()
                    sys.exit()
                elif event.type == pg.KEYDOWN:
                    if event.key == ord("a") or event.key == pg.K_LEFT:
                        blank_cell_index = self.moveL(blank_cell_index, num_cols)
                    elif event.key == ord("d") or event.key == pg.K_RIGHT:
                        blank_cell_index = self.moveR(blank_cell_index, num_cols)
                    elif event.key == ord("w") or event.key == pg.K_UP:
                        blank_cell_index = self.moveU(
                            blank_cell_index, num_rows, num_cols
                        )
                    elif event.key == ord("s") or event.key == pg.K_DOWN:
                        blank_cell_index = self.moveD(blank_cell_index, num_cols)

                elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                    x, y = pg.mouse.get_pos()
                    x_pos = x / self.cell_width
                    y_pos = y / self.cell_height
                    idx = x_pos + y_pos * num_cols
                    if idx == blank_cell_index - 1:
                        blank_cell_index = self.moveR(blank_cell_index, num_cols)
                    if idx == blank_cell_index + 1:
                        blank_cell_index = self.moveL(blank_cell_index, num_cols)
                    if idx == blank_cell_index + num_cols:
                        blank_cell_index = self.moveU(
                            blank_cell_index, num_rows, num_cols
                        )
                    if idx == blank_cell_index - num_cols:
                        blank_cell_index = self.moveD(blank_cell_index, num_cols)

            if self.isGameOver():
                self.board[blank_cell_index] = num_cells - 1
                self.is_running = False

            self.GameScreen.fill(BACKGROUNDCOLOR)
            for i in range(num_cells):
                if self.board[i] == -1:
                    continue
                x_pos = i // num_cols
                y_pos = i % num_cols

                rect = pg.Rect(
                    y_pos * self.cell_width,
                    x_pos * self.cell_height,
                    self.cell_width,
                    self.cell_height,
                )
                img_area = pg.Rect(
                    (self.board[i] % num_cols) * self.cell_width,
                    (self.board[i] // num_cols) * self.cell_height,
                    self.cell_width,
                    self.cell_height,
                )
                self.GameScreen.blit(self.game_img, rect, img_area)

            for i in range(num_cols + 1):
                pg.draw.line(
                    self.GameScreen,
                    BLACK,
                    (i * self.cell_width, 0),
                    (i * self.cell_width, self.game_img_rect.height),
                )
            for i in range(num_rows + 1):
                pg.draw.line(
                    self.GameScreen,
                    BLACK,
                    (0, i * self.cell_height),
                    (self.game_img_rect.width, i * self.cell_height),
                )

            # * Update the screen
            pg.display.update()
            # * Use the clock created to set the fps
            self.clock.tick(FPS)

        self.showEndInterface(self.game_img_rect.width, self.game_img_rect.height)


if __name__ == "__main__":
    game = PokemonPuzzle()
