import pygame
import sys

pygame.init()

# Screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car on Road")

# Colors
BLACK = (0, 0, 0)
GRAY = (50, 50, 50)
WHITE = (255, 255, 255)
RED = (200, 0, 0)

clock = pygame.time.Clock()

# Car
car_width = 50
car_height = 80
car_x = WIDTH // 2 - car_width // 2
car_y = HEIGHT - 120
car_speed = 5

road_line_y = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car_x > 200:
        car_x -= car_speed
    if keys[pygame.K_RIGHT] and car_x < 550:
        car_x += car_speed

    # Draw grass
    screen.fill((0, 150, 0))

    # Draw road
    pygame.draw.rect(screen, GRAY, (200, 0, 400, 600))

    # Road moving lines
    road_line_y += 5
    if road_line_y > HEIGHT:
        road_line_y = 0

    for i in range(10):
        pygame.draw.rect(screen, WHITE, (395, i * 100 + road_line_y, 10, 50))

    # Draw car
    pygame.draw.rect(screen, RED, (car_x, car_y, car_width, car_height))

    pygame.display.update()
    clock.tick(60)
