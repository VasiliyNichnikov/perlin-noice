import os.path
from abc import ABC
from typing import Dict, MutableMapping, Any, Tuple

import toml
from pygame import Vector2

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
PATH_CONFIG = f"{ROOT_DIR}/config.toml"


class BaseConfig(ABC):
    def __init__(self) -> None:
        with open(PATH_CONFIG, 'r', encoding="utf-8") as file:
            data = toml.loads(file.read())
            self.__config = data["config"]

    @property
    def _config(self) -> MutableMapping[str, Any]:
        return self.__config


class Screen:
    def __init__(self, data: Dict) -> None:
        self.__width = data["width"]
        self.__height = data["height"]
        self.__fps = data["fps"]

    @property
    def width(self) -> int:
        return self.__width

    @property
    def height(self) -> int:
        return self.__height

    @property
    def fps(self) -> int:
        return self.__fps


class Caption:
    def __init__(self, data: Dict) -> None:
        self.__name = data["name"]

    @property
    def name(self) -> str:
        return self.__name


class Colors:
    def __init__(self, data: Dict) -> None:
        self.__black = tuple(data["black"])
        self.__white = tuple(data["white"])
        self.__blue_violet = tuple(data["blue_violet"])
        self.__azure = tuple(data["azure"])
        self.__lemon_chiffon = tuple(data["lemon_chiffon"])
        self.__misty_rose = tuple(data["misty_rose"])

    @property
    def black(self) -> Tuple[int, int, int]:
        return self.__black

    @property
    def white(self) -> Tuple[int, int, int]:
        return self.__white

    @property
    def blue_violet(self) -> Tuple[int, int, int]:
        return self.__blue_violet

    @property
    def lemon_chiffon(self) -> Tuple[int, int, int]:
        return self.__lemon_chiffon

    @property
    def misty_rose(self) -> Tuple[int, int, int]:
        return self.__misty_rose


class Octave:
    def __init__(self, data: Dict) -> None:
        self.__angle_top_left = data["angle_top_left"]
        self.__angle_top_right = data["angle_top_right"]
        self.__angle_bottom_left = data["angle_bottom_left"]
        self.__angle_bottom_right = data["angle_bottom_right"]

    @property
    def angle_top_left(self) -> int:
        return self.__angle_top_left

    @property
    def angle_top_right(self) -> int:
        return self.__angle_top_right

    @property
    def angle_bottom_left(self) -> int:
        return self.__angle_bottom_left

    @property
    def angle_bottom_right(self) -> int:
        return self.__angle_bottom_right


class Map:
    def __init__(self, data: Dict, width: int) -> None:
        self.__width = width
        self.__size_block = data["size_block"]
        self.__boundaries_between_blocks = data["boundaries_between_blocks"]
        self.__frame = data["frame"]
        self.__number_of_blocks = int((width - self.__frame) / (self.__size_block + self.__boundaries_between_blocks))

    @property
    def size_block(self) -> int:
        return self.__size_block

    @property
    def borders(self) -> int:
        return self.__boundaries_between_blocks

    @property
    def number_of_blocks(self) -> int:
        return self.__number_of_blocks

    @property
    def half_frame(self) -> int:
        return self.__frame // 2

    @property
    def position_top_left(self) -> Vector2:
        return Vector2(0, 0)

    @property
    def position_top_right(self) -> Vector2:
        return Vector2(self.__number_of_blocks, 0)

    @property
    def position_bottom_left(self) -> Vector2:
        return Vector2(0, self.__number_of_blocks)

    @property
    def position_bottom_right(self) -> Vector2:
        return Vector2(self.__number_of_blocks, self.__number_of_blocks)


class Config(BaseConfig):
    def __init__(self) -> None:
        super().__init__()
        self.__screen = Screen(self._config["screen"])
        self.__caption = Caption(self._config["caption"])
        self.__colors = Colors(self._config["colors"])
        self.__map = Map(self._config["map"], self.__screen.width)
        self.__octave = Octave(self._config["octave"])

    @property
    def screen(self) -> Screen:
        return self.__screen

    @property
    def caption(self) -> Caption:
        return self.__caption

    @property
    def colors(self) -> Colors:
        return self.__colors

    @property
    def map(self) -> Map:
        return self.__map

    @property
    def octave(self) -> Octave:
        return self.__octave


__config = None


def get_config() -> Config:
    global __config
    if __config is None:
        __config = Config()
        return __config
    return __config
