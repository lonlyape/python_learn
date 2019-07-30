import pygame
import random


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('大球吃小球')
    screen.fill((242, 242, 242))
    bg_img = pygame.image.load('./bg.jpeg').convert()
    bg_img = pygame.transform.scale(bg_img, (800, 600))
    pygame.display.flip()
    running = True
    x, y = random.randint(30, 800-30), random.randint(30, 600-30)
    xv, yv = 1, 1
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.blit(bg_img, (0, 0, 800, 600))
        pygame.draw.circle(screen, (255, 0, 0), (x, y), 30, 0)
        pygame.display.flip()

        pygame.time.delay(2)
        x += xv
        y += yv
        if(x+30 >= 800 or x-30 <= 0):
            xv = -xv
        if(y+30 >= 600 or y-30 <= 0):
            yv = -yv


if __name__ == '__main__':
    main()
