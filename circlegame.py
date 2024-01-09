# Example file showing a circle moving on screen
import pygame

class Bullet():
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
delta = 0

bullet = Bullet(pygame.Vector2(10,200),0)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("blue")

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        bullet.velocity = 1000

    bullet.position.x += bullet.velocity * delta
    pygame.draw.circle(screen, "red", bullet.position, 20)
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    delta = clock.tick(60) / 1000

pygame.quit()