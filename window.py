import pygame

# "Initate" the creation of the window
pygame.init()

# Window Size
width = 800
height = 600


# Creates the window
window = pygame.display.set_mode((width, height))

# Sets teh title for the window
pygame.display.set_caption("Window")

# Makes window stay open
running = True
while running:
    # Handel the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:

            # If the window is closed, the game won't run in the background
            running = False

    # Fill the screen with the color white
    window.fill((255,255,255))

    # Update display
    pygame.display.flip()

# Quit the game
pygame.quit()