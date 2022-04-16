import math
from typing import List, Tuple

from pygame import Rect
from pygame import Vector2

from calculations import lerp, smoothstep
from map.direction import DirectionBlocks, DirectionOctaves
from utils import get_config


class Point:
    def __init__(self, position: Vector2, size: Tuple[int, int]) -> None:
        self.__config = get_config()
        self.__position = position
        self.__size = size
        self.__rect = self.__init_rect()
        self.__directions = DirectionBlocks(self)
        self.__depth_y = 0

    def __init_rect(self) -> Rect:
        x = self.__position.x * self.__size[0] + \
            self.__config.map.borders * self.__position.x + self.__config.map.half_frame
        y = self.__position.y * self.__size[1] + \
            self.__config.map.borders * self.__position.y + self.__config.map.half_frame
        return Rect(Vector2(x, y), self.__size)

    @property
    def depth_y(self) -> float:
        return self.__depth_y

    @depth_y.setter
    def depth_y(self, value: float) -> None:
        self.__depth_y = value

    @property
    def rect(self) -> Rect:
        return self.__rect

    @property
    def directions(self) -> DirectionBlocks:
        return self.__directions

    @property
    def center(self) -> Vector2:
        return Vector2(self.__position.x + 0.5, self.__position.y + 0.5)

    def calculate_depth(self, octave: DirectionOctaves) -> None:
        smooth_x = smoothstep(0.5)
        smooth_y = smoothstep(0.5)

        dot_top_left = self.__directions.top_left.dot(octave.top_left)
        dot_top_right = self.__directions.top_right.dot(octave.top_right)
        dot_bottom_left = self.__directions.bottom_left.dot(octave.bottom_left)
        dot_bottom_right = self.__directions.bottom_right.dot(octave.bottom_right)

        lerp_top = lerp(smooth_x, dot_top_left, dot_top_right)
        lerp_bottom = lerp(smooth_x, dot_bottom_left, dot_bottom_right)

        self.__depth_y = lerp(smooth_y, lerp_top, lerp_bottom)


class Points:
    def __init__(self, octave: DirectionOctaves) -> None:
        self.__points: List[List[Point]] = []

        self.__config = get_config()
        self.__min, self.__max = math.inf, -math.inf
        self.__octave = octave
        self.__init()

    def get(self) -> List[List[Point]]:
        return self.__points

    def __init(self) -> None:
        size_block = self.__config.map.size_block

        for y in range(self.__config.map.number_of_blocks):
            line_blocks = []
            for x in range(self.__config.map.number_of_blocks):
                p = Point(Vector2(x, y), (size_block, size_block))
                p.calculate_depth(self.__octave)
                if p.depth_y < self.__min:
                    self.__min = p.depth_y
                elif p.depth_y > self.__max:
                    self.__max = p.depth_y
                line_blocks.append(p)
            self.__points.append(line_blocks)
        self.__normalize()

    def __normalize(self) -> None:
        for line in self.__points:
            for point in line:
                point.depth_y = (point.depth_y - self.__min) / (self.__max - self.__min)
