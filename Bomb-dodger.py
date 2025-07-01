import pygame
import random

pygame.init()
score = 0
screen = pygame.display.set_mode((500, 500))
font = pygame.font.SysFont("Pixeltype.ttf", 36)

bomb1 = pygame.Rect(random.randint(0, 250), 0, 25, 25)
bomb2 = pygame.Rect(random.randint(250, 480), 0, 25, 25)
bomb3 = pygame.Rect(random.randint(0, 250), 0, 25, 25)
bomb4 = pygame.Rect(random.randint(250, 480), 0, 25, 25)
bomb5 = pygame.Rect(random.randint(0, 250), 0, 25, 25)
bomb6 = pygame.Rect(random.randint(250, 480), 0, 25, 25)
bomb7 = pygame.Rect(random.randint(0, 250), 0, 25, 25)

bomb8 = pygame.Rect(0, random.randint(0, 250), 25, 25)
bomb9 = pygame.Rect(0, random.randint(250, 480), 25, 25)
bomb10 = pygame.Rect(0, random.randint(0, 250), 25, 25)
bomb11 = pygame.Rect(0, random.randint(250, 480), 25, 25)

player = pygame.Rect(250, 460, 20, 20)

running = True
clock = pygame.time.Clock()
while running:
    screen.fill((0, 255, 255))
    clock.tick(60)
    pygame.time.delay(-100)

    for bomb in [bomb1, bomb2, bomb3, bomb4, bomb5, bomb6, bomb7]:
        pygame.draw.rect(screen, (255, 0, 0), bomb)

    for bomb in [bomb8, bomb9, bomb10, bomb11]:
        pygame.draw.rect(screen, (255, 0, 0), bomb)

    pygame.draw.rect(screen, (0, 0, 0), player)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] and player.x > 0:
        player.x -= 5
    if keys[pygame.K_d] and player.x < 470:
        player.x += 5
    if keys[pygame.K_w] and player.y > 0:
        player.y -= 5
    if keys[pygame.K_s] and player.y < 480:
        player.y += 5

    for bomb in [bomb1, bomb2, bomb3, bomb4, bomb5, bomb6, bomb7]:
        bomb.y += 3
        if bomb.y > 500:
            bomb.y = 0
            bomb.x = random.randint(0, 480)
            score += 1

    for bomb in [bomb8, bomb9, bomb10, bomb11]:
        bomb.x += 3
        if bomb.x > 500:
            bomb.x = 0
            bomb.y = random.randint(0, 480)
            score += 1

    for bomb in [bomb1, bomb2, bomb3, bomb4, bomb5, bomb6, bomb7, bomb8, bomb9, bomb10, bomb11]:
        if bomb.colliderect(player):
            print("Game Over!!")
            running = False
            break

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = Falsea
    
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    

    pygame.display.update()

print("Your score is:", score)
pygame.quit()