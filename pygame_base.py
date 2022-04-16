from abc import ABC, abstractmethod

from pygame import Surface


class GameObject(ABC):
    def __init__(self, surface: Surface) -> None:
        self._surface = surface

    @abstractmethod
    def update(self) -> None:
        pass
