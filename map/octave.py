from pygame import Surface
from map.direction import Direction


class Octave:
    def __init__(self, surface: Surface) -> None:
        self.__top_left = Direction(surface, (50, 50))
        self.__top_right = Direction(surface, (450, 50))
        self.__bottom_left = Direction(surface, (50, 450))
        self.__bottom_right = Direction(surface, (450, 450))

    def draw(self) -> None:
        self.__top_left.draw(60)
        self.__top_right.draw(-25)
        self.__bottom_left.draw(61)
        self.__bottom_right.draw(-35)