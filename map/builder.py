import pygame
from pygame import Surface, Rect
from utils import get_config


class Builder:
    def __init__(self, surface: Surface) -> None:
        self.__config = get_config()
        self.__surface = surface

    def draw_map(self) -> None:
        parameters_map = self.__config.map
        size_block = parameters_map.size_block
        pos_x, pos_y = parameters_map.borders, parameters_map.borders
        one_step = size_block + parameters_map.borders * 2

        for y in range(self.__config.map.number_of_blocks):
            for x in range(self.__config.map.number_of_blocks):
                rect = Rect((pos_x, pos_y, size_block, size_block))
                self.__draw_block(rect)
                pos_x += one_step
            pos_x = parameters_map.borders
            pos_y += one_step

    def __draw_block(self, rect: Rect) -> None:
        pygame.draw.rect(self.__surface, self.__config.colors.white, rect)

