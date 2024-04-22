import math
import random
import time
import pygame
pygame.init()

# ramas la 8.23.45


WIDTH, HEIGHT = 800, 600

WIN = pygame.display.set_mode((WIDTH, HEIGHT)) # initializing a pygame window and dysplay it on the screen
pygame.display.set_caption("Aim Trainer")

TARGET_INCREMENT = 400 # time of apearence of targe
TARGE_EVENT = pygame.USEREVENT

TARGET_PADDING = 30

BG_COLOR = (0, 25, 40) # 0 red, 25 green, 40 blue
LIVES = 5
TOP_BAR_HEIGHT = 50

LABEL_FONT = pygame.font.SysFont("comicsans", 24)


class Target:
    MAX_SIZE = 30
    GROWTH_RATE = 0.2
    COLOR = "red"
    SECOND_COLOR = "white"


    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 0
        self.grow = True


    def update(self):
        if self.size + self.GROWTH_RATE >= self.MAX_SIZE:
            self.grow = False

        if self.grow:
            self.size += self.GROWTH_RATE #growing  
        else:
            self.size -= self.GROWTH_RATE   # shrinking


    def draw(self, win): #draw target as 4 circles smaller in order of different colors
        pygame.draw.circle(win, self.COLOR, (self.x, self.y), self.size)
        pygame.draw.circle(win, self.SECOND_COLOR, (self.x, self.y), self.size * 0.8)
        pygame.draw.circle(win, self.COLOR, (self.x, self.y), self.size * 0.6)
        pygame.draw.circle(win, self.SECOND_COLOR, (self.x, self.y), self.size * 0.4)


    def collide(self, x, y): # mouse position on colide with target
        dis = math.sqrt(((x - self.x)**2) + ((y - self.y)**2))
        return dis <= self.size


def draw(win, targets):
    win.fill(BG_COLOR)
    #loop thru the targets
    for target in targets:
        target.draw(win)


def format_time(secs):
    milli = math.floor(int(secs * 1000 % 1000 / 100)) # nb of miliseconds from secs to display
    seconds = int(round(secs % 60, 1))
    minutes = int(secs // 60)

    return f"{minutes:02d}:{seconds:02d}.{milli}"
# 02d - format to start with 0 and another digit- 01, 02

def draw_top_bar(win, elapsed_time, targets_pressed, misses):
    pygame.draw.rect(win, "grey", (0, 0, WIDTH, TOP_BAR_HEIGHT))
    time_label = LABEL_FONT.render(f"Time: {format_time(elapsed_time)}", 1, "black")

    speed = round(targets_pressed / elapsed_time, 1)
    speed_label = LABEL_FONT.render(f"Speed: {speed} t/s", 1, "blue")

    hits = round(targets_pressed, 1)
    hits_label = LABEL_FONT.render(f"Hits: {hits}", 1, "purple")

    lives = round(LIVES - misses, 1)
    lives_label = LABEL_FONT.render(f"Lives: {lives}", 1, "red")

    win.blit(time_label, (5,5))
    win.blit(speed_label, (200,5))
    win.blit(hits_label, (450,5))
    win.blit(lives_label, (600,5))


def end_screen(win, elapsed_time, targets_pressed, clicks):
    win.fill(BG_COLOR)

    time_label = LABEL_FONT.render(f"Time: {format_time(elapsed_time)}", 1, "yellow")
    speed = round(targets_pressed / elapsed_time, 1)
    speed_label = LABEL_FONT.render(f"Speed: {speed} t/s", 1, "blue")

    hits = round(targets_pressed, 1)
    hits_label = LABEL_FONT.render(f"Hits: {hits}", 1, "purple")

    accuracy = round(targets_pressed / clicks * 100, 1)
    acc_label = LABEL_FONT.render(f"Accuracy: {accuracy}%", 1, "white")

    win.blit(time_label, (get_middle(time_label),100))
    win.blit(speed_label, (get_middle(speed_label),200))
    win.blit(hits_label, (get_middle(hits_label),300))
    win.blit(acc_label, (get_middle(acc_label),400))

    pygame.display.update()

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                quit()
# waiting to press a key to close the game


def get_middle(surface):
    return WIDTH / 2 - surface.get_width()/2 # draw in the middle

def main():
    run = True
    # custom event in time - make a new target
    targets = []
    clock = pygame.time.Clock()

    targets_pressed = 0
    clicks = 0 
    misses = 0 # end game at nb of missed targets
    start_time = time.time() # track time since started game


    pygame.time.set_timer(TARGE_EVENT, TARGET_INCREMENT) # trigger the target event every target increment

    while run:
        clock.tick(60) # nb of frames per second 
        click = False
        mouse_pos = pygame.mouse.get_pos()
        elapsed_time = time.time() - start_time

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

            if event.type == TARGE_EVENT:
                x = random.randint(TARGET_PADDING, WIDTH - TARGET_PADDING)
                y = random.randint(TARGET_PADDING + TOP_BAR_HEIGHT, HEIGHT - TARGET_PADDING)
                target = Target(x,y)
                targets.append(target)

            if event.type == pygame.MOUSEBUTTONDOWN: #mouse click on target
                click = True
                clicks += 1

        for target in targets:
            target.update()

            if target.size <= 0:
                targets.remove(target)
                misses += 1 
            
            if click and target.collide(*mouse_pos): # "*"-break down the tuple into individual element
                targets.remove(target)
                targets_pressed += 1   
        
        if misses >= LIVES:
            end_screen(WIN, elapsed_time, targets_pressed, clicks)
        draw(WIN, targets)
        draw_top_bar(WIN, elapsed_time, targets_pressed, misses)
        pygame.display.update() 

    pygame.quit()


if __name__ == "__main__":
    main()