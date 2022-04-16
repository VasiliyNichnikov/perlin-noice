from math import cos, sin, pi

from pygame import Vector2


def calculate_position_end_by_angle(start: Vector2, angle: int, length: int) -> Vector2:
    x1, y1 = start
    radian = convert_from_degrees_to_radians(angle)
    x2, y2 = (x1 + length * cos(radian), y1 + length * sin(radian))
    return Vector2(x2, y2)


def convert_from_degrees_to_radians(angle: float) -> float:
    return angle * pi / 180


def lerp(t: float, a: float, b: float) -> float:
    return a + (b - a) * t


def smoothstep(t: float | int) -> float:
    return t * t * (3. - 2. * t)

