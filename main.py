import pygame

fps = 60
screen_width = 1200
screen_height = 900

game_screen = pygame.display.set_mode((screen_width, screen_height))  # ustawienie okna gry

background_image = pygame.image.load("assets//33ec482c083bbd739ca2146d70bbe84d.jpg") # dodawnie obrazu w tle
background_image = pygame.transform.scale(background_image, (screen_width, screen_height)) # skalowanie obrazu w tle, do okna

hover_image = pygame.image.load("assets//hover.png")  # dodawnie obrazu
hover_width = 49
hover_height = 39


def draw_window(hover):
    """Funkcja do nanoszenia obrazu na okno"""

    game_screen.blit(background_image, (0, 0))  # dodawanie tła
    game_screen.blit(hover_image, (hover.x, hover.y))  # dodawanie łazika w miejscu hover.x i hover.y na mapie


def hover_movement(keys, hover):
    """Poruszanie sie łazika"""

    if keys[pygame.K_a]:  # w lewo
        hover.x -= 1
    if keys[pygame.K_d]:  # w prawo
        hover.x += 1
    if keys[pygame.K_w]:  # w górę
        hover.y -= 1
    if keys[pygame.K_s]:  # w dół
        hover.y += 1


def main():
    pygame.init()  # inicjalizacja gry

    clock = pygame.time.Clock()

    hover = pygame.Rect(screen_width / 2, screen_height / 2, hover_width, hover_height)  # utworzenie obiektu łazika, przechowującego informację o położeniu x,y i wymiarach

    run = True
    while run:
        clock.tick(fps)
        draw_window(hover)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # sprawdza "eventy", które dzieją się w danej chwili, jeśli jest to wciśnięcie guzika zamykającego okno, kończy grę
                run = False

        key_pressed = pygame.key.get_pressed()  # sprawdza które przyciski są wciśnięte w danej chwili
        hover_movement(key_pressed, hover)  # wywołanie funkcji do zmiany wartości x i y łazika (poruszania się)

        pygame.display.update()  # odświeża nasze okno


if __name__ == "__main__":
    main()
