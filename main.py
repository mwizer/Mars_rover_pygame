import pygame


fps = 60
screen_width = 1200
screen_height = 900

game_screen = pygame.display.set_mode((screen_width, screen_height))

background_image = pygame.image.load("assets//33ec482c083bbd739ca2146d70bbe84d.jpg")
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

hover_image = pygame.image.load("assets//hover.png")
hover_width = 49
hover_height = 39


def draw_window(hover):
    """Funkcja do nanoszenia obrazu na okno"""

    game_screen.blit(background_image, (0, 0))
    game_screen.blit(hover_image, (hover.x, hover.y))

def main():
    pygame.init()
    run = True
    clock = pygame.time.Clock()

    hover = pygame.Rect(screen_width / 2, screen_height / 2, (hover_width, hover_height))

    while run:
        clock.tick(fps)



        draw_window(hover)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        key_pressed = pygame.key.get_pressed()


        if key_pressed[pygame.K_a]:
            hover.x -= 1


        pygame.display.update()



if __name__ == "__main__":
    main()