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
    
    display.blit(bg, (0, 0))
    display.blit(bird, (birdX, birdY))
    pygame.display.update()
    
