import pygame
import random

pygame.init()

# Set up display
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# Set up initial snake speed and speed increase
initial_snake_speed = 10
speed_increase = 1  # Increase speed with every point scored

snake_speed = initial_snake_speed
snake = [(100, 50)]
snake_direction = (10, 0)
snake_length = 1
food = (random.randrange(0, width, 10), random.randrange(0, height, 10))
score = 0

font = pygame.font.Font(None, 36)

clock = pygame.time.Clock()

def collision_with_self():
    return snake[0] in snake[1:]

def collision_with_wall():
    x, y = snake[0]
    return x < 0 or x >= width or y < 0 or y >= height

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and snake_direction != (10, 0):
        snake_direction = (-10, 0)
    if keys[pygame.K_RIGHT] and snake_direction != (-10, 0):
        snake_direction = (10, 0)
    if keys[pygame.K_UP] and snake_direction != (0, 10):
        snake_direction = (0, -10)
    if keys[pygame.K_DOWN] and snake_direction != (0, -10):
        snake_direction = (0, 10)

    # Move the snake
    x, y = snake[0]
    new_x = (x + snake_direction[0]) % width
    new_y = (y + snake_direction[1]) % height
    snake.insert(0, (new_x, new_y))

    # Check for collision with food
    if snake[0] == food:
        snake_length += 1
        food = (random.randrange(0, width, 10), random.randrange(0, height, 10))
        score += 1
        snake_speed += speed_increase

    # Remove the tail
    if len(snake) > snake_length:
        snake.pop()

    # Check for collisions
    if collision_with_self() or collision_with_wall():
        running = False

    # Draw the screen
    screen.fill(black)
    for segment in snake:
        pygame.draw.rect(screen, white, (segment[0], segment[1], 10, 10))
    pygame.draw.rect(screen, green, (food[0], food[1], 10, 10))

    # Display score
    score_text = font.render(f"Score: {score}", True, white)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(snake_speed)

pygame.quit()
