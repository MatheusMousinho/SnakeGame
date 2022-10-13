import pygame, random
from pygame.locals import *
from time import sleep

pygame.init()

def on_grid_random():
    x = random.randint(0,590)
    y = random.randint(0,590)
    return(x//10 * 10, y//10 * 10)

def collision(c1,c2):
    return(c1[0] == c2[0]) and (c1[1] == c2[1])

game_over = False
SPEED = 15
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('Snake')

snake = [(200,200), (210,200), (220,200)]
snake_skin = pygame.Surface((10,10)) 
snake_skin.fill((255,255,255))

apple_pos = on_grid_random()
apple = pygame.Surface((10,10))
apple.fill((255,0,0))

my_direction = LEFT

SIZE = len(snake) - 1

clock = pygame.time.Clock()

while True:
    clock.tick(SPEED)

    

    for event in pygame.event.get():
        
        if event.type == QUIT:
            pygame.quit()

        if event.type == KEYDOWN:
            if event.key == K_UP:
                my_direction = UP
            if event.key == K_DOWN:
                my_direction = DOWN
            if event.key == K_LEFT:
                my_direction = LEFT
            if event.key == K_RIGHT:
                my_direction = RIGHT

    if collision(snake[0], apple_pos):
        apple_pos = on_grid_random()
        snake.append((0,0))
        SPEED = SPEED + 1

    if snake[0][0] == 600 or snake[0][1] == 600 or snake[0][0] < 0 or snake[0][1] < 0:
        game_over = True
        sleep(1.5)
        break

    for x in range(2, len(snake) -1):
        if snake[0][0] == snake[x][0] and snake[0][1] == snake [x][1]:
            game_over= True
            sleep(1.5)
            break

    if (game_over == True):
        break

    if my_direction == UP:  
        snake[0] = (snake[0][0], snake[0][1] -10)
    if my_direction == DOWN:  
        snake[0] = (snake[0][0], snake[0][1] +10)
    if my_direction == RIGHT:  
        snake[0] = (snake[0][0] +10, snake[0][1])
    if my_direction == LEFT:  
        snake[0] = (snake[0][0] -10, snake[0][1])

    for i in range(len(snake) -1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])


    screen.fill((0,0,0))
    screen.blit(apple, apple_pos)
    for pos in snake:
        screen.blit(snake_skin,pos)

    pygame.display.update()