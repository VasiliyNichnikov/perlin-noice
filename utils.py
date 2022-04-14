import os.path
from abc import ABC
from typing import Dict, MutableMapping, Any, Tuple

import toml

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

    @property
    def black(self) -> Tuple[int, int, int]:
        return self.__black

    @property
    def white(self) -> Tuple[int, int, int]:
        return self.__white

    @property
    def blue_violet(self) -> Tuple[int, int, int]:
        return self.__blue_violet


class Map:
    def __init__(self, data: Dict, width: int) -> None:
        self.__size_block = data["size_block"]
        self.__boundaries_between_blocks = data["boundaries_between_blocks"]
        self.__frame = data["frame"]
        self.__number_of_blocks = int((width - self.__frame) / (self.__size_block + self.__boundaries_between_blocks))

    @property
    def size_block(self) -> int:
        return self.__size_block

    @property
    def borders(self) -> int:
        return self.__boundaries_between_blocks / 2

    @property
    def number_of_blocks(self) -> int:
        return self.__number_of_blocks

    @property
    def half_frame(self) -> int:
        return self.__frame // 2


class Config(BaseConfig):
    def __init__(self) -> None:
        super().__init__()
        self.__screen = Screen(self._config["screen"])
        self.__caption = Caption(self._config["caption"])
        self.__colors = Colors(self._config["colors"])
        self.__map = Map(self._config["map"], self.__screen.width)

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


__config = None


def get_config() -> Config:
    global __config
    if __config is None:
        __config = Config()
        return __config
    return __config
