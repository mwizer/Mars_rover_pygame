import random

import pygame

pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)

fps = 60
screen_width = 1200
screen_height = 900

game_screen = pygame.display.set_mode((screen_width, screen_height))  # ustawienie okna gry

background_image = pygame.image.load("assets//33ec482c083bbd739ca2146d70bbe84d.jpg")  # dodawnie obrazu w tle
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))  # skalowanie obrazu w tle, do okna

hover_image = pygame.image.load("assets//hover.png")  # dodawnie obrazu
hover_width = 49
hover_height = 39


class Hover:
    """Klasa zawierająca informajce o łaziku"""

    def __init__(self, x, y, width, height):
        self.name = "hover"
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.vel = 2  # szybkość łazika
        self.hp = 3
        self.score = 0

class Sample:
    """Klasa próbki"""

    def __init__(self):

        self.name = "sample"
        self.width = 64
        self.height = 64
        self.x = random.randint(0, screen_width - self.width)
        self.y = random.randint(0, screen_height - self.height)

        self.image = pygame.image.load("assets//sample1.png")
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

        self.screen_time = 0
        self.screen_time_limit = 10

    def timer(self):
        self.screen_time += 1  # na zmienną time warto uważać, bo ta zmienna może być zarezerwowana i przez to program może nie działać

    def timer_limit(self):
        if self.screen_time == self.screen_time_limit:
            return True
        else:
            return False

    def collision(self, hover):
        hover.score += random.randint(10, 20)
        return True

    def draw(self):
        game_screen.blit(self.image, (self.x, self.y))

class Sandstorm:
    """Klasa burzy piaskowej"""  # na Marsie to bardziej Dust_storm :P

    def __init__(self):

        self.name = "sandstorm"
        self.width = 64
        self.height = 64
        self.x = random.randint(0, screen_width - self.width)
        self.y = random.randint(0, screen_height - self.height)

        self.image = pygame.image.load("assets//sandstorm1.png")
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

        self.screen_time = 0
        self.screen_time_limit = 10

        self.vel = 5
        self.dir_x = random.randint(-1, 1)  # losowa liczba  -1 / 0 / 1
        self.dir_y = random.randint(-1, 1)

    def movement(self):

        if self.dir_x == -1:  # w lewo
            self.x -= self.vel
        if self.dir_x == 1:  # w prawo
            self.x += self.vel
        if self.dir_y == 1:  # w dół
            self.y += self.vel
        if self.dir_y == -1:  # w górę
            self.y -= self.vel

        if self.x < 0 or (self.x + self.width) > screen_width:
            self.dir_x *= (-1)  # dirx = dirx * (-1)
        if self.y < 0 or (self.y + self.height) > screen_height:
            self.dir_y *= (-1)

    def timer(self):
        self.screen_time += 1  # na zmienną time warto uważać, bo ta zmienna może być zarezerwowana i przez to program może nie działać

    def timer_limit(self):
        if self.screen_time == self.screen_time_limit:
            return True
        else:
            return False

    def collision(self, hover):
        hover.hp -= 1
        if hover.hp == 0:
            return False
        return True

    def draw(self):
        game_screen.blit(self.image, (self.x, self.y))

def draw_obstacle(time, obstacle_list, hover, run):
    if time % (fps * 5) == 0:
        obstacle_list.append(Sample())

    if time % (fps * 2) == 0:
        obstacle_list.append(Sandstorm())

    if obstacle_list != []:
        for obstacle in obstacle_list:
            obstacle.draw()

            if obstacle.name == "sandstorm":
                obstacle.movement()

            if hover.x < obstacle.x + obstacle.width and hover.x + hover.width > obstacle.x and hover.y < obstacle.y + obstacle.height and hover.y + hover.height > obstacle.y:
                run = obstacle.collision(hover)
                obstacle_list.remove(obstacle)
                print(hover.hp, hover.score)

            if time % fps == 0:
                obstacle.timer()

                if obstacle.timer_limit() == True:
                    obstacle_list.remove(obstacle)

    return run

def score_board(hover):
    pygame.draw.rect(game_screen, [0, 0, 0], [0, 0, 175, 100])  # taki prostokąt

    text = my_font.render(f"HP : {hover.hp}", False, (255, 255, 255))  # <- kolor biały
    game_screen.blit(text, (10, 0))
    text = my_font.render(f"Score : {hover.score}", False, (255, 255, 255))  # <- kolor biały
    game_screen.blit(text, (10, 45))

def draw_window(hover):
    """Funkcja do nanoszenia obrazu na okno"""

    game_screen.blit(background_image, (0, 0))  # dodawanie tła
    game_screen.blit(hover_image, (hover.x, hover.y))  # dodawanie łazika w miejscu hover.x i hover.y na mapie
    score_board(hover)

def hover_movement(keys, hover):
    """Poruszanie sie łazika"""

    if keys[pygame.K_a] and hover.x - 1 > 0:  # w lewo
        hover.x -= hover.vel
    if keys[pygame.K_d] and (hover.x + hover.width) < screen_width:  # w prawo
        hover.x += hover.vel
    if keys[pygame.K_w] and hover.y > 0:  # w górę
        hover.y -= hover.vel
    if keys[pygame.K_s] and (hover.y + hover.height) < screen_height:  # w dół
        hover.y += hover.vel

def main():
    pygame.init()  # inicjalizacja gry

    clock = pygame.time.Clock()

    hover = Hover(screen_width / 2, screen_height / 2, hover_width, hover_height)  # utworzenie obiektu łazika, przechowującego informację o położeniu x,y i wymiarach

    obstacle_list = []
    time = 0

    run = True
    while run:
        clock.tick(fps)
        draw_window(hover)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # sprawdza "eventy", które dzieją się w danej chwili, jeśli jest to wciśnięcie guzika zamykającego okno, kończy grę
                run = False

        key_pressed = pygame.key.get_pressed()  # sprawdza które przyciski są wciśnięte w danej chwili
        hover_movement(key_pressed, hover)  # wywołanie funkcji do zmiany wartości x i y łazika (poruszania się)

        if time == fps * 10:
            time = 0

        run = draw_obstacle(time, obstacle_list, hover, run)

        time += 1  # += time = time +1
        pygame.display.update()  # odświeża nasze okno


if __name__ == "__main__":
    main()
