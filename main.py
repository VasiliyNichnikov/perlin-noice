import pygame

from utils import get_config
from map.builder import Builder


def init_pygame() -> None:
    pygame.init()
    pygame.mixer.init()


def main() -> None:
    init_pygame()

    config = get_config()
    fps = config.screen.fps
    screen = pygame.display.set_mode((config.screen.width, config.screen.height))
    pygame.display.set_caption(config.caption.name)
    clock = pygame.time.Clock()
    running = True

    builder = Builder(screen)
    while running:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Rendering
        screen.fill(config.colors.blue_violet)

        # Update
        builder.draw_map()
        # Flip screen
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
