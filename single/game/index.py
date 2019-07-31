import pygame
from random import randint
from enum import Enum, unique


class Color(Enum):

    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GRAY = (242, 242, 242)

    @staticmethod
    def random_color():
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        return (r, g, b)


class Ball(object):
    def __init__(self, x, y,
                 radius=10, color=Color.random_color(), sx=1, sy=1):
        self.x = x
        self.y = y
        self.sx = sx
        self.sy = sy
        self.radius = radius
        self.color = color
        self.alive = True

    def move(self, screen):
        self.x += self.sx
        self.y += self.sy
        r = self.radius
        if self.x-r <= 0 or self.x+r >= screen.get_width():
            self.sx = -self.sx
        if self.y-r <= 0 or self.y+r >= screen.get_height():
            self.sy = -self.sy

    def draw(self, screen):
        pygame.draw.circle(screen, self.color,
                           (self.x, self.y), self.radius, 0)


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('大球吃小球')
    screen.fill((242, 242, 242))
    bg_img = pygame.image.load('./bg.jpeg').convert()
    bg_img = pygame.transform.scale(bg_img, (800, 600))
    pygame.display.flip()
    balls = []
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                ball = Ball(x, y, randint(10, 30), Color.random_color(),
                            randint(-5, 5), randint(-5, 5))
                balls.append(ball)
        screen.blit(bg_img, (0, 0, 800, 600))
        for ball in balls:
            if ball.alive:
                ball.draw(screen)
            else:
                balls.remove(ball)
        pygame.display.flip()

        pygame.time.delay(8)
        for ball in balls:
            ball.move(screen)


if __name__ == '__main__':
    main()
