import pygame
import time
import random

# Initialize pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Snake class
class Snake:
    def __init__(self):
        self.size = 20
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.dx = self.size
        self.dy = 0
        self.body = [(self.x, self.y)]
        self.length = 1
    
    def move(self):
        self.x += self.dx
        self.y += self.dy
        
        # Wrap around screen
        if self.x >= WIDTH:
            self.x = 0
        elif self.x < 0:
            self.x = WIDTH - self.size
        if self.y >= HEIGHT:
            self.y = 0
        elif self.y < 0:
            self.y = HEIGHT - self.size
        
        self.body.insert(0, (self.x, self.y))
        if len(self.body) > self.length:
            self.body.pop()
    
    def draw(self, screen):
        for segment in self.body:
            pygame.draw.rect(screen, GREEN, (segment[0], segment[1], self.size, self.size))

class Food:
    def __init__(self):
        self.size = 20
        self.x = random.randint(0, (WIDTH - self.size) // self.size) * self.size
        self.y = random.randint(0, (HEIGHT - self.size) // self.size) * self.size
    
    def draw(self, screen):
        pygame.draw.rect(screen, RED, (self.x, self.y, self.size, self.size))
    
    def respawn(self):
        self.x = random.randint(0, (WIDTH - self.size) // self.size) * self.size
        self.y = random.randint(0, (HEIGHT - self.size) // self.size) * self.size

# Game setup
snake = Snake()
food = Food()
score = 0
font = pygame.font.SysFont(None, 36)

def show_game_over(screen, score):
    screen.fill(BLACK)
    font_large = pygame.font.SysFont(None, 72)
    font_small = pygame.font.SysFont(None, 36)
    
    game_over_text = font_large.render("GAME OVER", True, WHITE)
    score_text = font_small.render(f"Final Score: {score}", True, WHITE)
    restart_text = font_small.render("Press R to Restart or Q to Quit", True, WHITE)
    
    screen.blit(game_over_text, (WIDTH//2 - game_over_text.get_width()//2, HEIGHT//2 - 100))
    screen.blit(score_text, (WIDTH//2 - score_text.get_width()//2, HEIGHT//2))
    screen.blit(restart_text, (WIDTH//2 - restart_text.get_width()//2, HEIGHT//2 + 100))
    pygame.display.update()
    
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return True
                elif event.key == pygame.K_q:
                    return False
    return False

def game_loop():
    snake = Snake()
    food = Food()
    score = 0
    font = pygame.font.SysFont(None, 36)
    
    running = True
    clock = pygame.time.Clock()
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and snake.dx == 0:
                    snake.dx = -snake.size
                    snake.dy = 0
                elif event.key == pygame.K_RIGHT and snake.dx == 0:
                    snake.dx = snake.size
                    snake.dy = 0
                elif event.key == pygame.K_UP and snake.dy == 0:
                    snake.dy = -snake.size
                    snake.dx = 0
                elif event.key == pygame.K_DOWN and snake.dy == 0:
                    snake.dy = snake.size
                    snake.dx = 0
        
        snake.move()
        
        # Check for food collision
        if snake.x == food.x and snake.y == food.y:
            snake.length += 1
            score += 1
            food.respawn()
            # Make sure food doesn't spawn on snake
            while (food.x, food.y) in snake.body:
                food.respawn()
        
        # Check for self-collision
        if (snake.x, snake.y) in snake.body[1:]:
            running = False
        
        screen.fill(BLACK)
        snake.draw(screen)
        food.draw(screen)
        
        # Display score
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))
        
        pygame.display.update()
        clock.tick(10)  # 10 FPS
    
    return show_game_over(screen, score)

# Main game
running = True
while running:
    running = game_loop()

pygame.quit()