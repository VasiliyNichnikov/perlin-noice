from pygame import Surface

from map.octave import Octave
from utils import get_config
from pygame_base import GameObject


class Builder(GameObject):
    def __init__(self, surface: Surface) -> None:
        super().__init__(surface)

        self.__config = get_config()
        self.__octave = Octave(self._surface)

    def update(self) -> None:
        self.__octave.update()

