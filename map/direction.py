import math
from typing import Tuple
from pygame import Surface
import pygame
from utils import get_config


class Direction:
    # (x2,y2) = (x1 + line_length*cos(angle),y1 + line_length*sin(angle))

    length = 50
    line_width = 2

    def __init__(self, surface: Surface, position: Tuple[float, float]) -> None:
        self.__start = position
        self.__surface = surface
        self.__config = get_config()

    def draw(self, angle: int = 0) -> None:
        x1, y1 = self.__start
        radian = self.__convert_from_degrees_to_radians(angle)
        x2, y2 = (x1 + self.length * math.cos(radian), y1 + self.length * math.sin(radian))

        pygame.draw.line(self.__surface, self.__config.colors.black, (x1, y1), (x2, y2), self.line_width)

    @staticmethod
    def __convert_from_degrees_to_radians(angle: int) -> float:
        return angle * math.pi / 180
