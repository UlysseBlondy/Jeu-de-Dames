import pygame
import sys
from checkers_game.board_piece import*


def main():
    win = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Checkers Game")
    clock = pygame.time.Clock()

    game = CheckerGame()
    game.display_grid()

    running = True
    while running:
        win.fill(white)
        game.draw_grid(win)
        game.draw_pawn(win)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if game.selected_piece is None:
                    pos = game.get_piece_at_position(pygame.mouse.get_pos())
                    if pos is not None and game.grid[pos[0]][pos[1]] == game.begin:
                        game.selected_piece = pos
                        game.moves = [(pos[0] - 1, pos[1] + 1), (pos[0] - 1, pos[1] - 1)]

                        
                        
                else:
                    pos = game.get_piece_at_position(pygame.mouse.get_pos())
                    if pos in game.moves or game.moves_promoted:
                        game.move_pawn(game.selected_piece, pos)
                        

                    game.selected_piece = None

        clock.tick(60)

    pygame.quit()
    sys.exit()

main()