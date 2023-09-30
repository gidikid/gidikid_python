import random
import pygame

# Initialize Pygame
pygame.init()

# Set up the window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Colored Circles")

# Colors dictionary
colors = {"red": (255, 0, 0), "green": (0, 255, 0), "blue": (0, 0, 255)}

# Circles list
circles_coulor = colors["red"]
circle_radius = 70

def get_random_values():
    end = random.randint
    x, y = random.randint(10,  (window_width - 10)), random.randint(10,  (window_height - 10))
    radius = random.randint(10, 50)

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Set the background color
    window.fill((255, 255, 255))  # RGB color: white

    # Draw circles
    for circle in circles:
        x, y, radius, color_name = circle
        color = colors[color_name]
        pygame.draw.circle(window, color, (x, y), radius)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                x, y, radius, color_name = circle
        color = colors[color_name]
        pygame.draw.circle(window, color, (x, y), radius)
        