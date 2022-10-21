import pygame
pygame.init()

"""Game Window"""  # width,height
gameWindow = pygame.display.set_mode((1000, 500))

"""Game title"""
pygame.display.set_caption("My First Game")

"""Game Specific variables"""
exit_game = False
game_over = False


"""Game loop"""  # main control of game are handled here
while not exit_game:
    pass


"""after game loop exit"""
pygame.quit()
quit()