import pygame
import random
pygame.init()

"""colors"""
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

"""Game Window"""  # width,height
screen_width = 800
screen_height = 600
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
# velocity for snake
velocity_x = 0
velocity_y = 0
init_velocity=5
#score
score = 0

"""game specific variable for food"""
food_x=random.randint(20,screen_width-100)
food_y=random.randint(20,screen_height-100)

"""game specific variable for time"""
fps = 60
clock = pygame.time.Clock()

"""font of score"""
font =pygame.font.SysFont(None,55)

"""to print font on window"""
def text_screen(text,color,x,y):
     screen_text=font.render(text,True,color)
     gameWindow.blit(screen_text,[x,y])

"""snake length increment"""
def plot_snake(gameWindow,color,snk_lst,snake_size):
    for x, y in snk_lst:
          pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

"""Game specific variable for snake length"""
snk_lst=[]
snk_length =1

"""Game loop"""
while not exit_game:
    for event in pygame.event.get():
        # print(event)
        """quit event handling"""
        if event.type == pygame.QUIT:
            exit_game = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                velocity_x=init_velocity
                velocity_y=0
            if event.key == pygame.K_DOWN:
                velocity_y = init_velocity
                velocity_x = 0
            if event.key == pygame.K_LEFT:
                velocity_x = -init_velocity
                velocity_y = 0
            if event.key == pygame.K_UP:
                velocity_y = - init_velocity
                velocity_x = 0


    """velocity for snake"""
    snake_x += velocity_x
    snake_y += velocity_y

    """replotting and score"""

    if abs(snake_x-food_x)<19 and abs(snake_y-food_y)<19:
        score+=1
        # print("Score:",score*10)

        food_x = random.randint(20, screen_width - 100)
        food_y = random.randint(20, screen_height - 100)
        """for length"""
        snk_length +=4

    """Game window colors fill"""
    gameWindow.fill(white)
    #to print score on window
    text_screen("Score:" + str(score * 10), red, 5, 5)


    """snake making in game"""
    # pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size])

    """length"""
    head=[]
    head.append(snake_x)
    head.append(snake_y)
    snk_lst.append(head)
    #function for lenght increment
    plot_snake(gameWindow,black,snk_lst,snake_size)

    """logic for length increasing too much"""
    if len(snk_lst)>snk_length:
        del snk_lst[0]

    """food in game"""
    pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])

    # to make any change in program appear in game use  update
    pygame.display.update()
    clock.tick(fps)

pygame.quit()
quit()
