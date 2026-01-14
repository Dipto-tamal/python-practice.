import pygame
import random
import sys

pygame.init()

# Screen
WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Real Bike Racing")

clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
GRAY = (60, 60, 60)
GREEN = (0, 150, 0)
RED = (220, 0, 0)
BLUE = (0, 100, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)

# Player Bike
bike_w, bike_h = 40, 80
bike_x = WIDTH // 2 - bike_w // 2
bike_y = HEIGHT - 120
bike_speed = 8

# Enemy Bikes
enemy_bikes = []
enemy_speed = 4
for i in range(4):
    x = random.randint(260, 600)
    y = random.randint(-600, -100)
    enemy_bikes.append([x, y])

# Road lines
line_y = 0

# Score
score = 0
font = pygame.font.SysFont(None, 36)

# Draw functions
def draw_bike(x, y):
    # Body
    pygame.draw.rect(screen, BLUE, (x + 10, y + 20, 20, 40))
    # Handle
    pygame.draw.line(screen, YELLOW, (x + 5, y + 20), (x + 35, y + 20), 4)
    # Wheels
    pygame.draw.circle(screen, BLACK, (x + 10, y + 65), 8)
    pygame.draw.circle(screen, BLACK, (x + 30, y + 65), 8)

def draw_enemy_bike(x, y):
    pygame.draw.rect(screen, RED, (x + 10, y + 20, 20, 40))
    pygame.draw.line(screen, YELLOW, (x + 5, y + 20), (x + 35, y + 20), 4)
    pygame.draw.circle(screen, BLACK, (x + 10, y + 65), 8)
    pygame.draw.circle(screen, BLACK, (x + 30, y + 65), 8)

def show_score():
    txt = font.render("Score: " + str(score), True, WHITE)
    screen.blit(txt, (10, 10))

def crash():
    txt = font.render("GAME OVER", True, RED)
    screen.blit(txt, (350, 250))
    pygame.display.update()
    pygame.time.delay(2500)
    pygame.quit()
    sys.exit()

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Player control
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and bike_x > 250:
        bike_x -= bike_speed
    if keys[pygame.K_RIGHT] and bike_x < 610:
        bike_x += bike_speed

    # Move enemy bikes
    for bike in enemy_bikes:
        bike[1] += enemy_speed
        if bike[1] > HEIGHT:
            bike[1] = random.randint(-400, -100)
            bike[0] = random.randint(260, 600)
            score += 1
            enemy_speed += 0.2

        # Collision detection
        if bike_y < bike[1] + 80 and bike_y + 80 > bike[1]:
            if bike_x < bike[0] + 40 and bike_x + 40 > bike[0]:
                crash()

    # Draw background
    screen.fill(GREEN)  # grass
    pygame.draw.rect(screen, GRAY, (240, 0, 420, 600))  # road

    # Road lines
    line_y += 10
    if line_y > HEIGHT:
        line_y = 0
    for i in range(10):
        pygame.draw.rect(screen, WHITE, (445, i * 100 + line_y, 10, 50))

    # Draw player bike
    draw_bike(bike_x, bike_y)

    # Draw enemy bikes
    for bike in enemy_bikes:
        draw_enemy_bike(bike[0], bike[1])

    # Show score
    show_score()

    pygame.display.update()
    clock.tick(60)

