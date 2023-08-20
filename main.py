import pygame as py

# starting variables
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# beginning of py
py.init()

# special variables
FPS_clock = py.time.Clock()
width = 1000
height = 600
screen = py.display.set_mode((width, height))
py.display.set_caption("Maze Game!")

game_font = py.font.SysFont('Impact', 40)
screen.fill(BLACK)

running = True

WALLS = [
    py.Rect(25, 0, 20, 540),
    py.Rect(70, 0, 20, 200),
    py.Rect(70, 230, 20, 375),
    py.Rect(115, 0, 20, 200),
    py.Rect(115, 0, 20, 540),
    py.Rect(160, 0, 20, 200),
    py.Rect(160, 230, 20, 375),
    py.Rect(205, 0, 20, 200),
    py.Rect(205, 0, 20, 540),
    py.Rect(250, 0, 20, 200),
    py.Rect(250, 230, 20, 375),
    py.Rect(295, 0, 20, 540),
    py.Rect(295, 0, 20, 200),
    py.Rect(340, 230, 20, 375),
    py.Rect(340, 0, 20, 200),
    py.Rect(385, 0, 20, 540),
    py.Rect(385, 0, 20, 200),
    py.Rect(430, 230, 20, 375),
    py.Rect(430, 0, 20, 200),
    py.Rect(475, 0, 20, 540),
    py.Rect(475, 0, 20, 200),
    py.Rect(520, 50, 85, 85),
    py.Rect(520, 160, 85, 85),
    py.Rect(520, 270, 85, 85),
    py.Rect(520, 380, 85, 85),
    py.Rect(520, 490, 415, 85),
    py.Rect(630, 50, 85, 85),
    py.Rect(630, 160, 85, 85),
    py.Rect(630, 270, 85, 85),
    py.Rect(630, 380, 85, 85),
    py.Rect(630, 490, 85, 85),
    py.Rect(740, 50, 85, 85),
    py.Rect(740, 160, 85, 85),
    py.Rect(740, 270, 85, 85),
    py.Rect(740, 380, 85, 85),
    py.Rect(740, 490, 85, 85),
    py.Rect(850, 50, 85, 85),
    py.Rect(850, 160, 85, 85),
    py.Rect(850, 270, 85, 85),
    py.Rect(850, 380, 85, 85),
    py.Rect(850, 490, 85, 85)
]

# main() as function for starter
def main(speed, player_x, player_y, player_vel_x, player_vel_y):
    global running
    while running:
        FPS_clock.tick(30)

        for event in py.event.get():
            if event.type == py.QUIT:
                running = False

        # WASD detection
        pressed = py.key.get_pressed()
        if pressed[py.K_w]:
            player_vel_y -= speed
        if pressed[py.K_s]:
            player_vel_y += speed
        if pressed[py.K_a]:
            player_vel_x -= speed
        if pressed[py.K_d]:
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
        player = py.Rect(player_x, player_y, 15, 15)
        py.draw.rect(screen, WHITE, player)

        # defining winning square
        winning = py.Rect(940, 25, 65, 550)

        # defining borders
        bottom_border = py.Rect(0, 575, 1000, 25)
        top_border = py.Rect(0, 0, 1000, 25)

        # drawing winning square
        py.draw.rect(screen, GREEN, winning)

        # drawing borders
        py.draw.rect(screen, RED, bottom_border)
        py.draw.rect(screen, RED, top_border)

        # drawing the wall part of maze
        for x in WALLS:
            py.draw.rect(screen, RED, x)

        # a = False means creative mode xdxdxdxdxdxdxddxd
        hack = False
        if (any(player.colliderect(x) and hack for x in WALLS)):
            player_x = 0
            player_y = 35

        # if player reaches the end
        if player.colliderect(winning):
            screen.fill(BLACK)
            ending = game_font.render("Congratulations on finishing! You win!", False, GREEN)
            screen.blit(ending, (200, 250))

        # updates display
        py.display.update()
        screen.fill(BLACK)


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
