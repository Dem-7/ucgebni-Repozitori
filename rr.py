import pygame
import time
pygame.init()
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Тестовый проект")

image = pygame.image.load("r.png")
image_rect = image.get_rect()
image2 = pygame.image.load("nn.png.jpg")
image_rect2 = image2.get_rect()



speed = 5


run = True
while run:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False
    screen.fill((0, 0, 0))
    screen.blit(image2, image_rect2)

    screen.blit(image, image_rect)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        image_rect.x +=speed
    if keys[pygame.K_LEFT]:
        image_rect.x -= speed
    if keys[pygame.K_UP]:
        image_rect.y-= speed
    if keys[pygame.K_DOWN]:
        image_rect.y += speed

    if event.type == pygame.MOUSEMOTION:
        mouseX , mouseY = pygame.mouse.get_pos()
        image_rect.x = mouseX - 280
        image_rect.y = mouseY - 280
    if  image_rect.colliderect(image_rect2):
        print("Произошло столкновение")
        time.sleep(1)


    pygame.display.flip()
pygame.quit()

