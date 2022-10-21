import pygame
pygame.init()

"""Game Window"""  # width,height
gameWindow = pygame.display.set_mode((1000, 500))

"""Game title"""
pygame.display.set_caption("My First Game")

"""Game Specific variables"""
exit_game = False
game_over = False

"""Game loop"""  # main control of gaeme are handled here
while not exit_game:
    """what we do inside game is event"""
    for event in pygame.event.get():
        """event handle for quit"""
        if event.type == pygame.QUIT:
            exit_game = True
        if event.type==pygame.KEYDOWN:
            """keydown to detect when key is pressed"""
            if event.key==pygame.K_RIGHT:
                print("You have pressed right arrow key")

"""after game loop exit"""
pygame.quit()
quit()
