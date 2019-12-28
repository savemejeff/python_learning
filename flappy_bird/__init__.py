import random
import pygame


class Bird(object):
    def __init__(self):
        self.x = 400
        self.y = 300
        self.color = (255, 0, 0)
        self.radius = 30
        self.alive = True
        self.a = 2
        self.v = 0

    def drop(self, screen):
        self.v += self.a
        if self.y + self.radius >= screen.get_height():
            self.v = 0
            self.alive = False
        self.y += self.v

    def bounce(self):
        self.v = -20

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius, 0)


class Pipe(object):
    def __init__(self):
        self.height = random.randint(100, 400)
        self.position = 800
        self.in_range = True

    def draw(self, screen):
        rect_up = pygame.Rect(self.position, 0, 100, self.height)
        rect_down = pygame.Rect(self.position, self.height+150, 100, 450-self.height)
        pygame.draw.rect(screen, (0, 255, 255), rect_up)
        pygame.draw.rect(screen, (0, 255, 255), rect_down)

    def move(self):
        self.position -= 10
        if self.position < -100:
            self.in_range = False

    def is_bird_alive(self, bird):
        if bird.x-bird.radius < self.position < bird.x+bird.radius:
            if (bird.y+bird.radius > self.height+150) or (bird.y-bird.radius < self.height):
                bird.alive = False


pygame.init()
# 初始化用于显示的窗口并设置窗口尺寸
screen = pygame.display.set_mode((800, 600))
# 设置当前窗口的标题
pygame.display.set_caption('flappy_bird')
bird = Bird()
pipes = []
running = True
while running:
    # 从消息队列中获取事件并对事件进行处理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # 处理鼠标事件的代码
        if event.type == pygame.MOUSEBUTTONDOWN:
            bird.bounce()
    screen.fill((0, 255, 0))
    if bird.alive:
        bird.draw(screen)
        if not pipes:
            pipe = Pipe()
            pipes.append(pipe)
        elif pipes[len(pipes) - 1].position < 600:
            pipe = Pipe()
            pipes.append(pipe)
        for pipe in pipes:
            if pipe.in_range:
                pipe.move()
                pipe.draw(screen)
                pipe.is_bird_alive(bird)
            else:
                pipes.remove(pipe)
    pygame.display.flip()
    pygame.time.delay(50)
    bird.drop(screen)

