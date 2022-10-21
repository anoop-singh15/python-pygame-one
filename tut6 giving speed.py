import pygame

pygame.init()

"""colors"""
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

"""Game Window"""  # width,height
screen_width = 900
screen_height = 500
gameWindow = pygame.display.set_mode((screen_width, screen_height))



"""Game title"""
pygame.display.set_caption("Snake")
pygame.display.update()

"""Game Specific variables"""
exit_game = False
game_over = False

"""game specific variable for snake"""
snake_x = 45
snake_y = 55
snake_size = 19
#velocity for snake
velocity_x=2
velocity_y=2



"""game specific variable for time"""
fps = 30
clock = pygame.time.Clock()

"""Game loop"""
while not exit_game:
    for event in pygame.event.get():
        # print(event)
        """quit event handling"""
        if event.type == pygame.QUIT:
            exit_game = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake_x = snake_x + 10
            if event.key ==pygame.K_DOWN:
                snake_y+=10
            if event.key == pygame.K_LEFT:
                snake_x -= 10
            if event.key == pygame.K_UP:
                snake_y -= 10

    """velocity for snake"""
    snake_x+=velocity_x
    snake_y+=velocity_y
    """Game window colors fill"""
    gameWindow.fill(white)
    # to make any change in program appear in game use  update
    """snake making in game"""
    pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size])
    pygame.display.update()
    clock.tick(fps)

pygame.quit()
quit()
