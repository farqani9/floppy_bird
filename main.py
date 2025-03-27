import pygame
import random
import sys
from typing import Tuple, List

# Initialize Pygame
pygame.init()

# Game Constants
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
FPS = 60
GRAVITY = 0.5
BIRD_JUMP = -10
PIPE_SPEED = 3
PIPE_SPAWN_TIME = 2000  # milliseconds
PIPE_GAP = 200
PIPE_WIDTH = 70

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
SKY_BLUE = (135, 206, 235)

# Game Setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Floppy Bird")
clock = pygame.time.Clock()

class Bird:
    def __init__(self):
        self.x = SCREEN_WIDTH // 3
        self.y = SCREEN_HEIGHT // 2
        self.velocity = 0
        self.rect = pygame.Rect(self.x, self.y, 30, 30)

    def jump(self):
        self.velocity = BIRD_JUMP

    def update(self):
        self.velocity += GRAVITY
        self.y += self.velocity
        self.rect.y = self.y

    def draw(self):
        pygame.draw.rect(screen, BLACK, self.rect)

class Pipe:
    def __init__(self):
        self.gap_y = random.randint(PIPE_GAP, SCREEN_HEIGHT - PIPE_GAP)
        self.x = SCREEN_WIDTH
        self.passed = False
        
        # Top pipe
        self.top_height = self.gap_y - PIPE_GAP // 2
        self.top_rect = pygame.Rect(self.x, 0, PIPE_WIDTH, self.top_height)
        
        # Bottom pipe
        self.bottom_y = self.gap_y + PIPE_GAP // 2
        self.bottom_height = SCREEN_HEIGHT - self.bottom_y
        self.bottom_rect = pygame.Rect(self.x, self.bottom_y, PIPE_WIDTH, self.bottom_height)

    def update(self):
        self.x -= PIPE_SPEED
        self.top_rect.x = self.x
        self.bottom_rect.x = self.x

    def draw(self):
        pygame.draw.rect(screen, GREEN, self.top_rect)
        pygame.draw.rect(screen, GREEN, self.bottom_rect)

class Game:
    def __init__(self):
        self.bird = Bird()
        self.pipes: List[Pipe] = []
        self.score = 0
        self.game_over = False
        self.last_pipe = pygame.time.get_ticks()
        self.font = pygame.font.Font(None, 36)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if self.game_over:
                        self.__init__()  # Reset game
                    else:
                        self.bird.jump()

    def update(self):
        if not self.game_over:
            # Update bird
            self.bird.update()

            # Spawn new pipes
            now = pygame.time.get_ticks()
            if now - self.last_pipe > PIPE_SPAWN_TIME:
                self.pipes.append(Pipe())
                self.last_pipe = now

            # Update and check pipes
            for pipe in self.pipes[:]:
                pipe.update()
                
                # Check collision
                if (self.bird.rect.colliderect(pipe.top_rect) or 
                    self.bird.rect.colliderect(pipe.bottom_rect)):
                    self.game_over = True
                
                # Score points
                if not pipe.passed and pipe.x < self.bird.x:
                    self.score += 1
                    pipe.passed = True
                
                # Remove off-screen pipes
                if pipe.x < -PIPE_WIDTH:
                    self.pipes.remove(pipe)

            # Check screen boundaries
            if self.bird.y < 0 or self.bird.y > SCREEN_HEIGHT:
                self.game_over = True

    def draw(self):
        screen.fill(SKY_BLUE)
        
        # Draw game elements
        self.bird.draw()
        for pipe in self.pipes:
            pipe.draw()

        # Draw score
        score_text = self.font.render(f"Score: {self.score}", True, BLACK)
        screen.blit(score_text, (10, 10))

        # Draw game over message
        if self.game_over:
            game_over_text = self.font.render("Game Over! Press SPACE to restart", True, BLACK)
            text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
            screen.blit(game_over_text, text_rect)

        pygame.display.flip()

def main():
    game = Game()
    
    while True:
        game.handle_events()
        game.update()
        game.draw()
        clock.tick(FPS)

if __name__ == "__main__":
    main()