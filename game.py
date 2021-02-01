import sys
import numpy as np
import pygame

pygame.init()

screen = pygame.display.set_mode((611, 611))
screen.fill((135, 200, 55))
name = pygame.display.set_caption('Логическая игра')

font_number = pygame.font.Font(None, 36)
mas = np.random.randint(1, 4, (10, 10))

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        for row in range(10):
            for col in range(10):
                coordinat_x = col * 60 + (col + 1) * 1
                coordinat_y = row * 60 + (row + 1) * 1

                number = font_number.render(f'{mas[row][col]}', True, (255, 255, 255))
                place_number = pygame.draw.rect(screen,
                                                (0, 0, 0),
                                                (coordinat_x, coordinat_y, 60, 60)
                                                )
                screen.blit(number, place_number)

        if e.type == pygame.MOUSEBUTTONDOWN:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            row = x_mouse // (60 + 1)
            column = y_mouse // (60 + 1)

            if row == 9 and column == 0:
                if mas[column][row - 1] == 0 and mas[column + 1][row] == 0 and mas[column + 1][row - 1] == 0:
                    mas[column][row] -= 0
                elif mas[column][row] > 0:
                    mas[column][row] -= 1
                    if mas[column][row - 1] > 0:
                        mas[column][row - 1] -= 1
                    if mas[column + 1][row] > 0:
                        mas[column + 1][row] -= 1
                    if mas[column + 1][row - 1] > 0:
                        mas[column + 1][row - 1] -= 1

            elif row == 9 and column == 9:
                if mas[column - 1][row] == 0 and mas[column - 1][row - 1] == 0 and mas[column][row - 1] == 0:
                    mas[column][row] -= 0
                elif mas[column][row] > 0:
                    mas[column][row] -= 1
                    if mas[column - 1][row] > 0:
                        mas[column - 1][row] -= 1
                    if mas[column - 1][row - 1] > 0:
                        mas[column - 1][row - 1] -= 1
                    if mas[column][row - 1] > 0:
                        mas[column][row - 1] -= 1

            elif row == 0 and column == 0:
                if mas[column][row + 1] == 0 and mas[column + 1][row + 1] == 0 and mas[column + 1][row] == 0:
                    mas[column][row] -= 0
                elif mas[column][row] > 0:
                    mas[column][row] -= 1
                    if mas[column][row + 1] > 0:
                        mas[column][row + 1] -= 1
                    if mas[column + 1][row + 1] > 0:
                        mas[column + 1][row + 1] -= 1
                    if mas[column + 1][row] > 0:
                        mas[column + 1][row] -= 1

            elif row == 0 and column == 9:
                if mas[column - 1][row + 1] == 0 and mas[column - 1][row] == 0 and mas[column][row + 1] == 0:
                    mas[column][row] -= 0
                elif mas[column][row] > 0:
                    mas[column][row] -= 1
                    if mas[column - 1][row + 1] > 0:
                        mas[column - 1][row + 1] -= 1
                    if mas[column - 1][row] > 0:
                        mas[column - 1][row] -= 1
                    if mas[column][row + 1] > 0:
                        mas[column][row + 1] -= 1

            elif row == 0:
                if mas[column - 1][row + 1] == 0 and mas[column - 1][row] == 0 and mas[column][row + 1] == 0 and \
                        mas[column + 1][row + 1] == 0 and mas[column + 1][row] == 0:
                    mas[column][row] -= 0
                elif mas[column][row] > 0:
                    mas[column][row] -= 1
                    if mas[column - 1][row + 1] > 0:
                        mas[column - 1][row + 1] -= 1
                    if mas[column - 1][row] > 0:
                        mas[column - 1][row] -= 1
                    if mas[column][row + 1] > 0:
                        mas[column][row + 1] -= 1
                    if mas[column + 1][row + 1] > 0:
                        mas[column + 1][row + 1] -= 1
                    if mas[column + 1][row] > 0:
                        mas[column + 1][row] -= 1

            elif row == 9:
                if mas[column - 1][row] == 0 and mas[column - 1][row - 1] == 0 and mas[column][row - 1] == 0 and \
                        mas[column + 1][row] == 0 and mas[column + 1][row - 1] == 0:
                    mas[column][row] -= 0
                elif mas[column][row] > 0:
                    mas[column][row] -= 1
                    if mas[column - 1][row] > 0:
                        mas[column - 1][row] -= 1
                    if mas[column - 1][row - 1] > 0:
                        mas[column - 1][row - 1] -= 1
                    if mas[column][row - 1] > 0:
                        mas[column][row - 1] -= 1
                    if mas[column + 1][row] > 0:
                        mas[column + 1][row] -= 1
                    if mas[column + 1][row - 1] > 0:
                        mas[column + 1][row - 1] -= 1

            elif column == 0:
                if mas[column][row + 1] == 0 and mas[column][row - 1] == 0 and mas[column + 1][row + 1] == 0 and \
                        mas[column + 1][row - 1] == 0:
                    mas[column][row] -= 0
                elif mas[column][row] > 0:
                    mas[column][row] -= 1
                    if mas[column][row + 1] > 0:
                        mas[column][row + 1] -= 1
                    if mas[column][row - 1] > 0:
                        mas[column][row - 1] -= 1
                    if mas[column + 1][row + 1] > 0:
                        mas[column + 1][row + 1] -= 1
                    if mas[column + 1][row] > 0:
                        mas[column + 1][row] -= 1
                    if mas[column + 1][row - 1] > 0:
                        mas[column + 1][row - 1] -= 1

            elif column == 9:
                if mas[column - 1][row + 1] == 0 and mas[column - 1][row] == 0 and mas[column - 1][row - 1] == 0 and \
                        mas[column][row + 1] == 0 and mas[column][row - 1] == 0:
                    mas[column][row] -= 0
                elif mas[column][row] > 0:
                    mas[column][row] -= 1
                    if mas[column - 1][row + 1] > 0:
                        mas[column - 1][row + 1] -= 1
                    if mas[column - 1][row] > 0:
                        mas[column - 1][row] -= 1
                    if mas[column - 1][row - 1] > 0:
                        mas[column - 1][row - 1] -= 1
                    if mas[column][row + 1] > 0:
                        mas[column][row + 1] -= 1
                    if mas[column][row - 1] > 0:
                        mas[column][row - 1] -= 1
            else:
                if mas[column - 1][row + 1] == 0 and mas[column - 1][row] == 0 and mas[column - 1][row - 1] == 0 and \
                        mas[column][row + 1] == 0 and mas[column][row - 1] == 0 and mas[column + 1][row + 1] == 0 and \
                        mas[column + 1][row] == 0 and mas[column + 1][row - 1] == 0:

                    mas[column][row] -= 0
                elif mas[column][row] > 0:
                    mas[column][row] -= 1
                    if mas[column - 1][row + 1] > 0:
                        mas[column - 1][row + 1] -= 1
                    if mas[column - 1][row] > 0:
                        mas[column - 1][row] -= 1
                    if mas[column - 1][row - 1] > 0:
                        mas[column - 1][row - 1] -= 1
                    if mas[column][row + 1] > 0:
                        mas[column][row + 1] -= 1
                    if mas[column][row - 1] > 0:
                        mas[column][row - 1] -= 1
                    if mas[column + 1][row + 1] > 0:
                        mas[column + 1][row + 1] -= 1
                    if mas[column + 1][row] > 0:
                        mas[column + 1][row] -= 1
                    if mas[column + 1][row - 1] > 0:
                        mas[column + 1][row - 1] -= 1

    pygame.display.update()
