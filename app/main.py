from __future__ import annotations

import math


class Vector:

    def __init__(self, x, y) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other) -> Vector | float:
        if isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(
        cls, start_point: tuple, end_point: tuple
    ) -> Vector:
        return cls(
            x=end_point[0] - start_point[0],
            y=end_point[1] - start_point[1],
        )

    def get_length(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, vector: Vector) -> int:
        cosine_a = (self * vector) / (self.get_length() * vector.get_length())
        return round(math.degrees(math.acos(cosine_a)))

    def get_angle(self):
        return round(math.degrees(math.acos(self.y / self.get_length())))

    def rotate(self, angle):
        angle_rad = math.radians(angle)
        return Vector(
            x=self.x * math.cos(angle_rad) - self.y * math.sin(angle_rad),
            y=self.x * math.sin(angle_rad) + self.y * math.cos(angle_rad),
        )
