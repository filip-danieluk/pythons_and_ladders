import sys

import pygame


# brand.cbre.com
LIGHT_GRAY = (202, 209, 211)
ACCENT_GREEN = (128, 187, 173) 

BLOCK_SIZE = 60
WINDOW_HEIGHT = BLOCK_SIZE * 10
WINDOW_WIDTH = BLOCK_SIZE * 10


def draw_grid():
    for x in range(0, WINDOW_WIDTH, BLOCK_SIZE):
        for y in range(0, WINDOW_HEIGHT, BLOCK_SIZE):
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(SCREEN, ACCENT_GREEN, rect, 1)


def main():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    # CLOCK = pygame.time.Clock()
    SCREEN.fill(LIGHT_GRAY)

    while True:
        draw_grid()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


if __name__ == '__main__':
    main()