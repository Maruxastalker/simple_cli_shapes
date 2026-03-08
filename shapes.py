from dataclasses import dataclass

@dataclass
class Point:
    id: int
    x: float
    y: float


@dataclass
class Segment:
    id: int
    x1: float
    y1: float
    x2: float
    y2: float


@dataclass
class Circle:
    id: int
    x: float
    y: float
    r: float


@dataclass
class Square:
    id: int
    x: float
    y: float
    a: float