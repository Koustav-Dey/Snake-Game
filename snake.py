import pygame
import random
import os

pygame.mixer.init()


pygame.init()

white=(255, 255, 255)
red = (255, 0, 0)
black = (0 , 0 ,0)
green = (0,128,0)
orange =(255, 21, 0)

screen_width = 1200
screen_heigth = 600
gameWindow = pygame.display.set_mode((screen_width, screen_heigth))


bgimg = pygame.image.load("back.jpg")
bgimg = pygame.transform.scale(bgimg, (screen_width, screen_heigth)).convert_alpha()


fntimg = pygame.image.load("front.jpg")
fntimg = pygame.transform.scale(fntimg, (screen_width, screen_heigth)).convert_alpha()

overimg = pygame.image.load("over.jpg")
overimg = pygame.transform.scale(overimg, (screen_width, screen_heigth)).convert_alpha()



pygame.display.set_caption("Snake Game")
pygame.display.update()
font = pygame.font.SysFont(None, 55)
clock = pygame.time.Clock()



def text_screen(text, color, x,y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text,[x,y])


def plot_snake(gameWindow , color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow , color, [x, y, snake_size, snake_size])

def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill((222,200,164))
        gameWindow.blit(fntimg,(0,0) )
        text_screen("WELCOME IN SNAKES", orange, 350,250)
        text_screen("Press Spacebar To Play", orange, 350,350)
        
        

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        pygame.mixer.music.load('back.mp3')
                        pygame.mixer.music.play()
                        gameloop()



        pygame.display.update()
        clock.tick(60)


def gameloop():


    snk_list = []
    snk_length = 1
    exit_game = False
    game_over = False
    snake_size = 20
    snake_x = 45
    snake_y = 55
    score = 0
    fps = 60
    velocity_x = 0
    velocity_y = 0
    init_velocity = 3

    food_x = random.randint(20, screen_width/2)
    food_y = random.randint(20,screen_heigth/2)



    if (not os.path.exists("Highscore.txt")):
        with open("Highscore.txt", "w") as f:
            f.write("0")

    with open("Highscore.txt", "r") as f:
        Highscore = f.read()
        
    # pygame.display.update()

    while not exit_game:
        if game_over:
            with open("Highscore.txt", "w") as f:
                f.write(str(Highscore))
                
            gameWindow.fill(white)
            gameWindow.blit(overimg,(0,0) )
            text_screen("Press Enter to Continue ", red, 380, 530 )
            for event in pygame.event.get():
                # print(event)
                if event.type == pygame.QUIT:
                    exit_game = True


                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN or pygame.K_SPACE:
                        welcome()


        else:


            for event in pygame.event.get():
                # print(event)
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0
                        # snake_x = snake_x + 10
                    
                    if event.key == pygame.K_LEFT:
                        # snake_x = snake_x - 10
                        velocity_x = - init_velocity
                        velocity_y = 0
                    
                    if event.key == pygame.K_UP:
                        # snake_y = snake_y - 10
                        velocity_y = - init_velocity
                        velocity_x = 0
                    
                    if event.key == pygame.K_DOWN:
                        # snake_y = snake_y + 10
                        velocity_y = init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_s:
                        score +=10



            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x)<12 and abs(snake_y - food_y)<12:
                score+=10
                
                # print("score : ",score * 10)
                food_x = random.randint(20, screen_width/2)
                food_y = random.randint(20,screen_heigth/2)
                snk_length += 4
                if score > int(Highscore):
                    Highscore = score
                    pygame.mixer.music.load('highscore.mp3')
                    pygame.mixer.music.play()

            gameWindow.fill(white)
            gameWindow.blit(bgimg,(0,0) )
            text_screen("    Score : " + str(score) + "        HighScore : "+str(Highscore) , green, 5, 5)
            pygame.draw.rect(gameWindow , red, (food_x, food_y, snake_size, snake_size))
            
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True
                pygame.mixer.music.load('gameover.mp3')
                pygame.mixer.music.play()
                

            if snake_x<0 or snake_x>screen_width or snake_y <0 or snake_y>screen_heigth:
                game_over = True
                print("Game Over")
                pygame.mixer.music.load('gameover.mp3')
                pygame.mixer.music.play()
            
            
            pygame.draw.rect(gameWindow , black, (snake_x, snake_y, snake_size, snake_size))
            plot_snake(gameWindow , black, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
# gameloop()
welcome()
    


