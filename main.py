import pygame
# starting variables
red = (255, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)
black = (0, 0, 0)

# beginning of pygame
#bruh
pygame.init()

# special variables
FPS_clock = pygame.time.Clock()
width = 1000
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Maze Game!")

game_font = pygame.font.SysFont('Impact', 40)
screen.fill(black)

walls = [
    pygame.Rect(25, 0, 20, 540),
pygame.Rect(70, 0, 20, 200),
pygame.Rect(70, 230, 20, 375),
pygame.Rect(115, 0, 20, 200),
pygame.Rect(115, 0, 20, 540),
pygame.Rect(160, 0, 20, 200),
pygame.Rect(160, 230, 20, 375),
pygame.Rect(205, 0, 20, 200),
pygame.Rect(205, 0, 20, 540),
pygame.Rect(250, 0, 20, 200),
pygame.Rect(250, 230, 20, 375),
pygame.Rect(295, 0, 20, 540),
pygame.Rect(295, 0, 20, 200),
pygame.Rect(340, 230, 20, 375),
pygame.Rect(340, 0, 20, 200),
pygame.Rect(385, 0, 20, 540),
pygame.Rect(385, 0, 20, 200),
pygame.Rect(430, 230, 20, 375),
pygame.Rect(430, 0, 20, 200),
pygame.Rect(475, 0, 20, 540),
pygame.Rect(475, 0, 20, 200),
 pygame.Rect(520, 50, 85, 85),
 pygame.Rect(520, 160, 85, 85),
 pygame.Rect(520, 270, 85, 85),
 pygame.Rect(520, 380, 85, 85),
 pygame.Rect(520, 490, 415, 85),
 pygame.Rect(630, 50, 85, 85),
 pygame.Rect(630, 160, 85, 85),
 pygame.Rect(630, 270, 85, 85),
 pygame.Rect(630, 380, 85, 85),
 pygame.Rect(630, 490, 85, 85),
 pygame.Rect(740, 50, 85, 85),
 pygame.Rect(740, 160, 85, 85),
 pygame.Rect(740, 270, 85, 85),
 pygame.Rect(740, 380, 85, 85),
 pygame.Rect(740, 490, 85, 85),
 pygame.Rect(850, 50, 85, 85),
 pygame.Rect(850, 160, 85, 85),
 pygame.Rect(850, 270, 85, 85),
 pygame.Rect(850, 380, 85, 85),
 pygame.Rect(850, 490, 85, 85)
]

# main() as function for starter
def main(speed, player_x, player_y, player_vel_x, player_vel_y):
    while True:
        FPS_clock.tick(100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_w]:
            player_vel_y -= speed
        if pressed[pygame.K_s]:
            player_vel_y += speed
        if pressed[pygame.K_a]:
            player_vel_x -= speed
        if pressed[pygame.K_d]:
            player_vel_x += speed

        # movement mechanism
        player_x += player_vel_x
        player_y += player_vel_y
        player_vel_x *= 0.9
        player_vel_y *= 0.9

        # border detection
        if player_x < 0:
            player_x = 0
        elif player_y < 0:
            player_y = 0
        elif player_x > width - 15:
            player_x = width - 15
        elif player_y > height - 15:
            player_y = height - 15

        # initiation of player
        player_controlled = pygame.Rect(player_x, player_y, 15, 15)
        pygame.draw.rect(screen, white, player_controlled)

        # defining winning square
        winning = pygame.Rect(940, 25, 65, 550)

        # defining borders
        bottom_border = pygame.Rect(0, 575, 1000, 25)
        top_border = pygame.Rect(0, 0, 1000, 25)

        # drawing winning square
        pygame.draw.rect(screen, green, winning)

        # drawing borders
        pygame.draw.rect(screen, red, bottom_border)
        pygame.draw.rect(screen, red, top_border)

        # drawing the wall part of maze
        for x in walls:
            pygame.draw.rect(screen, red, x)

        # a = False means creative mode xdxdxdxdxdxdxddxd
        a = False
        for x in walls:
            if player_controlled.colliderect(x) and a:
                player_x = 0
                player_y = 35

        # if player reaches the end
        if player_controlled.colliderect(winning):
            screen.fill(black)
            ending = game_font.render("Congratulations on finishing! You win!", False, green)
            screen.blit(ending, (200, 250))

        # updates display
        pygame.display.update()
        screen.fill(black)


# difficulty selector
difficulty = int(input("choose a dificulty from 1 to 4"))
if difficulty == 1:
    main(0.1, 0, 35, 0, 0)
elif difficulty == 2:
    main(0.15, 0, 35, 0, 0)
elif difficulty == 3:
    main(0.2, 0, 35, 0, 0)
elif difficulty == 4:
    main(0.5, 0, 35, 0, 0)
elif difficulty not in [1, 2, 3, 4]:
    difficulty = eval(input("Choose a difficulty, the higher the number, the harder it is(1-4) "))
