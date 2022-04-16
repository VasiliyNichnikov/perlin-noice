import pygame.draw
from pygame import Surface, Vector2

from calculations import calculate_position_end_by_angle
from map.direction import DirectionOctaves
from map.points import Points
from pygame_base import GameObject
from utils import get_config


class Octave(GameObject):
    def __init__(self, surface: Surface) -> None:
        super().__init__(surface)
        self.__directions = DirectionOctaves()
        self.__points = Points(self.__directions)
        self.__config = get_config()

    def update(self) -> None:
        self.__draw_point()

    def __draw_point(self) -> None:
        for line in self.__points.get():
            for point in line:
                color = (point.depth_y * 255, point.depth_y * 255, point.depth_y * 255)
                pygame.draw.rect(self._surface, color, point.rect)

    # TODO fix
    def __draw_directions(self) -> None:
        color = self.__config.colors.misty_rose
        self.draw_direction(color, (50, 50), self.__config.octave.angle_top_left)
        self.draw_direction(color, (50, 450), self.__config.octave.angle_bottom_left)
        self.draw_direction(color, (450, 50), self.__config.octave.angle_top_right)
        self.draw_direction(color, (450, 450), self.__config.octave.angle_bottom_right)

    def draw_direction(self, color, start, angle) -> None:
        start = Vector2(start)
        length = 50
        end = calculate_position_end_by_angle(start, angle, length)
        pygame.draw.line(self._surface, color, start, end)
