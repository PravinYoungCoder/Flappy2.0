import pygame
from random import randint
pygame.mixer.init()
pygame.mixer.music.load("Today's Plan - DJ Freedem.mp3")
pygame.init()
display = pygame.display.set_mode((320, 568))
text = pygame.font.Font(None, 50)
bg = pygame.image.load('bg.png')
bird = pygame.image.load('bird.png')
top_pole_height = randint(100,400)
pole_width = 70
pole_color = (220, 85, 57)
pole_X = 320
pole_gap = 100
bird_Y = 150
bird_X = 20
clock = pygame.time.Clock()
score = 0
pygame.mixer.music.play()

while True:
    pygame.event.get()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        bird_Y = bird_Y-3
    if keys[pygame.K_DOWN]:
        bird_Y = bird_Y+6

    display.blit(bg, (0,0))
    display.blit(bird, (bird_X, bird_Y))
    pole_X = pole_X-2
    if pole_X <= -pole_width:
        pole_X = 320
        top_pole_height = randint(50,400)
        score = score+20
    pygame.draw.rect(display, pole_color, (pole_X, 0, pole_width, top_pole_height))
    pygame.draw.rect(display, pole_color, (pole_X, top_pole_height+pole_gap, pole_width, 568))

    #collision
    if pole_X <= bird_X+50 and bird_X <= pole_X+pole_width:
        if bird_Y <= top_pole_height or bird_Y >= top_pole_height+pole_gap:
            break
    score_text = text.render(f'Score: {score}', True, "white")
    display.blit(score_text, (0,0))
    pygame.display.update()
    clock.tick(60)
print(f'You have scored {score} points')
