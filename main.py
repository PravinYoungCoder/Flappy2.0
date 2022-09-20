import pygame
from random import randint
pygame.mixer.init()
pygame.mixer.music.load("Today's Plan - DJ Freedem.mp3")
pygame.init()
display = pygame.display.set_mode((320, 568))
text= pygame.font.Font(None, 50)
bg = pygame.image.load('bg.png')
bird = pygame.image.load('bird.png')
pole_width = 70
top_pole_height = randint(100, 400)
pole_color = (220, 85, 57)
pole_gap = 100
pole_X = 320
birdY = 150
birdX = 20
clock = pygame.time.Clock()
score = 0
pygame.mixer.music.play()
while True:
    pygame.event.get()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        birdY = birdY-3
    if keys[pygame.K_DOWN]:
        birdY = birdY+6
    display.blit(bg, (0, 0))
    display.blit(bird, (birdX, birdY))
    pole_X = pole_X-2
    if pole_X <= -pole_width:
        pole_X = 320
        top_pole_height = randint(50,400)
        score = score+20
    pygame.draw.rect(display, pole_color, (pole_X, 0, pole_width, top_pole_height))
    pygame.draw.rect(display, pole_color, (pole_X, top_pole_height+pole_gap, pole_width, 568))

    #collision
    if pole_X <= birdX+50 and birdX <= pole_X+pole_width:
        if birdY <= top_pole_height or birdY >= top_pole_height+pole_gap:
            break
    score_text = text.render(f'Score: {score}', True, "white")
    display.blit(score_text, (0,0))
    pygame.display.update()
    clock.tick(60)
print("You Die!")
print(f"The score is {score}")
