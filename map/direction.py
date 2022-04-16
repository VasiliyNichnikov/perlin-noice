import random

from pygame import Vector2

from calculations import calculate_position_end_by_angle
from utils import get_config


class Direction:
    __length = 50

    def __init__(self, start: Vector2, **kwargs):
        self.__start = start
        self.__end = self.__get_position_end(**kwargs)

    @property
    def vector(self) -> Vector2:
        return self.__end - self.__start

    @property
    def start(self) -> Vector2:
        return self.__start

    @property
    def end(self) -> Vector2:
        return self.__end

    def __get_position_end(self, **kwargs) -> Vector2:
        keys = list(kwargs.keys())
        if "angle" in keys:
            angle = kwargs["angle"]
            return calculate_position_end_by_angle(self.__start, angle, self.__length)
        elif "random" in keys and kwargs["random"]:
            angle = random.randint(-90, 90)
            return calculate_position_end_by_angle(self.__start, angle, self.__length)
        elif "end" in keys:
            return kwargs["end"]
        else:
            raise Exception("Invalid parameters")


class DirectionFour:
    _top_left: Direction = None
    _top_right: Direction = None
    _bottom_left: Direction = None
    _bottom_right: Direction = None

    def __init__(self) -> None:
        self._config = get_config()
        self._map = self._config.map

    @property
    def top_left(self) -> Vector2:
        return self._top_left.vector.normalize()

    @property
    def top_right(self) -> Vector2:
        return self._top_right.vector.normalize()

    @property
    def bottom_left(self) -> Vector2:
        return self._bottom_left.vector.normalize()

    @property
    def bottom_right(self) -> Vector2:
        return self._bottom_right.vector.normalize()


class DirectionOctaves(DirectionFour):
    def __init__(self) -> None:
        super().__init__()
        self._top_left = Direction(self._map.position_top_left, angle=self._config.octave.angle_top_left)
        self._top_right = Direction(self._map.position_top_right, angle=self._config.octave.angle_top_right)
        self._bottom_left = Direction(self._map.position_bottom_left, angle=self._config.octave.angle_bottom_left)
        self._bottom_right = Direction(self._map.position_bottom_right, angle=self._config.octave.angle_bottom_right)


class DirectionBlocks(DirectionFour):
    def __init__(self, point) -> None:
        super().__init__()
        block_center = point.center

        self._top_left = Direction(self._map.position_top_left, end=block_center)
        self._top_right = Direction(self._map.position_top_right, end=block_center)
        self._bottom_left = Direction(self._map.position_bottom_left, end=block_center)
        self._bottom_right = Direction(self._map.position_bottom_right, end=block_center)
