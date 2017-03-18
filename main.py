
import  pygame
import random
import sys
import time

Max_x = 1366
Max_y = 768
Max_snow = 100   # макс кол-во снежинок
Snow_size = 64   # размер снежинки


class Snow:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = random.randint(1, 3) # использование случайных цыфр от 1 до 3 включительно
        self.img_num = random.randint(1, 3)     # какую картинку будем использовать
        self.image_filename = "snow" + str(self.img_num) + ".png" #будет перебором брать картинку
        self.image = pygame.image.load(self.image_filename).convert_alpha() # convert_alpha()
                                                                            #  если картинка без фона,
                                                                            # то и показывает  картинку без фона
        self.image = pygame.transform.scale(self.image, (Snow_size, Snow_size))  # уменьшаем нашу картинку

    def move_snow(self):
        self.y = self.y + self.speed
        if self.y > Max_y: # когда доходит до низа, то начинает сверху
            self.y = (0 - Snow_size)
        i = random.randint(1, 3)
        if i == 1:  # Move right
            self. x = self.x + 1
            if self.x > Max_x: # если дойдет до края стенки то начинает с другой стороны
                self.x = (0 - Snow_size)
        elif i == 2:     # Move left
            self.x -= 1
            if self.x < (0 - Snow_size):
                self.x = Max_x

    def draw_snow(self):    # рисует
        screen.blit(self.image, (self.x, self.y))


def initialize_snow(max_snow, snowfall):    # будет создавать снежинки и создавать случайные им положения
    for i in range(0, max_snow):
        xx = random.randint(0, Max_x)
        yy = random.randint(0, Max_y)
        snowfall.append(Snow(xx, yy))


def check_for_exit(): # закрывает экран
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            sys.exit()


# ------------ Main ----------
pygame.init()
screen = pygame.display.set_mode((Max_x, Max_y), pygame.FULLSCREEN)
bg_color = (0, 0, 0)        # меняем фон
snowfall = []

initialize_snow(Max_snow, snowfall)

while True:
    x = random.randint(0, 255)
    y = random.randint(0, 255)
    z = random.randint(0, 255)
    screen.fill((x, y, z))  #  каждый раз меняем фон
    check_for_exit()
    for i in snowfall:
        i.move_snow()   # двигаем картинку
        i.draw_snow()    # рисуем каждую картинку
    time.sleep(0.05)
    pygame.display.flip()

