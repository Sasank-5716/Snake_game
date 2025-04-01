import pygame
import time

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

# Game setup
snake = Snake()

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
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
    
    screen.fill(BLACK)
    snake.draw(screen)
    pygame.display.update()
    clock.tick(10)  # 10 FPS

pygame.quit()