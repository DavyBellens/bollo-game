import pygame
screensize=(1024, 650)
game_running = True
surface=pygame.display.set_mode(screensize)

def create_main_surface():
    return surface

def main():
    create_main_surface()
    while game_running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()


def clear_main_surface():
    empty = (0,0,0,0)
    surface.fill(empty)


main()