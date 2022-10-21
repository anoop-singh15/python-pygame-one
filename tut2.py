import pygame
pygame.init()

"""Game Window"""  # width,height
gameWindow = pygame.display.set_mode((1000, 500))

"""Game title"""
pygame.display.set_caption("My First Game")

"""Game Specific variables"""
exit_game=False
game_over=False
