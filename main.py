from modules.game import title_screen, play_level, game_credits
from modules.info import GameState, SCREEN_WIDTH, SCREEN_HEIGHT
from modules.player import Player
import pygame

# main function
def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_state = GameState.TITLE

    while True:
        if game_state == GameState.TITLE:
            game_state = title_screen(screen)

        if game_state == GameState.NEWGAME:
            player = Player()
            game_state = play_level(screen, player)

        if game_state == GameState.NEXT_LEVEL:
            player.level += 1
            game_state = play_level(screen, player)

        if game_state == GameState.CREDITS:
            game_state = game_credits(screen)

        if game_state == GameState.RESET_POS:
            player.x = 0
            player.y = 35

        if game_state == GameState.QUIT:
            pygame.quit()
            return

if __name__ == "__main__":
    main()