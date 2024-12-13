import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Game settings
WIDTH, HEIGHT = 1440, 1080
BG_COLOR = (255, 255, 255)
FPS = 60

# Moves dictionary
moves = {
    pygame.K_r: "Rock",
    pygame.K_p: "Paper",
    pygame.K_s: "Scissors"
}

# Results dictionary
results = {
    "Rock": {"Rock": "Draw", "Paper": "Lose", "Scissors": "Win"},
    "Paper": {"Rock": "Win", "Paper": "Draw", "Scissors": "Lose"},
    "Scissors": {"Rock": "Lose", "Paper": "Win", "Scissors": "Draw"}
}

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rock-Paper-Scissors Game")

font = pygame.font.Font(None, 36)

clock = pygame.time.Clock()

def display_result(result):
    result_text = font.render(result, True, (0, 0, 0))
    screen.blit(result_text, (WIDTH // 2 - result_text.get_width() // 2, HEIGHT // 2 - result_text.get_height() // 2))
    pygame.display.flip()
    pygame.time.delay(2000)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key in moves:
                player_move = moves[event.key]
                computer_move = random.choice(list(moves.values()))

                result = results[player_move][computer_move]
                display_result(result)

    screen.fill(BG_COLOR)
                                                           
    text = font.render("""Press R for Rock ,                                                      S for Scissors
    P for Paper ,                   """, True, (0, 0, 0))



    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))

    pygame.display.flip()
    clock.tick(FPS)
