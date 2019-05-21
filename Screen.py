import pygame
import random
pygame.init()

size = width, height = 800, 600
screen = pygame.display.set_mode(size)

pygame.display.set_caption('DVD Bouncy thing')

logo1 = pygame.image.load("dvd_blue.png")
logo1 = pygame.transform.scale(logo1, (185, 100))
logo2 = pygame.image.load("dvd_green.png")
logo2 = pygame.transform.scale(logo2, (185, 100))
logo3 = pygame.image.load("dvd_red.png")
logo3 = pygame.transform.scale(logo3, (185, 100))
logo4 = pygame.image.load("dvd_yellow.png")
logo4 = pygame.transform.scale(logo4, (185, 100))
logos = [logo1, logo2, logo3, logo4]
rect = logos[0].get_rect()

rect.left = random.randint(0, width - rect.right)
rect.top = random.randint(0, height-rect.bottom)
speed = [4, 2]
clock = pygame.time.Clock()
fps = 60
colorCounter = 0

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if rect.left < 0:
        speed[0] = -speed[0]
        colorCounter += 1
    if rect.right > width:
        speed[0] = -speed[0]
        colorCounter += 1
    if rect.top < 0:
        speed[1] = -speed[1]
        colorCounter += 1
    if rect.bottom > height:
        speed[1] = -speed[1]
        colorCounter += 1

    if colorCounter >= 4:
        colorCounter = 0

    rect.left += speed[0]
    rect.top += speed[1]
    screen.fill((0, 0, 0))
    screen.blit(logos[colorCounter], rect)
    pygame.display.update()
    clock.tick(fps)

pygame.quit()

