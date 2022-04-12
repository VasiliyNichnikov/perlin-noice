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

    @property
    def black(self) -> Tuple[int, int, int]:
        return self.__black

    @property
    def white(self) -> Tuple[int, int, int]:
        return self.__white


class Config(BaseConfig):
    def __init__(self) -> None:
        super().__init__()
        self.__screen = Screen(self._config["screen"])
        self.__caption = Caption(self._config["caption"])
        self.__colors = Colors(self._config["colors"])

    @property
    def screen(self) -> Screen:
        return self.__screen

    @property
    def caption(self) -> Caption:
        return self.__caption

    @property
    def colors(self) -> Colors:
        return self.__colors


def get_config() -> Config:
    return Config()
